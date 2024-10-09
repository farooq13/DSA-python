from array import *


myarr = array('d', [1.1, 2.2, 3.3])
myarr.extend([4.4, 5.5])

count = 0
while count < myarr[2]:
  print(count)
  count += 1