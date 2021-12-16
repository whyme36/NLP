import numpy as np
from math import sqrt

class LSI_SVD_cosine_similarity:
    def clear_docs(self,array_of_documents: list) -> list():
        """
        :param array_of_documents - take array of array of words:
        :return array of array of cleared words:
        """
        for index, dokument in enumerate(array_of_documents):
            for p in [',', '.']:
                dokument = dokument.replace(p, '')
            array_of_documents[index] = dokument.lower().split()
        return array_of_documents
    def get_set(self,array_of_arrays):
        """
        :param array_of_arrays - take array of array of words:
        :return - set of words:
        """
        output=[]
        for array in array_of_arrays:
            for word in array:
                output.append(word)

        return sorted(set(output))
    def make_matrix(self,docs,set, is_query=False):
        """
        :param docs - array of array of words or query:
        :param set - all words in docs:
        :param is_query - bool True for query:
        :return:
        """
        if is_query:
            output=[]
            for word in set:
                if word in docs:
                    output.append(1)
                else:
                    output.append(0)
        else:
            output=[[] for i in range(len(docs))]
            for index,doc in enumerate(docs):
                for word in set:
                    if word in doc:
                        output[index].append(1)
                    else:
                        output[index].append(0)
        return output
    def svd_reduce_to_k_dim(self,matrix,k):
        """
        :param matrix - numpy array:
        :param k - num of dimention:
        :return:
        """
        U, s, Vt = np.linalg.svd(matrix, full_matrices=False)
        U = U[:, :k]
        s = np.diag(s)
        s = s[:k, :k]
        Vt = Vt[:k, :]
        return U.dot(s.dot(Vt))
    def cosine_similarity(self,v1, v2):
        "compute cosine similarity of 2 vectors "
        numerator, denominator_1, denominator_2 = 0, 0, 0
        for i in range(len(v1)):
            x = v1[i];
            y = v2[i]
            denominator_1 += x ** 2
            denominator_2 += y ** 2
            numerator += x * y
        return round(numerator / (sqrt(denominator_1) * sqrt(denominator_2)), 2)
if __name__ == '__main__':

    # read data
    lsi=LSI_SVD_cosine_similarity()
    num_dosc=int(input())
    docs = []
    for _ in range(num_dosc):
        doc=input()
        docs.append(doc)
    query= input()
    num_dim = int(input())

    #preprocessing
    cleared_docs=lsi.clear_docs(docs)
    # print(cleared_docs)
    set=lsi.get_set(cleared_docs)
    # print(set)
    docs=lsi.make_matrix(cleared_docs,set)
    # print(docs)
    query=query.lower().split()
    vector=lsi.make_matrix(query,set,is_query=True)
    # print(vector)
    docs.append(vector)
    docs=np.array(docs)
    # print(docs)

    #svd
    docs=lsi.svd_reduce_to_k_dim(docs,2)
    # print(docs)

    #cos similarity
    output=[]
    for doc in docs[:-1]:
        output.append(lsi.cosine_similarity(doc,docs[-1:][0]))
    print(output)

# input
# 3
# Shipment of gold damaged in a fire.
# Delivery of silver arrived in a silver truck.
# Shipment of gold arrived in a truck.
# gold silver truck
# 2
# Output
# [0.23, 0.98 0.72]







