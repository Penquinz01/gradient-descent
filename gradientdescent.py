import numpy as np
def gradient_descent(a,b,c,d,x,learning_rate = 0.01,num_iterations = 10000):
    '''
        J = a*x**3 +b*x**2+c*x+d
        dJ_dx = (3a*x**2+2*b*x+c)

        in each iterations
         x = x-learning_rate*dJ_dx
         clamp x using relu
    '''
    for i in range(num_iterations):
        fx = loss(a,b,c,d,x)
        if fx == 0:
            break
        grad = derivatives(a,b,c,d,x,fx)
        x = x-learning_rate*grad
        
        
    return x
def loss(a,b,c,d,x):
    return a*x**3 +b*x**2+c*x+d
def derivatives(a,b,c,d,x,fx):
    return 2*fx*(3*a*x**2+2*b*x+c)


a =float(input("Enter coefficient of x^3:"))
b = float(input("Enter coefficient of x^2:"))
c =float(input("Enter coefficient of x^1:"))
d =float(input("Enter coefficient of x^0:"))

#initial guess
x = np.random.rand()
x = gradient_descent(a,b,c,d,x)

print(f"Approximate value of x is {x}")
