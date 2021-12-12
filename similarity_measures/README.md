# Similarity

Class task, use the probability measures between the texts: product, cube, Jaccard and cosine

## Reading

Reading a file:
* number of documents (n),
* n lines with documents,
* line with query.


## Processing

The read documents were cleaned: letters were shrunk, periods and commas were removed, and documents were saved to an array.

## Method

The TF-IDF measure was used to calculate the weights of the words in the documents. Words with a weight of 0 that were not present in a document but were present in other documents were also added. Words from the query were given a weight of 1, this was imposed by the task content.

The resulting document dictionaries were compared to the query by calculating the distance measures.
## Output

n rows, and in each row a list of measures: product, Dice, Jaccard, and cosine for the given document.

