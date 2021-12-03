# Hyperopt

In this directory we have notebooks which explore the fundamentals of hyperopt.

Recall that the purpose of hyperopt is to provide a data scientist with the optimal set of hyperparameters for a machine learning algorithm.

In order to find this optimal set of hyperparameters, hyperopt needs to search for them. For this purpose, hyperopt provides a [search space](Hyperopt%20Search%20Space.ipynb) object. As the name suggests, a search space. is a multi-dimensional space through which we will search for our optimal hyperparameter set.

Additionally, recall that hyperopt considers a model as a hyperparameter. As we know, a different models will accept different sets of different hyperparameters. Thus we will see both models and their coresponding hyperparameters appearing in our definitions of search spaces.

In addition to the search space, hyperopt needs a way to assess how "good" a set of parameters is. Is uses this measurement to compare sets of hyperparameters and ultimately choose the best set. This is commonly referred to as a "loss function". Hyperopt documentation refers to this as an [objective functions](Hyperopt%20Objective%20Functions.ipynb). Defining an objective function is outside the scope of these notbeooks but trivial examples are given.

And finally, hyperopt provides a collection of [search algorithms](Hyperopt%20Search%20Algorithms.ipynb) which defines how hyperopt searches through the search space while using the objective function.

# Implimentation

The hyperopt framework provides the mechanisms to define the search space, the search algorithm, and the objective function. At its core, Hyperopt provides the function *fmin()* for conducting searches. This function accepts a search space and search algorithm as a parameter and orchestrates the search.

```
best_hyper_parameters = fmin(
                            objective_function, 
                            search_space, 
                            search_algorithm, 
                            other_search_parameters)
```

It is recommended to review the foundational material in the following order:

- [Search Spaces](Hyperopt%20Search%20Space.ipynb)
- [Search Algorithms](Hyperopt%20Search%20Algorithms.ipynb)
- [Objective Functions](Hyperopt%20Objective%20Functions.ipynb)

Additionally, hyperopt has some integrations which are worth exploring:

- [Hyperopt Integration With Apache Spark](Hyperopt%20Spark%20Integration.ipynb)
- [Hyperopt Integration With MLFlow](Hyperopt%20MLFlow%20Integration.ipynb)

**Note**: There are some major changes/incompatabilities between versions of hyperopt. I have seen some angry notes in various points complaining about this. For the sake of avoiding this issue, take note that I am using the latest package versioned 0.2.5.