# K Nearest Neighbors

K Nearest Neighbour is a simple algorithm that stores all the available cases and classifies the new data or case based on a similarity measure. It is mostly used to classifies a data point based on how its neighbours are classified.

![KNN](https://miro.medium.com/max/1300/1*9HZkibzNcY_IvBO5O6Fo4g.png)

## Reading

Input: 
* number of documents from the training set (N)
* N training documents (1 per line)
* a line of ones and zeros indicating whether the i-th document has been classified in class cj (1) or not (0)
* document to be classified
* a number of k nearest neighbors based on which
decision is made
  
## Processing
First, assign the appropriate TF-IDF weights to the words in the documents and the query, and expand the document to include words that were included in the corpus but are not present in the document and assign them weights of 0

Then calculate the distance between the query and all documents in the collection.  I used the Euclidean distance.


Finally, the number of neighbors given by the user is selected and the class membership is calculated (if a tie, the query belongs to class 1)

## Output

Output:
* 0 or 1 - indicating the result of document classification







