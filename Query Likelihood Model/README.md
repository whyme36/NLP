# Query Likelihood Model

The query likelihood model is a language model used in information retrieval. A language model is constructed for each document in the collection. It is then possible to rank each document by the probability of specific documents given a query. This is interpreted as being the likelihood of a document being relevant given a query ([Wiki](https://en.wikipedia.org/wiki/Query_likelihood_model)).
## Reading
Input: 
* number of documents to process (n)
* n lines with documents
* query q
## Processing

Cleansing data by removing punctuation and lowering the letters.

Using QLM, to examine the relevance of the dokuments.

## Output
Output:
* list of document indexes sorted in descending order
according to the probability of generating query q







