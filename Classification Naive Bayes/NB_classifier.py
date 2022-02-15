from collections import defaultdict
from math import log10, pow


class NB_classifier():

    def __init__(self):
        self.all_words = set()

    def clear_docs(self, array_of_documents: list) -> list():
        """
        :param array_of_documents - take array of array of words:
        :return array of array of cleared words:
        """
        if len(array_of_documents) > 1:
            for index, dokument in enumerate(array_of_documents):
                for p in [',', '.']:
                    dokument = dokument.replace(p, '')
                array_of_documents[index] = dokument.lower().split()
        for i in array_of_documents:
            for word in i:
                if word:
                    self.all_words.add(word)
        return array_of_documents

    def get_set_of_words(self):
        return self.all_words

    def create_dict(self, docs, clas):
        """
        :param docs - array of documents:
        :param clas - array of documents class:
        :return dict of dicts where key is class and value is bag of words for classes:
        """
        key_used = []
        dct = defaultdict(dict)
        for key, value in zip(clas, docs):
            words = []
            for word in value:
                if key not in key_used:
                    dct[key][word] = 1
                elif key not in key_used and dct[key][word]:
                    continue
                elif key in key_used and word not in dct[key].keys() and word not in words:
                    dct[key][word] = 1
                elif key in key_used and word in dct[key].keys() and word not in words:
                    dct[key][word] += 1
                words.append(word)
            key_used.append(key)
        return dct

    def table_for_word(self, dict_of_dicts, word, clas_array):
        """
        :param dict_of_dicts - dict form create_dict():
        :param word - looking word:
        :param clas_array - vector of documents class:
        :return array  (N00 N10 N01 N11):
        """
        # array N00 N01 N10 N11
        word_in_clases = {}
        how_many_dosc_in_clas = {}
        array = []
        for i in range(len(dict_of_dicts)):
            if word in dict_of_dicts[i].keys():
                word_in_clases[i] = dict_of_dicts[i][word]
                how_many_dosc_in_clas[i] = len([clas for clas in clas_array if clas == i])
            else:
                word_in_clases[i] = 0
                how_many_dosc_in_clas[i] = len([clas for clas in clas_array if clas == i])
        for key, value in how_many_dosc_in_clas.items():
            how_many_dosc_in_clas[key] = how_many_dosc_in_clas[key] - word_in_clases[key]
        for i in range(len(dict_of_dicts)):
            array.append(how_many_dosc_in_clas[i])
            array.append(word_in_clases[i])
        return array

    def chi(self, N00, N10, N01, N11):
        """
        :param Nxx - value of N:
        :return chi value:
        """
        N = N00 + N10 + N01 + N11
        N_1 = N01 + N11
        N1_ = N10 + N11
        N_0 = N10 + N00
        N0_ = N01 + N00
        try:
            output = log10((N * pow(N11 * N00 - N10 * N01, 2)) / (N_1 * N1_ * N_0 * N0_))
        except ZeroDivisionError as e:
            print(f'Error: {e}')
            output = 0
        return output

    def total_term(self, cleared, classes, clas):
        counted_words = 0
        for classes, array_of_word in zip(classes, cleared):
            if classes == clas:
                for _ in array_of_word:
                    counted_words += 1
        return counted_words

    def word_in_class(self, cleared, classes, clas, looked_word):
        counter_of_looked_word = 0
        for classes, array_of_word in zip(classes, cleared):
            if classes == clas:
                for word in array_of_word:
                    if word == looked_word:
                        counter_of_looked_word += 1
        return counter_of_looked_word


if __name__ == '__main__':
    # input data
# 3
# You care set up, do not pluck my care down.
# My care is loss of care with old care done.
# Your care is gain of care when new care is won.
# 0 1 1
# Care is loss when my gain is won
# 8

    # entry data
    docs = []
    num_docs = int(input())
    for i in range(num_docs):
        doc = input()
        docs.append(doc)
    clas = input().split()
    clas = [int(i) for i in clas]
    query = input()
    feature_selection = int(input())

    # clear data and create defaultdict(dict)
    nb = NB_classifier()
    cleared = nb.clear_docs(docs)
    dct_for_classes = nb.create_dict(cleared, clas)

    # clear query
    for p in [',', '.']:
        query = query.replace(p, '')
    query = query.lower().split()

    # find n words
    dic_of_chi = {}
    for word in nb.get_set_of_words():
        table_in_array = nb.table_for_word(dct_for_classes, word, clas)
        chi = nb.chi(table_in_array[0], table_in_array[1], table_in_array[2], table_in_array[3])
        dic_of_chi[word] = chi
    dic_of_chi = sorted(dic_of_chi.items(), key=lambda x: x[1], reverse=True)[:feature_selection]
    dic_of_words = [word for word, _ in dic_of_chi]

    # Naive bayes
    output = {}
    for class_counted in set(clas):
        word_weights = {}
        for looked_word in dic_of_words:
            num_of_words_in_class = nb.total_term(cleared, clas, class_counted)
            num_of_looked_word_in_class = nb.word_in_class(cleared, clas, class_counted, looked_word)
            word_weights.update(
                {looked_word: log10((num_of_looked_word_in_class + 1) / (num_of_words_in_class + len(dic_of_words)))})
        probability = log10(len([i for i in clas if i == class_counted]) / len(clas))
        for word in query:
            if word in word_weights.keys():
                probability += word_weights[word]
        output[class_counted] = probability
    print(sorted(output.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0])
