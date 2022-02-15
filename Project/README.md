# Classification based on TF-IDF measure

This project is intended to illustrate the possibility of classification using the
TF-IDF measure. 

## Problem

The problem may seem trivial, after all, you can extract a few patterns and 
classify the data based on the regex, without having to build a model.
Unfortunately, the publications have many different patterns, which are 
impossible to catch using regexp.  This is caused by the fact that they are added 
manually on a site by officials, who have different patterns in providing 
information. 

## Data (Input)

The input data was taken from the website [companyhouse](https://www.companyhouse.de/), 
with obvious permission. However, due to legal considerations, 
the dataset was not added to the project 

The collection contains two columns ,,text" and ,,label". As the names imply, 
"text" is responsible for the content of the publication and 
"label"is responsible for its labeling.

* Publications are information provided by German companies relating to changes 
  in their company: change of address, name, directors, etc.
* Label is data that has been manually marked.

Data is also publicly available in company registers such as 
[unternehmensregister](https://www.unternehmensregister.de/ureg/).
They can be downloaded with the scraper .

## Methods

The TF-IDF method was used, which can be consulted [here](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.121.1424&rep=rep1&type=pdf) as well as in [this repository](https://github.com/whyme36/NLP/tree/master/TF_IDF).

Classification methods:
* [Logistic Regression](https://www.researchgate.net/publication/242579096_An_Introduction_to_Logistic_Regression_Analysis_and_Reporting)
* [Naive Bayes Classifier](https://arxiv.org/abs/1404.0933).
* [SVM](https://www.researchgate.net/publication/221621494_Support_Vector_Machines_Theory_and_Applications)
* [RANDOM FORESTS](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf)
* [XGboost](https://arxiv.org/abs/1603.02754)

And a framework for creating interactive visualizations [dash](https://dash.plotly.com/introduction)

## Proces

### Preprocessing
Data preprocessing can be found in the file Classificators.ipynb
* getting rid of punctuation (re),
* lemmatization (simplemma),
* get rid of stop words (nltk),
* reducing all letters.

### Create Classifiers
The classifiers were created on default parameters, the goal of the project was not to get the best classifier, which could of course be done. However, the trained classifiers also produced satisfactory results.
The trained classifiers can be found in the file  Classificators.ipynb
* LR, NB, SVM, RF (sklearn)
* XGBoost (xgboost)

### Dash processing
A separate file was created to parse the publication text provided by the user and to load the learned models: preparator_text_and_classifier.py

Which supports web-based interactive visualization in the file: dash_interface.py


## Output

Classifying text as: 
* Change of address was detected by the model NAME_OF_MODEL
* No change of address detected by the model NAME_OF_MODEL










