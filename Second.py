'''
The input is a natural number nn, and then nn different natural numbers in sequence,
sequentially at each stage. A program is written that prints the final and second
finite number of a sequence.
'''
largest = -1
biggest = -1
a = int(input())
for i in range(a):
  num = int(input())
  if num > largest:
    biggest = largest
    largest = num
  else:
    if num < largest and num > biggest:
      biggest = num
print(largest)
print(biggest)