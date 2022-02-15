from collections import Counter
from math import log10, pow, sqrt


class KNN_classifier():

    def __init__(self):
        self.all_words = {}
        self.nb_of_documents = 0

    def clear_docs(self, array_of_documents: list, is_not_query=True) -> list():
        """
        :param array_of_documents - list of strings (docs:
        :param is_not_query - if its labeled data or new docs:
        :return clreaed data, separated words, low, withous , and . :
        """
        if is_not_query:
            self.nb_of_documents = len(array_of_documents)
            if len(array_of_documents) > 1:
                for index, dokument in enumerate(array_of_documents):
                    for p in [',', '.']:
                        dokument = dokument.replace(p, '')
                    array_of_documents[index] = dokument.lower().split()
            for dokument in array_of_documents:
                for word in set(dokument):
                    if word in self.all_words:
                        self.all_words[word] = self.all_words[word] + 1
                    else:
                        self.all_words[word] = 1
        else:
            for p in [',', '.']:
                array_of_documents = array_of_documents.replace(p, '')
            array_of_documents = array_of_documents.lower().split()
        return array_of_documents

    def TF(self, table_of_cleared_words: str) -> dict:
        counted_words_dict = dict(Counter(table_of_cleared_words))
        max_value = counted_words_dict[max(counted_words_dict, key=counted_words_dict.get)]
        counted_words_dict = {key: counted_words_dict[key] / max_value for key in counted_words_dict}
        return counted_words_dict

    def IDF(self) -> dict:
        idf_dict = self.all_words
        max_value_title = self.nb_of_documents
        counted_words_dict_title = {key: log10(max_value_title / idf_dict[key]) for key in idf_dict}
        return counted_words_dict_title

    def TF_IDF(self, TF_dict: dict, IDF_dict: dict) -> dict:
        # if query bring a new word, drop it
        keys_to_delate = []
        for key in TF_dict.keys():
            if key not in IDF_dict.keys():
                keys_to_delate.append(key)
        for key in keys_to_delate:
            TF_dict.pop(key)
        for key in IDF_dict.keys():
            if key in TF_dict.keys():
                TF_dict[key] = TF_dict[key] * IDF_dict[key]
            else:
                TF_dict[key] = 0
        return {k: v for k, v in sorted(TF_dict.items(), key=lambda x: x[0], reverse=True)}

    def euclidean_distance(self, x: list, y: list):
        measure = 0
        for x_value, y_value in zip(x, y):
            value = pow(x_value - y_value, 2)
            measure += sqrt(value)
        return measure


if __name__ == '__main__':

    # input data
    # 3
    # You care set up, do not pluck my care down.
    # My care is loss of care with old care done.
    # Your care is gain of care when new care is won.
    # 0 1 1
    # Care is loss when my gain is won git.
    # 1

    # entry data
    docs = []
    num_docs = int(input())
    for i in range(num_docs):
        doc = input()
        docs.append(doc)
    clas = input().split()
    clas = [int(i) for i in clas]
    query = input()
    k = int(input())

    # create tf_idf from labeled data
    knn = KNN_classifier()
    cleared_dosc = knn.clear_docs(docs)
    IDF = knn.IDF()
    docs_tf = []
    for cleared_doc in cleared_dosc:
        docs_tf.append(knn.TF(cleared_doc))
    docs_tfidf = []
    for doc_tf in docs_tf:
        docs_tfidf.append(knn.TF_IDF(doc_tf, IDF))

    # create TFIDF query
    query = knn.clear_docs(query, is_not_query=False)
    query_tf = knn.TF(query)
    query_tfidf = knn.TF_IDF(query_tf, IDF)

    # distance
    class_id_distance = []
    for clas_id, doc_tfidf in zip(clas, docs_tfidf):
        class_id_distance.append((clas_id, knn.euclidean_distance(query_tfidf.values(), doc_tfidf.values())))

    # find k nearest neighbour
    k_nearest_neghbour = [id for id, _ in sorted(class_id_distance, key=lambda x: x[1])[:k]]
    if sum(k_nearest_neghbour) / len(k_nearest_neghbour) != 0.5:
        print(int(sum(k_nearest_neghbour) / len(k_nearest_neghbour)))
    else:
        print(1)

# output data
# 1
