from math import log10
# input
# 3
# Your care set up, do not pluck my care down.
# My care is loss of care with old care done.
# Your care is gain of care when new care is won.
# care loss
# 0 1 1
# 6
# Somewhere in Poland
# City in the western Poland in the Greater Poland region.
# You can see the Polish city, in the western part.
# Capital in Poland
# Here is the capital and largest city of Poland.
# I can't beleive that I see a western city in Poland, in the Greater Poland region.
# western city in Poland
# 0 1 1 0 0 1
class Solution():
    def __init__(self):
        self.dic_relevant=[]
        self.relevant_document=0
        self.all_document=0
    def add(self,relevant):
        relevation_map = {}
        for doc_index, relevation in enumerate(relevant.split()):
            relevation_map[doc_index] = relevation
        self.dic_relevant = relevation_map
        self.relevant_document = len([x for x in relevant.split() if x == '1'])  # S
        self.all_document = len(relevant.split())  # N
    def clear_docs(self,array_of_documents:list) -> list():
        for index,dokument in enumerate(array_of_documents):
            for p in [',', '.']:
                dokument = dokument.replace(p, '')
            array_of_documents[index] = dokument.lower().split()
        return array_of_documents
    #how many documents have word:
    def how_many_doc_have_word(self,array_of_cleared_documents:list(),word:str) -> int: #df_{i}
        doc_count=0
        for dokument in array_of_cleared_documents:
            if word in dokument:
                doc_count+=1
        return doc_count
    #how many relevant documents have word:
    def how_many_relevant_doc_have_word(self,array_of_cleared_documents:list(),word:str) -> int: #s
        doc_count=0
        for doc_index,dokument in enumerate(array_of_cleared_documents):
            if word in dokument and self.dic_relevant[doc_index]=='1':
                doc_count+=1
        return doc_count
    # probabilistic measure
    def p_n_c(self,array_of_cleared_documents,word:str) -> int:
        S=self.relevant_document
        N=self.all_document
        s=self.how_many_relevant_doc_have_word(array_of_cleared_documents, word)
        df_i=self.how_many_doc_have_word(array_of_cleared_documents, word)
        # p = s/S
        # n =(df_i-s)/(N-S)

        c=log10(((s+0.5)/(S-s+0.5))/((df_i-s+0.5)/(N-df_i-S+s+0.5)))

        return c

if __name__ == '__main__':

    #data
    docs = []
    how_many_dosc=int(input())
    for i in range(how_many_dosc):
        doc = input()
        docs.append(doc)
    query=input()
    relevantion=input()
    # clear data and start class
    s=Solution()
    s.add(relevantion)
    docs_cleared=s.clear_docs(docs)

    #count score of words in query
    c_score={}

    query=query.lower().split()
    for word in query:
        c_score[word]= s.p_n_c(docs_cleared,word)
    # count probabilistic of documents
    output={}
    for index,doc in enumerate(docs_cleared):
        for word in c_score.keys():
            if word in doc and index in output.keys():
                output[index] +=c_score[word]
            elif word in doc and not index in output.keys():
                output[index] = c_score[word]
    # print
    print(docs_cleared)
    print([round(value,2) for value in output.values()])
#output
#[0.22, 0.7, 0.22]
# [0.0, 2.76, 3.38, 0.0, 0.44, 2.76]



