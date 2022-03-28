# Hyperopt

In this directory we have notebooks which explore the fundamentals of hyperopt.

Recall that the purpose of hyperopt is to provide a data scientist with the optimal set of hyperparameters for a machine learning algorithm.

In order to find this optimal set of hyperparameters, Hyperopt needs to search for them. For this purpose, hyperopt provides a [Search Space](Hyperopt%20Search%20Space.ipynb) object. As the name suggests, a Search Space. is a multi-dimensional space through which we will search for our optimal hyperparameter set.

Additionally, recall that hyperopt considers a model as a hyperparameter. As we know, a different models will accept different sets of different hyperparameters. Thus we will see both models and their coresponding hyperparameters appearing in our definitions of search spaces.

Hyperopt provides a mechanism for keeping track of the search process. The [Trials](Hyperopt%20Search%20Space.ipynb) object allows users to understand the path Hyperopt has taken to derive the optimal parameters. The path is represented as an ordered list of Trials. A user can analyze The Trials object to derive the hyperparameters and correcponsing scores from the Objective Function for each Trial.

In addition to the Search Space, hyperopt needs a way to assess how "good" a set of parameters is. Is uses this measurement to compare sets of hyperparameters and ultimately choose the best set. This is commonly referred to as a "loss function". Hyperopt documentation refers to this as an [Objective Functions](Hyperopt%20Objective%20Functions.ipynb). Defining an objective function is outside the scope of these notbeooks but trivial examples are given.

And finally, hyperopt provides a collection of [Search Algorithms](Hyperopt%20Search%20Algorithms.ipynb) which defines how hyperopt searches through the search space while using the objective function.

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
- [Trials](Hyperopt%20Trials.ipynb)

Additionally, hyperopt has some integrations which are worth exploring:

- [Hyperopt Integration With Apache Spark](Hyperopt%20Spark%20Integration.ipynb)
- [Hyperopt Integration With MLFlow](Hyperopt%20MLFlow%20Integration.ipynb)

# Important Note On Hyperopt Versioning
**Note**: There are some major changes/incompatabilities between versions of hyperopt. I have seen some angry notes in various points complaining about this. I have also experienced som undocumented breaking changes hen switching between 0.2.5 and 0.2.7. For the sake of avoiding this issue, take note that I am using the latest package versioned 0.2.7.