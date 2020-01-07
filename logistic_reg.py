import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
import math
from typing import List
import numpy as np

st.title('Logistic Regression')
st.markdown('**_The Problem_**: ')
'We have an anonymized dataset of about 200 users, containing each user’s salary, her years of experience as a data scientist, and whether she paid for a premium account. We will use the Logistic Regression method to predict if the user is a premium or not'

tuples = [(0.7,48000,1),(1.9,48000,0),(2.5,60000,1),(4.2,63000,0),(6,76000,0),(6.5,69000,0),(7.5,76000,0),(8.1,88000,0),(8.7,83000,1),(10,83000,1),(0.8,43000,0),(1.8,60000,0),(10,79000,1),(6.1,76000,0),(1.4,50000,0),(9.1,92000,0),(5.8,75000,0),(5.2,69000,0),(1,56000,0),(6,67000,0),(4.9,74000,0),(6.4,63000,1),(6.2,82000,0),(3.3,58000,0),(9.3,90000,1),(5.5,57000,1),(9.1,102000,0),(2.4,54000,0),(8.2,65000,1),(5.3,82000,0),(9.8,107000,0),(1.8,64000,0),(0.6,46000,1),(0.8,48000,0),(8.6,84000,1),(0.6,45000,0),(0.5,30000,1),(7.3,89000,0),(2.5,48000,1),(5.6,76000,0),(7.4,77000,0),(2.7,56000,0),(0.7,48000,0),(1.2,42000,0),(0.2,32000,1),(4.7,56000,1),(2.8,44000,1),(7.6,78000,0),(1.1,63000,0),(8,79000,1),(2.7,56000,0),(6,52000,1),(4.6,56000,0),(2.5,51000,0),(5.7,71000,0),(2.9,65000,0),(1.1,33000,1),(3,62000,0),(4,71000,0),(2.4,61000,0),(7.5,75000,0),(9.7,81000,1),(3.2,62000,0),(7.9,88000,0),(4.7,44000,1),(2.5,55000,0),(1.6,41000,0),(6.7,64000,1),(6.9,66000,1),(7.9,78000,1),(8.1,102000,0),(5.3,48000,1),(8.5,66000,1),(0.2,56000,0),(6,69000,0),(7.5,77000,0),(8,86000,0),(4.4,68000,0),(4.9,75000,0),(1.5,60000,0),(2.2,50000,0),(3.4,49000,1),(4.2,70000,0),(7.7,98000,0),(8.2,85000,0),(5.4,88000,0),(0.1,46000,0),(1.5,37000,0),(6.3,86000,0),(3.7,57000,0),(8.4,85000,0),(2,42000,0),(5.8,69000,1),(2.7,64000,0),(3.1,63000,0),(1.9,48000,0),(10,72000,1),(0.2,45000,0),(8.6,95000,0),(1.5,64000,0),(9.8,95000,0),(5.3,65000,0),(7.5,80000,0),(9.9,91000,0),(9.7,50000,1),(2.8,68000,0),(3.6,58000,0),(3.9,74000,0),(4.4,76000,0),(2.5,49000,0),(7.2,81000,0),(5.2,60000,1),(2.4,62000,0),(8.9,94000,0),(2.4,63000,0),(6.8,69000,1),(6.5,77000,0),(7,86000,0),(9.4,94000,0),(7.8,72000,1),(0.2,53000,0),(10,97000,0),(5.5,65000,0),(7.7,71000,1),(8.1,66000,1),(9.8,91000,0),(8,84000,0),(2.7,55000,0),(2.8,62000,0),(9.4,79000,0),(2.5,57000,0),(7.4,70000,1),(2.1,47000,0),(5.3,62000,1),(6.3,79000,0),(6.8,58000,1),(5.7,80000,0),(2.2,61000,0),(4.8,62000,0),(3.7,64000,0),(4.1,85000,0),(2.3,51000,0),(3.5,58000,0),(0.9,43000,0),(0.9,54000,0),(4.5,74000,0),(6.5,55000,1),(4.1,41000,1),(7.1,73000,0),(1.1,66000,0),(9.1,81000,1),(8,69000,1),(7.3,72000,1),(3.3,50000,0),(3.9,58000,0),(2.6,49000,0),(1.6,78000,0),(0.7,56000,0),(2.1,36000,1),(7.5,90000,0),(4.8,59000,1),(8.9,95000,0),(6.2,72000,0),(6.3,63000,0),(9.1,100000,0),(7.3,61000,1),(5.6,74000,0),(0.5,66000,0),(1.1,59000,0),(5.1,61000,0),(6.2,70000,0),(6.6,56000,1),(6.3,76000,0),(6.5,78000,0),(5.1,59000,0),(9.5,74000,1),(4.5,64000,0),(2,54000,0),(1,52000,0),(4,69000,0),(6.5,76000,0),(3,60000,0),(4.5,63000,0),(7.8,70000,0),(3.9,60000,1),(0.8,51000,0),(4.2,78000,0),(1.1,54000,0),(6.2,60000,0),(2.9,59000,0),(2.1,52000,0),(8.2,87000,0),(4.8,73000,0),(2.2,42000,1),(9.1,98000,0),(6.5,84000,0),(6.9,73000,0),(5.1,72000,0),(9.1,69000,1),(9.8,79000,1),]

# We have this list of tuples that represent the data of the 200 users, we will convert it to a list of lists
data = [list(row) for row in tuples]

st.markdown('**_The data_**')

xs = [[1.0] + row[:2] for row in data]  # [1, experience, salary]
ys = [row[2] for row in data]

df = pd.DataFrame({
    '[1, experience, salary]': xs,
    '[premium]': ys,
})
agree = st.checkbox('Show data')
if agree:
    st.write(df)


st.markdown('**The Logistic Function**')
with st.echo():
    def logistic(x: float) -> float:
        return 1.0 / (1 + math.exp(-x))
st.write('The logistic regression uses, of course, the logistic function')
xs = np.arange(-10., 10., 0.2 )

ys: List[float] = []
for x in xs:
    ys.append(logistic(x))
# print(ys)

plt.plot(xs, ys, color='green')
plt.title('Logistic Function')
plt.ylabel('f(x)')
plt.xlabel('x')
st.pyplot()

'Here is the logistic derivative: '
with st.echo():
    def logistic_prime(x: float) -> float:
        y = logistic(x)
        return y * (1 - y)

st.markdown('_Here is the **log likelihood** that we will "maximize with" **Gradient Descent**_')
st.latex(r''' \log L(\beta|x_i, y_i) =  y_i\log f(x_i \beta) + (1 - y_i) \log(1-f(x_i \beta))''')
'Because the Gradient Descent minimizes things we will work with the negative log likelihood and minimize it.'

# Create a few resources to create the function
Vector = List[float]


def dot(v: Vector, w: Vector) -> float:
    assert len(v) == len(w), 'must have the same size'
    return sum(v_i * w_i for v_i, w_i in zip(v, w))
assert dot([1, 2, 3], [4, 5, 6]) == 32

def vector_sum(vectors: List[Vector]) -> Vector:
    assert vectors, "no vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"

    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]

st.subheader("Let's code")
with st.echo():
    def _negative_log_likelihood(x: Vector, y: float, beta: Vector) -> float:
        if y ==1:
            return -math.log(logistic(dot(x, beta)))
        else:
            return -math.log(1 - logistic(dot(x, beta)))
st.write('We will now sum all the log likelihood')
with st.echo():
    def negative_log_likelihood(xs: List[Vector], ys: List[Vector], beta: Vector) -> float:
        return sum(_negative_log_likelihood(x, y, beta) for x, y in zip(xs, ys))

    def _negative_log_partial_j(x: Vector, y: float, beta: Vector, j: int) -> float:
        return -(y - logistic(dot(x, beta))) * x[j]

    def _negative_log_gradient(x: Vector, y: float, beta: Vector) -> Vector:
        return [_negative_log_partial_j(x, y, beta, j)
                for j in range(len(beta))]

    def negative_log_gradient(xs: List[Vector], ys: List[float], beta: Vector) -> Vector:
        return vector_sum([_negative_log_gradient(x, y, beta)
                           for x, y in zip(xs, ys)])
