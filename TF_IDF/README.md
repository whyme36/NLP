# TF_IDF
one of the methods for calculating word weights based on the number of occurrences of words, belonging to the group of algorithms that calculate statistical term weights. Each document is represented by a vector, consisting of weights of words occurring in that document. TFIDF reports the frequency of occurrences of a term while taking into account the appropriate balance between the local meaning of the term and its importance in the context of the full collection of documents.


## Reading
The code in the repository is to process the data in the file: **input.txt**.

The first line gives the number of "documents" to process,
the document consists of two lines: the first is responsible for the title, the second for the content.
Last lines is for serching words (nb of words and that words)

## Processing
The process of processing of the document is to unify the character of the test: 
* titles as well as text are divided into words, 
* letters in words are changed to lowercase,
* words are lemmatized (**diffs.txt**).

## Method
The assignment of weights to words is based on the tf idf method.

term frequency - tft,d, the number of occurrences of term t in document d, normalized to avoid favoring long documents.

inverted document frequency - indicates the ratio of the number of all documents in the corpus (N) to the number of documents in which term t appears (Nt).

TF IDF for titles and content is combined at the very end, where titles are multiplied by a weight of 2.
## Output

The output is an array of "document" indexes, for each search word. The indexes are sorted by the value of word in the "document" (TF-IDF).



