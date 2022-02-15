class QLM():

    def __init__(self):
        self.words = []

    def clear_docs(self, array_of_documents: list, is_not_query=True) -> list():
        """
        :param array_of_documents - list of strings (docs:
        :param is_not_query - if its labeled data or new docs:
        :return clreaed data, separated words, low, withous , and . :
        """
        if is_not_query:
            for index, dokument in enumerate(array_of_documents):
                for p in [',', '.']:
                    dokument = dokument.replace(p, '')
                array_of_documents[index] = dokument.lower().split()
            for dokument in array_of_documents:
                for word in dokument:
                    self.words.append(word)
        else:
            for p in [',', '.']:
                array_of_documents = array_of_documents.replace(p, '')
            array_of_documents = array_of_documents.lower().split()

        return array_of_documents

    def QLM(self, documents: list, query: list) -> dict:
        smoothing_factor = 0.5
        prob = {}
        for doc_id, document in enumerate(documents):
            probability = 1
            for word in query:
                prob_document = document.count(word) / len(document)
                prob_all = self.words.count(word) / len(self.words)
                probability *= smoothing_factor * prob_document + (1 - smoothing_factor) * prob_all
            prob[doc_id] = probability
        return prob


if __name__ == '__main__':

    #     data
    # 3
    # Shipment of gold damaged in a fire.
    # Delivery of silver arrived in a silver truck.
    # Shipment of gold arrived in a truck.
    # gold silver trucK

    # entry data
    docs = []
    num_docs = int(input())
    for i in range(num_docs):
        doc = input()
        docs.append(doc)
    query = input()

    # cleaning data
    qlm = QLM()
    cleared_docs = qlm.clear_docs(docs)
    cleared_query = qlm.clear_docs(query, is_not_query=False)

    # segregation of documnets using QLM
    prob_qlm = qlm.QLM(cleared_docs, cleared_query)
    print([id for id, _ in sorted(prob_qlm.items(), key=lambda x: (x[1], x[0]), reverse=True)])

# output
# [1,2,0]
