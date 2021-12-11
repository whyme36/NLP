# Similarity

Class assignment, use probability measures between the texts: product, dice, jaccard and cosine

## Reading

Reading a file:
* number of documents (n),
* n lines with documents,
* a line with a query.


## Processing

The loaded documents have been cleaned up: the letters have been reduced, the periods and commas have been discarded, and the documents have been written to an array.

## Method

TF-IDF measure was used to calculate the word weights of the documents. Words with a weight of 0 that were not in the document but were found in the other documents were also added.

The document dictionaries thus obtained, were compared to the query by calculating the distance measures.
## Output

n lines, in each a list with the measures: product, Dice, Jaccard and cosine, for the given document.



