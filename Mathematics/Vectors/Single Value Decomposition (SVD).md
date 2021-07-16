# Overview
In this document we establish the mathematical framework for single value decomposition.

**Single Value Decomposition (SVD)** is a mathematial process of solving a system of equations to derive a specific set of mathematical objects. One of these objects is called an eigenvector and as such, SVD is sometimes refferred to as **eigen-decomposition**.

There are two cases by which we do SVD: the case where our vector set produces a non-square matrix (asymetrical) and the case where it does (symetrical).

# 1. Single Value Decomposition
## 1.1. The Asymetrical Case
We can apply single value decomposition theory to decompose an original vector $A$ into orthogonal vectors ($U$ and $V^T$) and a diagonal ($\Sigma$) matrix.

$$ A = U \Sigma V^T $$

**Note:** An important property of orthogonal vectors is that they are uncorrelated.

**Note:** In the case of SVD, the vectors $U$ and $V$ are referred to as **eigenvectors**.

## 1.2. The Symmetrical Case

If we know a matrix $A$ is symtric semi-definite positive, we know its eigenvectors are orthogonal ($Q$ and $Q^T$) and we can write:

$$ A = Q \Lambda Q^T$$

Here $\Lambda$ represents a the eigenvalue matrix. It is a square matrix with eigenvalues along the diagonals and zeros elsewhere. 

**Note:** The Symetrical case is is a special case such that $U = V = Q$. This arguably makes the problem much simpler to solve.

**Note:** The covariance matrix is an example of a symetric positive definitie matrix.


[source](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/positive-definite-matrices-and-applications/singular-value-decomposition/MIT18_06SCF11_Ses3.5sum.pdf)

### 1.2.1 Positive Semi-definite Matrix
A matrix $A \in \mathbb R^{nxn} $ is positive semi-definite if
$$ v^TAv \ge 0, \ \ \ \ \ \ \ \ \  \forall v \in \mathbb R^n
$$
http://theanalysisofdata.com/probability/C_4.html

### 1.2.2. Properties of Eigenvectors and Eigenvalues

- They come in pairs (every eigen vector has a coresponding eigenvalue)
- The # of pairs is equal to the # of dimensions (variables)
- eigenvectors of covariance matrix are the directions of the orthogonal best-fit vectors with most variance
- eigenvalues give amount of variance coresponding to each eigenvector (their square root gives the std. deviation)

### 1.2.3. Applications of Eigenvalues and Eigenvectors

Eigenvectors appear in mechanics and physics (specifically in principal axis theory). The idea is that when linear transformation affects a vector, some vectors are only scaled while remaining on their original span. (no rotation or change of angle/direction). These special vectors are called eigenvectors and the eigenvalue is the factor by which they are stretched or squished during the transformation. In the practical case, if the transformation is a rotation, the eigenvector is the axis of rotation. The corresponding eigenvalue would be one because the axis is not stretched in the case of rotation.

Another application which is more closely related to machine learning is that of Principal Component Analysis (PCA). The basic idea behind PCA is that we can decompose the correlation matrix of a vector to obtain a set of eigenvectors which point in the direction of the best fit lines for the data and a set of eigenvalues which quantify how much variance is accounted for by the best fit line. This quantification allows us to perform dimensionality redution by removing features which to not contribute a large amount of informaiton. It also allows us to perform classification by identifying datapoints which fall outside a pre-defined "ring of normality". For more information see the [notebooks about PCA](../../Data%20Science/Principal%20Component%20Analysis%20(PCA)/README.md)