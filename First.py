'''
In that code i solved next mathematical task:

Two segments are given on a number line: [a, b] and [c, d] Write a program that finds their intersection.
The intersection of two segments can be:
-line segment;
-dot;
-empty set.
'''
a, b, c, d = int(input()), int(input()), int(input()), int(input())
if a < c:
   amax = c
else:
   amax = a
if b < d:
   bmin = b
else:
   bmin = d
if amax > bmin:
   print("пустое множество")
elif amax == bmin:
   print(amax)
else:
   print(amax, bmin)
