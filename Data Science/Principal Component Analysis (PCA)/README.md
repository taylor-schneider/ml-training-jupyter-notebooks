# Overview
In this notebook we explore the concept of Principal Component Analysis. This technique is a powerful tool which is typically used for dimentionality reduction. PCA will try to measure the importance of a feature by measuring the variance that the variable introduces into the system. We then minimize the number of factors selected while maximizing the amount of variance preserved by the selected factors. In this way we can model the problem while reducing the number of variables (dimensions) in the problem.


# Notebooks
It is reccomended that the notebooks/documentation be read in the following order:
1. [Introduction To Eigenvalues And Eigenvectors](../../Mathematics/Matrix%20Algebra/Eigenvalues%20And%20Eigenvectors/Introduction%20To%20Eigenvalues%20And%20Eigenvectors.md)
2. [Intuition Behind Eigen-Decomposition](../../Mathematics/Matrix%20Algebra/Eigenvalues%20And%20Eigenvectors/Intuition%20Behind%20Eigen-Decomposition.ipynb)
3. [Principal Component Analysis](Principal%20Component%20Analysis.ipynb)

While creating the related notebooks, I wanted to do some sanity checks to make sure the eigenvalues/eigenvectors behaved the way they should. I was new to matrix algebra and numpy/pandas so I wanted to verify my code was written the way the math was written. We can see a few examples of using numpy to do proofs in [this notebook](../../Mathematics/Matrix%20Algebra/Eigenvalues%20And%20Eigenvectors/Numpy%20Eigen-decomposition%20Proof%20Check.ipynb)