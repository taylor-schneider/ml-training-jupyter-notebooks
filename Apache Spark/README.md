# Overview
Apache Spark is an open-source, distributed processing system used for big data workloads.

Spark is setup as a cluster based service which allows users to submit workloads to it through various language bindings. Users can submit code snippets to the cluster using Scala, Python, and R.

# 1. History
Originally developed at the University of California, Berkeley's AMPLab in 2009 under a BSD license, the Apache Spark codebase was later donated to the Apache Software Foundation in 2013 under the Apache 2.0 license. There have been several major iterations released with the most recent version being 3.1.

# 2. How It Works
Spark is setup as a master/slave pattern. In Spark terminology this is a Driver/Executor respectively. These components are Java programs. They can run locally or they can run on remote machines. In our case we will run these applciations as Kubernetes Pods which will be spun up automagically.

# 3. Relevant Notebooks
The following notebooks will get you up and running with Apache Spark.

### Getting setup:
In these notebooks we explore the steps to get Apache Spark up and running.

- [Install Apache Spark Prerequisites](Install%20Apache%20Spark%20Prerequisites.ipynb)
- [Create A SparkContext For Locally Hosted Cluster](Create%20A%20parkContext%20For%20Locally%20Hosted%20Cluster.ipynb)
- [Create A SparkContext For Kubernetes Hosted Cluster](Create%20A%20SparkContext%20For%20Kubernetes%20Hosted%20Cluster.ipynb)

### Hello, World! Examples:
Here we look at the basic hello worl example.

- [Spark Pi - The Hello World Example For Apache spark](Spark%20Pi%20-%20The%20Hello%20World%20Example%20For%20Apache%20spark.ipynb)
- [Running Apache Spark Locally](Running%20Apache%20Spark%20Locally.ipynb)
- [Running Apache Spark On Kubernetes](Running%20Apache%20Spark%20On%20Kubernetes.ipynb)

### Manipulating data on Apache Spark Cluster:
In this series we look at how a user can interact and manipulate data in Apache Spark using techniques familiar to those using simpler python libraries like numpy and pandas.

- [Intro To Koalas][Intro%20To%20Koalas.ipynb]
- [Load CSV Into Apache Spark Locally](Load%20CSV%20Into%20Apache%20Spark%20Locally.ipynb)
- [Load CSV Into Apache Spark On Kubernetes](Load%20CSV%20Into%20Apache%20Spark%20On%20Kubernetes.ipynb)