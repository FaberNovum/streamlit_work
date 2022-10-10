from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
# Introduction to Linear Regression

I've been thinking of how to teach data science tools in an approachable way.

I recently found Streamlit and think it might be a good fit.

So I'm going to test it out with a few concepts and see how it sticks.

Let me know what you think.

## What's linear regression?

Linear regression is a simple and easy to understand algorithm used in machine learning.

As with a lot of algorithms in machine learning, linear regression is stolen from statistics.

Here's the equation:
"""
st.latex(body= "y=B0 + B1*x")

latext = r'''
Where:

$${y}=$$ Output

$${B0}=$$ First coefficient

$${B1}=$$ Second coefficient

$${x}=$$ Input values
'''

st.write(latext)

st.write("Note that there will be as many coefficients as there are input columns.")
st.write("With the information you've learned thus far, can you guess what the model will do with these coefficients?")

"""
The linear regression model will estimate the values of the coefficients with the data (input columns) you have.


"""

"""

## Why use linear regression?

Several reasons:
- It's simple
- Easy to learn
- Easy to implement

"""

"""

## When to use linear regression?

When you need to predict a continuous value (a number with an infinite number of values between any two values).

It's really that simple.

Here are a couple famous use cases:

- Housing prices

- Stock prices

"""

"""
## How to optimize linear regression

First, what does optimization mean?

Simply put:

Optimization is the iterative improvement of the model.

This improvement happens by using different methods:

- Least Squares
- Gradient Descent
- Regularization

Don't worry about exactly what these are.

We can cover that at another time.

"""

"""
## Rules of Thumb for Linear Regression

1. Linearity
    - Your input and output values have a linear relationship.
2. Noise
    - Your input and output values are not noisy.
3. Collinearity
    - Your input columns aren't highly correlated.
4. Gaussian
    - Your input and output values have a normal (Gaussian) distribution.
5. Scale
    - Your input values share the same scale.

"""

"""
## Conclusion

So that's it.

One of the most straightforward algorithms in machine learning.

I will probably add a basic code walkthrough so keep an eye out for that.

Thanks for reading.
"""

