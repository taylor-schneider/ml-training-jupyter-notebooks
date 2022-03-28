# Overview

As the name suggests, Hyperparameter optimization (sometimes called hyperparameter tuning) is the process of tuning a set of hyperparameters. In other words is we want to find the optimal set of hyperparameters which yield the most accurate and/or precise model. Thus HPO is an [optimization](../../Data%20Science/Optimization/README.md) problem and employs many of the of the classical optimization techniques. Additionally, optimization techniques have been born specifically to handle the hyperparameter use case.

# The Difference Between Model Parameters and Hyperparameters

Recall that a machine learning model or algorithm is a mathematical equation or algorithm which is trained to fit a data set so that we can make predictions for data points which have not been observer. 

In the process of training a model, the **model parameters** are derived. Model parameters effectively tell the equation/algorithm how to fit the provided data set. For example the weights of a regression or deep neural network. 

**Model hyperparameters** on the other hand, are the parameters that define how the algorithm arrives at a given fit. Effectively they are used to estimate the model parameters. These parameters cannot be estimated by the model from the given data. For example, the k in the k-nearest neighbors algorithm or the learning rate in deep neural networks.

# HPO Algorithms
As HPO is an application of optimization there are a number of algorithms and techniques available for selecting the optimal set of hyperparameters.

An overview of these algorithms can be found [here](https://neptune.ai/blog/hyperparameter-tuning-in-python-a-complete-guide-2020) or [here](https://arxiv.org/pdf/2101.02289.pdf)

# Tooling
Some of the hyperparameter tuning libraries I have come accross include:

- Scikit-learn (grid search, random search)
- [Hyperopt](Hyperopt/README.md)
- Scikit-Optimize
- Optuna
- Ray.tune

We will explore some of these tools in their own notebooks.
