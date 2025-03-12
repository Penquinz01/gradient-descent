def gradient_descent(a,b,c,d,x,learning_rate = 0.01,num_iterations = 10000):
    '''
        J = (a*x**3 +b*x**2+c*x+d)**2
        dJ_dx = 2*(a*x**3 + bx**2 + c*x +d)*(3a*x**2+2*b*x+c)

        in each iterations
         x = x-learning_rate*dJ_dx
         clamp x using relu
    '''
    for i in range(num_iterations):
        fx = loss(a,b,c,d,x)
        grad = derivatives(a,b,c,d,x,fx)
        x = x-learning_rate*grad

    return x
def loss(a,b,c,d,x):
    return a*x**3 +b*x**2+c*x+d
def derivatives(a,b,c,d,x,fx):
    return 2*fx*(3*a*x**2+2*b*x+c)


a =2
b = -2
c =2
d =2

#initial guess
x = 0
x = gradient_descent(a,b,c,d,x)

print(f"Approximate value of x is {x}")
