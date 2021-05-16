# Overview
Apache Spark is an open-source, distributed processing system used for big data workloads.

Spark is setup as a cluster based service which allows users to submit workloads to it through various language bindings. Users can submit code snippets to the cluster using Scala, Python, and R.

# 1. History
Originally developed at the University of California, Berkeley's AMPLab in 2009 under a BSD license, the Spark codebase was later donated to the Apache Software Foundation in 2013 under the Apache 2.0 license. There have been several major iterations released with the most recent version being 3.1.

# 2. Installation

## 2.1. Install Java
According to the documentation Apark 3.1.1 requires Java 8/11. In the case of the openjdk, we will see a version of 1.8.x coresponding to Oracle version 8.

## 2.2. Install Programming Language
Accodring to the documentation Spark has the following compatabilities for it's landuage bindings:

    Scala 2.12
    Python 3.6+
    R 3.5+

Insure a compatable version is installed. In our case we are using python.

# 3. Relevant Notebooks
- [Install Apache Spark Prerequisites](Install%20Apache%20Spark%20Prerequisites.ipynb)
- [Running Apache Spark Locally](Running%20Apache%20Spark%20Locally.ipynb)