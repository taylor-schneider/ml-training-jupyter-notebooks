# Overview
In this notebook we provide a general overview of eigenvalues and eigenvectors and try to answer some FAQs. As the [README](README.md) suggests, we will start off simply and then gradually introduce more rigor.

# FAQs
## What Are Eigenvalues and Eigenvectors?
To put it simply, we can think of eigenvalues and eigenvectors as special properties exhibited by some matrices. For a matrix with special properties, we can derive a set of eigenvalues and eigenvectors. We will get to what these properties are and how they are used but for right now its important to understand that they are a characteristic of a matrix.

## How Do We Know If A Matrix Hase Them?
There are proofs that show if a matrix has certain other properties, it also has eigenvalues and eigenvectors. We will get into that in the other notebooks.

## How Do We Obtain Them?
In mathematics, we use matrices to represent data and/or transformations of data. [Matrix decomposition](../Decomposition.ipynb) is the process of decomposing a matrix in such a way that the component matrices can be "put back together" to obtain the original matrix. In the case of eigen-decomposition, the components of the decomposition are eigenvalues and eigenvectors. In this way we see that how having eigenvalues/vectors is a property.

## What Is The Meaning Behind Strange Name
In German, the prefix “eigen” means “specific of” or “characteristic of” or "proper". Eigenvectors and eigenvalues are also referred to as characteristic vectors and latent roots or characteristic equation. Initially, eigenvalues were called "Proper Values" in the United States but that term is no longer used. 

In more recent literature the eigenvectors have also been referred to as canonical vectors as there is a repeatable process to derive this singular, or canonical, set of eigenvectors. I prefer this naming as it relates the topic directly to the use of the property.

## How Are They Used?

We can think of them like [basis vectors](../../Mathematics/Vectors/Basis%20Vectors.ipynb). For a given set of data there exists only one set of eigenvalues and eigenvectors. As such it allows us to "orient" orselves within the data in a consistent manner regardless of the application. 

As we [build intuition](Intuition%20Behind%20Eigen-Decomposition.ipynb) we will see that they can be used to summarize our data. 

Eigenvectors appear in mechanics and physics (specifically in principal axis theory). The idea is that when linear transformation affects a vector, some vectors are only scaled while remaining on their original span. (no rotation or change of angle/direction). These special vectors are called eigenvectors and the eigenvalue is the factor by which they are stretched or squished during the transformation. In the practical case, if the transformation is a rotation, the eigenvector is the axis of rotation. The corresponding eigenvalue would be one because the axis is not stretched in the case of rotation.

Another application which is more closely related to machine learning is that of Principal Component Analysis (PCA). The basic idea behind PCA is that we can decompose the correlation matrix of a vector to obtain a set of eigenvectors which point in the direction of the best fit lines for the data and a set of eigenvalues which quantify how much variance is accounted for by the best fit line. This quantification allows us to perform dimensionality redution by removing features which to not contribute a large amount of informaiton. It also allows us to perform classification by identifying datapoints which fall outside a pre-defined "ring of normality". For more information see the [notebooks about PCA](../../Data%20Science/Principal%20Component%20Analysis%20(PCA)/README.md)

They are commonly used for [Principal Component Analysis](../../../Data%20Science/Principal%20Component%20Analysis%20(PCA)/README.md)

# Important Properties of Eigenvectors and Eigenvalues
The following was mostly created while working on PCA... I just didn't know where else to put the content.

- They come in pairs (every eigen vector has a coresponding eigenvalue)
- The # of pairs is equal to the # of dimensions (variables)
- eigenvectors of covariance matrix are the directions of the orthogonal best-fit vectors with most variance
- Eigenvalues give amount of variance coresponding to each eigenvector (their square root gives the std. deviation)


# References
For more information consider the following sources:
- [Linear Algebra – What are eigenvalues and eigenvectors](https://www.youtube.com/watch?v=kwA3qM0rm7c)
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- *Encyclopedia of Measurement and Statistics* ~ Abdi
- [What the Heck are Eigenvalues and Eigenvectors?](https://hubpages.com/education/What-the-Heck-are-Eigenvalues-and-Eigenvectors)