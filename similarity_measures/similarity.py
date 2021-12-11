from collections import Counter
from math import log10
from math import sqrt
class similarity_based_on_TFIDF:
    def __init__(self):
        self.all_content={}
        self.nb_of_documents=0
    def read_data(self,file_name:str):
        """
        :param file_name - path to file with data:
        :return cleared data:
        """
        with open(file_name,'r',encoding='utf-8') as f:
            all_data=f.read().splitlines()
            self.nb_of_documents=int(all_data[0])
            docs=all_data[1:self.nb_of_documents+1]
            looking_words=all_data[-1]
            return docs,looking_words
    def clear_words(self,phrase:str,looking_words=False):
            """
            :phrase - its array og string to clear :
            :looking_words - if True then no add to all content:
            :return: Cleared strings (lemat, low etc.)
            """
            for p in [',', '.']:
                phrase = phrase.replace(p, '')
            phrase=phrase.lower().split()
            if not looking_words:
                for word in set(phrase):
                    if word in self.all_content:
                        self.all_content[word] = self.all_content[word] + 1
                    else:
                        self.all_content[word] = 1
            return phrase
    """ tf= the number of occurrences of a term divided by the number of highest occurrences of the term in the sentence (ti/max(ti))"""
    def TF(self,table_of_cleared_words:str):
            counted_words_dict=dict(Counter(table_of_cleared_words))
            max_value=counted_words_dict[max(counted_words_dict, key=counted_words_dict.get)]
            counted_words_dict = {key: counted_words_dict[key] / max_value for key in counted_words_dict}
            return counted_words_dict
    """ idf= calculates the logarithm of 10 of the number of most frequently used words in documents by the number of occurrences of the word in the given documents (lgm(max(nt)/nt)"""
    def IDF(self):
        idf_dict = self.all_content
        max_value_title = self.nb_of_documents
        counted_words_dict_title = {key: log10(max_value_title / idf_dict[key]) for key in idf_dict}
        return counted_words_dict_title
    def TF_IDF(self, TF_dict: str, IDF_dict: dict):
        for key in TF_dict.keys():
            TF_dict[key] = TF_dict[key] * IDF_dict[key]

        return TF_dict
    def append_other_words(self,dict_of_words:dict):
        """
        :param dict_of_words:
        :return dict append of idf words with value 0:
        """
        for key in self.all_content.keys():
            if key not in dict_of_words.keys():
                dict_of_words[key]=0
        return {key:value for key,value in sorted(dict_of_words.items(), key=lambda item: item[0])}
    def product_measure(self,dict,dics_looking_words):
        """
        :param dict_0 - sorted and filled TF_IDF dict:
        :param looking_words - array of looking words:
        :return distance measure between dicts:
        """
        sum_measure=0
        for word in dics_looking_words.keys():
            if word in dict.keys():
                sum_measure+=dict[word]*dics_looking_words[word]
        return round(sum_measure,2)
    def dice(self,dict,dics_looking_words):
        """
        :param dict_0 - sorted and filled TF_IDF dict:
        :param looking_words - array of looking words:
        :return distance measure between dicts:
        """
        numerator=0
        denominator_1 = 0
        denominator_2 = 0
        for word in dics_looking_words.keys():
            if word in dict.keys():
                numerator+=dict[word]
                denominator_1+=dict[word]**2
                denominator_2+=dics_looking_words[word]**2
        try:
            sum_measure=2*numerator/(denominator_1*denominator_2)

        except ZeroDivisionError:
            sum_measure=0
        return round(sum_measure, 2)
    def jaccard(self,dict,dics_looking_words):
        """
        :param dict_0 - sorted and filled TF_IDF dict:
        :param looking_words - array of looking words:
        :return distance measure between dicts:
        """
        numerator=0
        denominator_1 = 0
        denominator_2 = 0
        for word in dics_looking_words.keys():
            if word in dict.keys():
                numerator+=dict[word]
                denominator_1+=dict[word]**2
                denominator_2+=dics_looking_words[word]**2
        sum_measure=numerator/(denominator_1+denominator_2-numerator)
        return round(sum_measure,2)
    def cos_measure(self, dict, dics_looking_words):
        """
        :param dict_0 - sorted and filled TF_IDF dict:
        :param looking_words - array of looking words:
        :return distance measure between dicts:
        """
        numerator = 0
        denominator_1 = 0
        denominator_2 = 0
        for word in dics_looking_words.keys():
            if word in dict.keys():
                numerator += dict[word]
                denominator_1 += dict[word] ** 2
                denominator_2 += dics_looking_words[word] ** 2
        try:
            sum_measure = numerator / (sqrt(denominator_1) * sqrt(denominator_2))
        except ZeroDivisionError:
            sum_measure=0
        return round(sum_measure, 2)

if __name__ == '__main__':
    # read data
    similarity=similarity_based_on_TFIDF()
    docs,looking_words=similarity.read_data('input.txt')

    #clear looking words
    TF_docs=[]
    cleared_words=similarity.clear_words(looking_words,looking_words=True)
    dics_looking_words={word: 1 for word in cleared_words}
    for doc in docs:
        # clear docs
        cleared_doc =similarity.clear_words(doc)
        #TF measures
        TF_docs.append(similarity.TF(cleared_doc))

    # idf measure
    idf=similarity.IDF()

    #distance measures for TF_IDF
    for TF_doc in TF_docs:
        output = []
        TF_IDF= similarity.TF_IDF(TF_doc,idf)
        TF_IDF=similarity.append_other_words(TF_IDF)
        # print(TF_IDF)
        # print(dics_looking_words)
        output.append(similarity.product_measure(TF_IDF,dics_looking_words))
        output.append(similarity.dice(TF_IDF, dics_looking_words))
        output.append(similarity.jaccard(TF_IDF, dics_looking_words))
        output.append(similarity.cos_measure(TF_IDF, dics_looking_words))
        print(output)



