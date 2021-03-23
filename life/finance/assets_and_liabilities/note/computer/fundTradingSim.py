#!/usr/bin/python3
import math

def estimatedRate(cost, pri, c_cost, inves):
    x = (pri+inves)*c_cost
    y = pri*c_cost + inves*cost
    z = 1 - x/y
    return z

def fundHightLow(filename, id):
    f = open(filename, "r")
    for line in f:
        a = line.split()
        b = a[0]
        if b == id:
            return a

# h
id  = input("fund id:")
list = fundHightLow("../data", id)
for i in list:
    print(i)
l_p = float(list[1])
h_p = float(list[2])
c_p = input("current point:")
c_p = float(c_p)
estimate = input("estimate range:")
estimate = float(estimate)
c_p += estimate
if (h_p < c_p):
    h_p = c_p
elif (c_p < l_p):
    l_p = c_p
l_t_h   = h_p - l_p
c_t_h   = h_p - c_p
f1  = c_t_h/l_t_h
f2  = math.pow((1+f1), (1+f1))
f3  = 0.05*f2
print ("down position:", "%.2f%%" % (f1*100.0))
print ("f1: %.2f" % f1, "f2: %.2f" % f2, "f3: %.2f%%" % (f3*100.0))
# are the conditions met
f4 = 5.0 * (1-f1)
print ("amplitude: %.2f%%" % f4)

principal = 4000.0
principal = principal*f1
print ("principal: %.2f " % principal)
investment_amount = principal * f3
print ("suggested single investment amount: %.2f " % investment_amount)

#principal = float(input("principal: "))
#position_cost = float(input("position cost: "))
#asset_value = float(input("funds' net asset value: "))

#estimated   = estimatedRate(position_cost, principal, asset_value, investment_amount)
#print("estimated: %.2f " % estimated*100.0)

