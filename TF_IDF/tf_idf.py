from collections import Counter
from math import log10
class TF_IDF:
    def __init__(self):
        self.all_title={}
        self.all_content={}
        self.nb_of_documents=0
        self.nb_of_dokument=0
        self.array_of_looking_words=[]
    """ Reads title, content and looking words, line by line (first line count of doc, title-content,next value of searching words, and this words)"""
    def read_data(self,file_name:str):
        with open(file_name,'r',encoding='utf-8') as plik:
            calyplik=plik.read().splitlines()

        self.nb_of_documents=int(calyplik[0])
        dokumenty=calyplik[1:self.nb_of_documents*2+1]
        words_to_search=calyplik[self.nb_of_documents*2+2:]
        tytuly=[]
        tresci=[]
        words=[]
        for index,element in enumerate(dokumenty):
            if index%2==0:
                tytuly.append(element)
            else:
                tresci.append(element)
        for word in words_to_search:
            words.append(word)
        return tytuly,tresci,words
    """ Reduces letters and removes word endings  """
    def clear_words(self,phrase:str,file_name:str,title_content:int):
        """
        :phrase - its string to clear :
        :file_name - it's prepared to file diffs.txt:
        :title_content if its title then 0, content 1:
        :return:
        """
        for p in [',', '.']:
            phrase = phrase.replace(p, '')
        phrase=phrase.lower().split()

        lemat = {}
        with open(file_name, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.split()
                lemat.update({line[0]: line[1]})
        output = [lemat[word] if word in lemat else word for word in phrase]
        # add to the global variable, all words form phrases
        if title_content==0:
            for word in set(output):
                if word in self.all_title:
                    self.all_title[word]=self.all_title[word]+1
                else:
                    self.all_title[word] = 1
        elif title_content==1:
            for word in set(output):
                if word in self.all_content:
                    self.all_content[word]=self.all_content[word]+1
                else:
                    self.all_content[word] = 1

        return output
    """ tf= the number of occurrences of a term divided by the number of highest occurrences of the term in the sentence (ti/max(ti))"""
    def TF(self,table_of_cleared_words:str):
        counted_words_dict=dict(Counter(table_of_cleared_words))
        max_value=counted_words_dict[max(counted_words_dict, key=counted_words_dict.get)]
        counted_words_dict = {key: counted_words_dict[key] / max_value for key in counted_words_dict}

        return counted_words_dict
    """ idf= calculates the logarithm of 10 of the number of most frequently used words in documents by the number of occurrences of the word in the given documents (lgm(max(nt)/nt)"""
    def IDF(self,title_content:int):
        if title_content==0:
            idf_dict=self.all_title
        else:
            idf_dict=self.all_content
        max_value_title = self.nb_of_documents
        counted_words_dict_title = {key: log10(max_value_title/idf_dict[key]) for key in idf_dict}
        return counted_words_dict_title
    """ TF_IDF = multiplication TF and IDF"""
    def TF_IDF(self,TF_dict:str,IDF_dict:dict):
        for key in TF_dict.keys():
                TF_dict[key] = TF_dict[key] * IDF_dict[key]

        return TF_dict
    """ function name says what it does"""
    def merge_two_dicts_and_sort(self,dict_one:dict,dict_two:dict):
        dict_one_counter = Counter(dict_one)
        dict_two_counter = Counter(dict_two)

        add_dict = dict_one_counter + dict_two_counter
        dict_output = dict(add_dict)
        #due to dissapearing words as "care" (words with 0 value), this code restore this words
        for word_one in dict_one.keys():
            if word_one not in dict_output.keys():
                dict_output[word_one] = 0.0
        for word_two in dict_two.keys():
            if word_two not in dict_output.keys():
                dict_output[word_two]=0.0
        return {key:dict_output[key] for key in sorted(dict_output, key=dict_output.get, reverse=True)}
    """ return array of looking words form docs"""
    def search_for_words(self,dict_merged:dict,array_of_words:list[str]):
        words_already_searched=[]
        for word in array_of_words:
            word = word.lower()
            clered_words = self.clear_words(phrase=word, file_name='diffs.txt', title_content=2)
            if len(word.split(' '))>1:
                for word_one in clered_words:
                    if word_one in dict_merged and word_one not in words_already_searched:
                        self.array_of_looking_words.append((self.nb_of_dokument, word_one, dict_merged[word_one]))
                        words_already_searched.append(word_one)
            else:
                if clered_words[0] in dict_merged and clered_words[0] not in words_already_searched:
                    self.array_of_looking_words.append((self.nb_of_dokument,clered_words[0],dict_merged[clered_words[0]]))
                    words_already_searched.append(word)
        self.nb_of_dokument+=1
        return self.array_of_looking_words
if __name__ == '__main__':
    array_TF_titles=[]
    array_TF_contents = []
    # start class and read data
    tf_idf=TF_IDF()
    titles,contents,words=tf_idf.read_data('input.txt')
    # implementation  of TF measure for each title and content
    for content,title in zip(contents,titles):
        clered_content=tf_idf.clear_words(phrase=content, file_name='diffs.txt', title_content=1)
        clered_title=tf_idf.clear_words(phrase=title, file_name='diffs.txt', title_content=0)
        array_TF_contents.append( tf_idf.TF(clered_content))
        array_TF_titles.append(tf_idf.TF(clered_title))
    # implementation  of IDF measure for all titles and content
    IDF_content=tf_idf.IDF(title_content=1)
    IDF_title = tf_idf.IDF(title_content=0)


    # implementation  of TF_IDF measure and marge results (title and its content). Search words
    index_word_value = []
    for content_dict,title_dict in zip(array_TF_contents,array_TF_titles):
        TF_IDF_dict_title=tf_idf.TF_IDF(TF_dict=title_dict, IDF_dict=IDF_title)
        for key in TF_IDF_dict_title:
            TF_IDF_dict_title[key] *= 2
        TF_IDF_dict_content=tf_idf.TF_IDF(TF_dict=content_dict, IDF_dict=IDF_content)
        merged_values=tf_idf.merge_two_dicts_and_sort(TF_IDF_dict_title, TF_IDF_dict_content)
        index_word_value=tf_idf.search_for_words(merged_values, words)
    # for every looking words write array of sorted index (biggest value first)
    for word in words:
        word.lower()
        clered_words = tf_idf.clear_words(phrase=word, file_name='diffs.txt', title_content=2)
        # [(0, 'care', 0.3521825181113625), (1, 'care', 0.0), (2, 'care', 0.3521825181113625), (2, 'gain', 1.1132829276792124), (1, 'is', 1.0129395957912186), (2, 'is', 0.11739417270378749)]
        #if we are looking for more than 1 word
        if len(word.split(' '))>1:
            specific_words=[]
            for word_one in clered_words:
                array_for_specific_word = [tuple for tuple in index_word_value if tuple[1] == word_one]
                for i in array_for_specific_word:
                    specific_words.append(i)
            output={}
            for index, _, value in specific_words:
                if not index in output:
                    output[index] = value
                else:
                    output[index] = (output[index] + value)
            print( output)
            print([k for k, v in sorted(output.items(), key=lambda item: item[1], reverse=True)])

        #[[0, 'care', 0.3521825181113625], [1, 'care', 0.0], [1, 'is', 1.0129395957912186], [2, 'care', 0.3521825181113625], [2, 'is', 0.11739417270378749]]
        #if we looking just one word
        else:
            array_for_specific_word=[tuple for tuple in index_word_value if tuple[1] == clered_words[0]]
            array_for_specific_word.sort(key=lambda x:x[2],reverse=True)
            print(array_for_specific_word)
            print([index for index,_,_  in array_for_specific_word])

