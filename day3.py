# -*- coding: utf-8 -*-
"""Day3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fh-3dVFAUMJ9HaeSCXcZOs64z-Jiy5MV
"""

#1st program

a=input("Enter altitude:")
a =int(a)

if a<=1000:
  print("Safe to land")
elif a <= 5000:
    print("Bring down to 1000")
else:
      print("Turn Around")

#2nd program

for n in range(1,201):
  count = 0
  for i in range(2,(n//2+1)):
    if(n%i==0):
      count=count+1
      break

  if(count==0 and n != 1):
    print("%d" %n,end=',')

