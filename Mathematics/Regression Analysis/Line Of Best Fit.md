# Overview
The line of best fit is typically a straight line that passes though our data in the best possible way. That is to say that it minimizes the error (differences) between the line and the coresponding data points which it is attempting to model. This difference is expressed mathematically as $(\hat y - y)$.

Another definition that frequently appears is a line which maximizes the variance; meaning the cumulative distance between the mean and the poitns in the data set is maximized (placing the line in the center of the data). This is written mathematically as $(x - \bar x)$.

See this site and relate info above to the graph: https://builtin.com/data-science/step-step-explanation-principal-component-analysis

<img src="images/Line%20Of%20Best%20Fit%20And%20Variance.gif">

# 1. Definition Of Line Of Best Fit
In this next section we will look at the definitions for the linear regression

## 1.1. The Simple Univariate Case

Given an independent variable $x$ which maps to a dependent variable $y$, we can mathematically denot the equation as:

$$ y = mx + b$$

Given a sample of data for $x$ and $y$ we can construct a line of best fit through the data:

$$ \hat y = \hat m x + \hat b $$

Where the "hat" terms represent our approximations. 

We can define the error in our regression as 

$$ \epsilon = y - \hat y $$

Doing some mathematical substitution we see:

$$ y = \hat y + \epsilon $$

$$ 0 = y - \hat m x - \hat b - \epsilon $$

## 1.2. The General Multivariate Case
When using $n$ dimensions, a multidimensional line can be represented as

$$ Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \cdots + \beta_n X_n $$

Where $\beta_0$ is the y-intercept, and $\beta_i$ is the "weight" or "regression coefficient" assigned to each variable.

Given a sample of data for $X$ and $Y$ we can construct a line of best fit through the data:

$$ \hat Y = \hat\beta_0 + \hat\beta_1 X_1 + \hat\beta_2 X_2 + \cdots + \hat\beta_n X_n$$

Rewriting this in summation notation we have:

$$ Y = \beta_0 + \sum^n_i \beta_i X_i$$

In matrix notation this would be:

$$ Y = \beta_0 + \beta^T X $$

It is equivalent to represent the equation as:

$$ Y = \beta_0 + X \beta^T $$

In some notations, the equation is simplified by assuming $X_0=1$ and combining the lone $\beta_0$ into the larger $\beta$ term:

$$
\beta = 
\begin{pmatrix}
\beta_0 \\
\beta_1 \\
\vdots \\
\beta_n
\end{pmatrix}
$$

$$
X = 
\begin{pmatrix}
1       & X_{1,1} & \cdots & X_{n,1} \\
1       & X_{1,2} & \cdots & X_{n,2} \\
\vdots  & \vdots  & \ddots & \vdots  \\
1       & X_{1,m} & \cdots & X_{n,m} 
\end{pmatrix}
$$


$$ Y = \beta^T X $$

**Note**: In the case of no y-intercept, $X_0 = 0$ and is omitted from the algebra.

Given a sample of data for $X$ and $Y$ we can construct a line of best fit through the data:

$$ \hat Y = \hat \beta^T X $$

We can define the error in our regression as 

$$ \epsilon = Y - \hat Y $$

Doing some mathematical substitution we see:

$$ Y = \hat Y + \epsilon $$

$$ 0 = Y - X \beta^T - \epsilon $$

# 2. Finding The Regression Coefficients
There are many ways to find the coefficients, we will use Ordinary Least Squares (OLS).

## 2.1. Ordinary Least Squares (OLS)

The basic idea is to find coefficients which minimize the difference between the actual data points of the dependent variable $y$ and those predicted by the regression line $\hat y$ (ie. minimize $ y-\hat y $).

Mathematically speaking, we will construct a closed form a loss function that we want to minimize. For a simple linear regression (univariate) we would have the follwoing:

$$ L = \sum(y-\hat y)^2 $$

$$ = \sum(y - \hat m x - \hat b)^2   $$

For a multiple regression (multivariate) our loss function would be

$$ L = (Y - \hat Y)^T(Y - \hat Y) $$

$$ L = (Y - \hat \beta_0 - {\hat \beta}^T X)^T(Y - \hat \beta_0 - {\hat \beta}^T X) $$

We can solve each of these closed form solutions below.

### 3.2.1. Solve Univariate OLS

#### 3.2.1.1. Find $\hat b$

We can take the derivative of the loss function using the chain rule, power rule, and the property of additivity

let $u = y - \hat m x + \hat b$

$$ L = \sum u ^2 $$

$$ \frac{\partial L}{\partial \hat b} = 2 \sum u \ du \  d \hat b $$

$$ = 2 \sum (y - \hat m x - \hat b)(-1) $$

$$ = -2 \sum (y - \hat m x - \hat b) $$

We then set the equation equal to 0, simplify, and solve

$$ \frac{\partial L}{\partial \hat b} = 0 $$

$$ 0 = -2 \sum (y - \hat m x - \hat b) $$

$$ 0 = \sum (y - \hat m x - \hat b) $$

$$ 0 = \sum y - \sum \hat m x - \sum \hat b $$

$$ \sum y = \sum \hat m x + \sum \hat b $$

$$ \sum^n y = \sum^n \hat m x + n \hat b $$

$$ \frac{\sum^n y}{n} = \frac{\sum^n \hat m x}{n} + \hat b $$

$$ \hat b = \frac{\sum^n y}{n} - \frac{\sum^n \hat m x}{n} $$

$$ \hat b = \bar y - \frac{\sum^n \hat m x}{n} $$

$$ \hat b = \bar y - \hat m \bar x $$

We can calculate the  mean values ($\bar x$ and $\bar y$) so really the only variable about which to minimize is $m$.

#### 3.2.1.2 Find $\hat m$

We repeat the process as before

let $u = y - \hat m x + \hat b$

$$ L = \sum u ^2 $$

$$ \frac{\partial L}{\partial \hat m} = 2 \sum u \ du \  d \hat b $$

$$ = 2 \sum (y - \hat m x - \hat b)(-x) $$

$$ = -2x \sum (y - \hat m x - \hat b) $$

We then set the equation equal to 0, simplify, and solve

$$ \frac{\partial L}{\partial \hat m} = 0 $$

$$ 0 = -2\sum (y - \hat m x - \hat b)x $$

$$ 0 = \sum (y - \hat m x - \hat b)x $$

Now substitute the value of $ \hat b = \bar y - \hat m \bar x $

$$ 0 = \sum (y - \hat m x - \bar y + \hat m \bar x)x $$

We know $x$ is not trivial

$$ 0 = \sum (y - \bar y + \hat m \bar x - \hat m x ) $$

$$ 0 = \sum (y - \bar y) - \hat m \sum ( \bar x - x) $$

$$ \hat m \sum (- \bar x + x) = \sum (y - \bar y) $$

$$ \hat m \sum (x - \bar x) = \sum (y - \bar y) $$


$$ \hat m  = \frac{\sum (y - \bar y)}{\sum ( x - \bar x)} $$

By doing one more manipulation we see that $\hat m$ is equal to the pearson correlation coefficient. If we multiply by one, $\frac{\sum ( x - \bar x)}{\sum ( x - \bar x)}$, this becomes clear.

$$ \hat m  = \frac{\sum (y - \bar y)( x - \bar x)}{\sum ( x - \bar x)^2} $$

With this derevation, $\hat m$ and $\hat b$ are now solavable and the minimum point can be obtained.

### 3.2.2. Solve Multivariate OLS

#### 3.2.2.1. Find $\hat \beta$

We start by expanding our loss function

$$ L = (Y - \hat Y)^T(Y - \hat Y) $$

$$ = (Y - {\hat \beta}^T X)^T(Y - {\hat \beta}^T X) $$

$$ = (Y^T - {\hat \beta} X^T)(Y - {\hat \beta}^T X) $$

We perform the multiplication

$$ = Y^T Y - Y^T \hat \beta X^T - \hat \beta X^T Y + \hat \beta X^T \hat \beta^T X$$

The transpose of a scalar is equal to that scalar

$$ = Y^T Y - Y^T \hat \beta X^T - Y^T \hat \beta X^T + \hat \beta X^T \hat \beta^T X$$

$$ = Y^T Y - 2 Y^T \hat \beta X^T + \hat \beta X^T \hat \beta^T X$$

We then take the derivative and set it equal to zero

$$ \frac{\partial L}{\partial \hat \beta} = 0$$ 

$$ \frac{\partial }{\partial \hat \beta} \left[ Y^T Y - 2 Y^T \hat \beta X^T + \hat \beta X^T \hat \beta^T X  \right]= 0$$

$$  - 2 Y X^T + 2 \hat \beta X^T X = 0$$

$$ 2 \hat \beta X^T X = 2 Y X^T $$

$$ \hat \beta X^T X = X^T Y$$

If we multiply a matrix by its inverse we get the identity matrix $I$

$$ (X^T X)^{-1} (X^T X) \hat \beta = (X^T X)^{-1} X^T Y $$

$$ I \hat \beta = (X^T X)^{-1} X^T Y$$

$$ \hat \beta = (X^T X)^{-1} X^T Y $$

Additional notes can be found [here](https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf)