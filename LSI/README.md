# LSI

Latent Semantic Indexing (LSI) dzieli się na:
* Latent Semantic Analysis ([LSA](http://www.scholarpedia.org/article/Latent_semantic_analysis)) - Latent Semantic Analysis  models the contribution to natural language attributable to combination of words into coherent passages. It uses a long-known matrix-algebra method, Singular Value Decomposition (SVD), which became practical for application to such complex phenomena only after the advent of powerful digital computing machines and algorithms to exploit them in the late 1980s. To construct a semantic space for a language, LSA first casts a large representative text corpus into a rectangular matrix of words by coherent passages, each cell containing a transform of the number of times that a given word appears in a given passage. The matrix is then decomposed in such a way that every passage is represented as a vector whose value is the sum of vectors standing for its component words. Similarities between words and words, passages and words, and of passages to passages are then computed as dot products, cosines or other vector-algebraic metrics. (For word and passage in the above, any objects that can be considered parts that add to form a larger object may be substituted.)
* latent Dirichlet allocation ([LDiA](https://par.nsf.gov/servlets/purl/10055536)) -topic modeling grew from LSA in several directions. Inputs to methods typically include a word-document matrix that records the number of times a particular word is included in one document. Early researchers applied conventional clustering methods, such as k-means clustering, and dimensional reduction methods, such as Principle Component Analysis (PCA), but these methods had limited success. Clustering methods were too rigid and dimensionality reduction methods often yielded results that were difficult to interpret. In the early 2000’s, a different approach called Latent Dirichlet Allocation (LDA) was developed, where the basic idea is “that documents are represented as random mixtures over latent topics, where each topic is characterized by a distribution over words." 


## Reading

Input:
* number of documents (𝑛)
* 𝑛 lines with documents.
* lines with a query
* number of dimensions after reduction (𝑘)
    

## Processing

The documents were cleaned up first:
* reducing letters 
* removing punctuation
* splitting sentences into word array

Unique words were extracted and used to create a word-document matrix, if a word was present in a document 1, if not 0.
The SVD method was used to reduce the dimension of the data to 2. The resulting matrix was used to calculate the distance (cosine similarity) between the search phrase relative to the documents
  

## Method

### SVD
In linear algebra, the Singular Value Decomposition (SVD) of a matrix is a factorization of that matrix into three matrices. It has some interesting algebraic properties and conveys important geometrical and theoretical insights about linear transformations. 

I will not describe here the whole course of SVD activities, please refer to [link](https://towardsdatascience.com/understanding-singular-value-decomposition-and-its-application-in-data-science-388a54be95d). 
The main idea of the algorithm is shown on the graphic below.


![SVD](https://www.researchgate.net/publication/323907837/figure/fig2/AS:606612796473344@1521639169497/Schematic-representation-for-singular-value-decomposition-SVD-analysis.png)

###cos similarity

![cos](https://miro.medium.com/max/1400/1*LfW66-WsYkFqWc4XYJbEJg.png)

## Output

* list with 𝑛 query similarity values for each 𝑛 document








