# DendriteClassificationWithAPI

The biological sciences are a prime hotspot for retrieving exorbitant amounts 
of data—ranging from physiological characteristics of large mammals (e.g., 
Whales, humans, etc.), down to nanoscale phenomena that can be measured. 

Here, I focus on bridging the gap between data acquired from 
neurobiological experimentation with modern, classification-techniques
currently used in data science—a field involved in extracting insight from 
structured and unstructured data. More specifically, I seek to answer the 
following question: “Is it feasible to classify whether a neuron has Aspiny or 
spiny dendrites given information about its firing properties?”

## Project Background:¶
Classification algorithms are a form of supervised learning. The main idea is train a classification model (i.e. generate a target function), that maps each instance of a feature set X to a class label y.

In my CS7180 course (Special topics in AI) we discussed two types of classification models--descriptive and predictive modeling.

Descriptive modeling serves as an tool to distinguish between objects of different classes by describing the features that make up an instance of a class.

Predictive modeling on the otherhand uses an instance of the features as input to predict the class label.

For the scope of this project, I will focus on predictive modeling for:

probablistic predictive classification model (i.e. Logistic Regression)
predictive classification model using the classification models discussed in class(e.g. KNN, Decision Tree, etc.)

## Flask Service:
To make this model usable on the web, I set up a simple swagger api specifiction found in swagger/dendrite_classification_api.yaml. I also exported the neuron classification model and wrapped it in a flask application found in ./dendrite_classification_api.py.