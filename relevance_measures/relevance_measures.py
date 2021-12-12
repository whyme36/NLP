# input
# 2
# 4 5 2 1 3
# 6 5 0 4 3 8
# 1 1 1 1 1 0 0 0 0

import numpy as np
class Solution:
    """
    Class task
    The assignment was to investigate the relevancy of documents.
    The program should take the number of searches, then searches in which document numbers are given,
    and finally document relevancy. The program calculates the relevancy of documents by using measures such as:
    * precision
    * relative recall
    * f_socre
    * mean_average_precision
    which are displayed in a list for each search.
    """

    def __init__(self):
        self.all_dokuments={}
    def prepare_relevant_dict(self,data) -> dict:
        d = {}
        for index, is_relevant in enumerate(data.split(' ')):
            d[index] = int(is_relevant)
        return d
    def prepare_documents_dict(self,data,relevant) -> dict:
        d={}
        for document in data.split(' '):
            d[int(document)]=relevant[int(document)]
            self.all_dokuments[int(document)]=relevant[int(document)]
        return d
    def precision(self,dict) ->int:
        return round(sum(dict.values())/len(dict.values()),2)
    def relative_recall(self,dict) -> int:
        return round(sum(dict.values())/sum(self.all_dokuments.values()),2)
    # i am not gonna use that func
    # def fall_out(self,dict,relevant) ->int:
    #     n_zeros_relevant = len([i for i in relevant.values() if i==0])
    #     n_zeros_dict = len([i for i in dict.values() if i == 0])
    #     return round(n_zeros_dict/n_zeros_relevant,2)
    def f_socre(self,precision,recall,n) -> int:
        return round(((1+n)*precision*recall)/(n*precision+recall),2)
    def precision_j(self,dict) ->list():
        arr={}
        output=[]
        for doc_index,relavant in dict.items():
            if arr=={}:
                arr[doc_index]=relavant
            else:
                output.append((sum(arr.values())/len(arr)))
                arr[doc_index] = relavant
                # print(arr)
        output.append((sum(arr.values()) / len(arr)))
        return output
    def mean_average_precision(self,dict) -> int:
        precision_j=self.precision_j(dict)
        numerator =sum([precision*value for precision,value in zip(precision_j,dict.values())])
        denominator=sum(self.all_dokuments.values())
        return round(numerator/denominator,2)
if __name__ == '__main__':
    # n = 2
    # x = ['4 5 2 1 3', '6 5 0 4 3 8']
    # relevant = '1 1 1 1 1 0 0 0 0'

    search_dokuments=[]
    n=int(input())
    while n>0:
        docs=input()
        search_dokuments.append(docs)
        n-=1
    relevant=input()


    s=Solution()
    relevant=s.prepare_relevant_dict(relevant)
    # print(relevant)
    docuements_inquiries=[]
    for docuement in search_dokuments:
        docuements_inquiries.append( s.prepare_documents_dict(docuement,relevant) )
    # print(docuements)
    for dokuments in docuements_inquiries:
        precision=s.precision(dokuments)
        relative_recall = s.relative_recall(dokuments)
        f_score=s.f_socre(precision,relative_recall,2)
        mean_average_precision = s.mean_average_precision(dokuments)
        # print()
        # print(dokument)
        # print(s.precision_j(dokument))
        print([precision,relative_recall,f_score,mean_average_precision])

#output
# [precision,relative_recall,f_score,mean_average_precision]
# [0.8, 0.8, 0.8, 0.64]
# [0.5, 0.6, 0.56, 0.29]