# Overview
In this notebook we give a definition of eigenvalues, eigenvectors, and eigen-decomposition.

The equations are written in matrix algebra so having an understanding of the topic would help.

# 1. What Are Eigenvalue, Eigenvectors, and Eigen-Decomposition
In German, the prefix “eigen” means “specific of” or “characteristic of” or "proper". Eigenvectors and eigenvalues are also referred to as characteristic vectors and latent roots or characteristic equation. Initially, eigenvalues were called "Proper Values" in the United States but that term is no longer used.

Eigenvalues and eigenvectors are properties of mathematical objects; specifically square matrices like our correlation matrix. These properties are derived using eigen-decomposition; a mathematical process to solve a specific system of equations.

The set of eigenvalues of a matrix is also called its spectrum and have a conection with spectral theory which is concerned with extending the theory to a wider range of mathematical structures and operations.

Not every square matrix will have eigenvalues/eigenvectors however. Luckily for us, the correlation matrix will.

For more information consider the following sources:
- [Linear Algebra – What are eigenvalues and eigenvectors](https://www.youtube.com/watch?v=kwA3qM0rm7c)
- [Eigenvectors and eigenvalues | Chapter 14, Essence of linear algebra](https://www.youtube.com/watch?v=PFDu9oVAE-g)
- *Encyclopedia of Measurement and Statistics* ~ Abdi
- [What the Heck are Eigenvalues and Eigenvectors?](https://hubpages.com/education/What-the-Heck-are-Eigenvalues-and-Eigenvectors)

# 2. Mathematical Definitions
While we don't neet to know/understand the mathematical theory it does help us sanity check our work! We will explore the definitions before looking at the python code to give us the answers.

## 2.1. The Fundamental Theory of Eigenvectors and Eigenvalues
The fundamental theory of eigenvectors and eigenvalues states that a (non-zero) vector $v$ of dimension N is an *eigenvector* of a square NxN matrix A if it satisfies the linear equation

$$Av = \lambda v $$

where $\lambda$ is a scalar, termed the *eigenvlue*, which corespondes to the eigenvector $v$.

There are multiple possible eigenvectors for the NxN matrix A. The spectral theroy allows us to identify that situation.

### 2.2. Spectral Theory

Let $A$ be a square n × n matrix with n linearly independent eigenvectors $q_i$ (where $i = 1, ..., n$). Then $A$ can be factorized as:

$$ A = Q \Lambda Q^{-1} $$

As this is a special case (square matrix) we can say that $Q$ is orthogonal and thus:

$$ A = Q \Lambda Q^T $$

We can apply the spectral theory to decompose our square correlation matrix into its canonical form: two square matrices consisting of eigenvalues $\Lambda$ and eigenvectors $Q$ respectively.

https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix



