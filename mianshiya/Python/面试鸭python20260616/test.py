"""
a = 0b1100
print(a)
b = ~a
print(b)

a = -0b1100
print(a)
b = ~a
print(b)


"""
import math

print(math.pi)
print(math.cos(math.pi))
print(math.sin(math.pi))
print(math.sqrt(4))
print(abs(-4))

a = [1,5,9,10,80,2,3,5,9,6]
a_vi = [(a[i],i) for i in range(len(a))]
print(a_vi)
a_vi.sort(key=lambda x: x[0],reverse=True)
print(a_vi)