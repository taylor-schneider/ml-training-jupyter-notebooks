# Overview
Apache Spark is an open-source, distributed processing system used for big data workloads.

Spark is setup as a cluster based service which allows users to submit workloads to it through various language bindings. Users can submit code snippets to the cluster using Scala, Python, and R.

# 1. History
Originally developed at the University of California, Berkeley's AMPLab in 2009 under a BSD license, the Apache Spark codebase was later donated to the Apache Software Foundation in 2013 under the Apache 2.0 license. There have been several major iterations released with the most recent version being 3.1.

# 2. How It Works
Spark is setup as a master/slave pattern. In Spark terminology this is a Driver/Executor respectively. These components are Java programs. They can run locally or they can run on remote machines. In our case we will run these applciations as Kubernetes Pods which will be spun up automagically.

# 3. Relevant Notebooks
The following notebooks will get you up and running with Apache Spark.

Getting setup:

- [Install Apache Spark Prerequisites](Install%20Apache%20Spark%20Prerequisites.ipynb)

Hello, World! Examples:

- [Spark Pi - The Hello World Example For Apache spark](Spark%20Pi%20-%20The%20Hello%20World%20Example%20For%20Apache%20spark.ipynb)
- [Running Apache Spark Locally](Running%20Apache%20Spark%20Locally.ipynb)
- [Running Apache Spark On Kubernetes](Running%20Apache%20Spark%20On%20Kubernetes.ipynb)

Loading A CSV into a koalas dataframe:

- [Load CSV Into Apache Spark Locally](Load%20CSV%20Into%20Apache%20Spark%20Locally.ipynb)
- [Load CSV Into Apache Spark On Kubernetes](Load%20CSV%20Into%20Apache%20Spark%20On%20Kubernetes.ipynb)