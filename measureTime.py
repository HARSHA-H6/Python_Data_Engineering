# adding the two numbers by measuring the time
import time

x = 100
y = 200
z=x+y
start_time =time.time()
print(f"The result of adding {x} and {y} is {z} ")
print("*********** %s microseconds*********"%((time.time()-start_time)*10**6))

start_time = time.time()
print("The result of adding",x,"and",y,"is",z)
print("*********** %s microseconds*********"%((time.time()-start_time)*10**6))
