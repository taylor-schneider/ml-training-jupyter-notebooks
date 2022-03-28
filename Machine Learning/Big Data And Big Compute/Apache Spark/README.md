# Overview
Apache Spark is an open-source, unified, and distributed, analytics engine for large-scale data processing. It is architected as a cluster based service. Using high-level APIs provided in Java, Scala, Python and R, and an optimized engine that supports general execution graphs, users can sumbit worloads to the cluster. It also supports a rich set of higher-level tools including Spark SQL for SQL and structured data processing, MLlib for machine learning, GraphX for graph processing, and Structured Streaming for incremental computation and stream processing.

# 1. History
Originally developed at the University of California, Berkeley's AMPLab in 2009 under a BSD license, the Apache Spark codebase was later donated to the Apache Software Foundation in 2013 under the Apache 2.0 license. There have been several major iterations released with the most recent version being 3.1.

# 2. How It Works
Spark is setup as a master/slave pattern. In Spark terminology this is a Driver/Executor respectively. These components are Java programs. They can run locally or they can run on remote machines. In our case we will run these applciations as Kubernetes Pods which will be spun up automagically.

To understand more about what Spark can do and how it works see this [Overview Notebook](Overview%20Apache%20Spark.ipynb)

To understand how spark is deployed on kubernetes we can see this [Overview Notebook](Overview%20Running%20Apache%20Spark%20On%20Kubernetes.ipynb)

# 3. Hands-On-Keyboard
The following notebooks will get you up and running with Apache Spark. 

Before we begin, I cannot stress this enough: kubernetes is very sensitive to version information. We are running v1.21.9.

## 3.1. Getting setup:
In these notebooks we explore the steps to get Apache Spark up and running.

- [Install Apache Spark Prerequisites](Install%20Apache%20Spark%20Prerequisites.ipynb)
- [Create A SparkContext For Locally Hosted Cluster](Create%20A%20SparkContext%20For%20Locally%20Hosted%20Cluster.ipynb)
- [Create A SparkContext For Kubernetes Hosted Cluster](Create%20A%20SparkContext%20For%20Kubernetes%20Hosted%20Cluster.ipynb)

## 3.2. Hello, World! Examples:
Here we look at the basic hello worl example.

- [Spark Pi - The Hello World Example For Apache spark](Spark%20Pi%20-%20The%20Hello%20World%20Example%20For%20Apache%20spark.ipynb)
- [Running Scikit-Learn On Apache Spark](Running%20Scikit-Learn%20Apache%20Spark.ipynb)
- [Running MLib Algorithms On Apache Spark](Running%20MLib%20Algorithms%20%28k-means%29.ipynb)

## 3.3. Manipulating data on Apache Spark Cluster:
In this series we look at how a user can interact and manipulate data in Apache Spark using techniques familiar to those using simpler python libraries like numpy and pandas.

- [Intro To Koalas](Intro%20To%20Koalas.ipynb)
- [Load CSV Into Apache Spark Locally](Load%20CSV%20Into%20Apache%20Spark%20Locally.ipynb)
- [Load CSV Into Apache Spark On Kubernetes](Load%20CSV%20Into%20Apache%20Spark%20On%20Kubernetes.ipynb)

Note: In the notebooke about loading a CSV on spark running on kubernetes we also look at adding code files to the cluster. This is helpful in some more advanced cases.

## 3.4. Parallelization