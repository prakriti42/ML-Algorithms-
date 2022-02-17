import numpy as np

def gradient_descent(x,y):
    m_curr = b_curr = 0
    n = len(x)
    iterations = 1000  #steps to take 
    learning_rate = 0.002  #step size

    for i in range(iterations):
        y_predicted = m_curr * x + b_curr  #finding predicted value at the point
        cost = (1/n) * sum ([val**2 for val in (y - y_predicted)])  #cost function
        md = -(2/n)*sum(x*(y-y_predicted)) #finding derivative of m
        bd = -(2/n)*sum((y-y_predicted))

        m_curr = m_curr - md * learning_rate #updating m
        b_curr = b_curr - bd * learning_rate #updating b
        print("m {}, b {}, error {} iteration {}".format(m_curr, b_curr, cost, i))

x  = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x, y)