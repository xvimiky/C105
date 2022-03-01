# stdev = sqrt[ ( sum of [(xi - mean)^2] )/n-1 ]

# 

# median --> avg of 20 & 30 --> 25
# mean = sum of all elements /total no of elements --> 100/4 = 25

# x1-mean --> 10-25 = -15 --> (-15)^2 --> 225
# x2-mean --> 20-25 = -5 --> (-5)^2 --> 25
# x3-mean --> 30-25 = 5 --> (5)^2 --> 25
# x4-mean --> 40-25 = 15 --> (15)^2 --> 225


# sum of --> 225 + 25 + 25 + 225 --> 500

# stdev = sqrt(500/3) --> sqrt(166.66) --> 12.88

#--------------------------------------------------------------------

import math

x = [10,20,30,40]

#-------------------- mean ------------------
n= len(x)

total =0

for i in x:
    total += int(i)

mean = total / n

#-------------------- stdev ----------------------
squared_list= []
for number in x:
    a = int(number) - mean
    a= a**2
    squared_list.append(a)

#getting sum
sum =0
for i in squared_list:
    sum =sum + i

#dividing the sum by the total values
result = sum/ (len(x)-1)

# getting the deviation by taking square root of the result
std_deviation = math.sqrt(result)
print( round(std_deviation) )
