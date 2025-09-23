# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = [int(x) for x in input().split()]
arrA = []
arrB = []
for y in range(n):
    for x in input().split():
        arrA.append(int(x))
for y in range(n):
    for x in input().split():
        arrB.append(int(x))
a = numpy.array(arrA,int)
b = numpy.array(arrB,int)
print("["+str(a+b)+"]")
print("["+str(a-b)+"]")
print("["+str(a*b)+"]")
print("["+str(a//b)+"]")
print("["+str(a%b)+"]")
print("["+str(a**b)+"]")
