# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy='1.13')
values = [int(x) for x in input().split()]
print (numpy.eye(values[0], values[1]))