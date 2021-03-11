#!/usr/bin/python3
import math

def estimatedRate(cost, pri, c_cost, inves):
    x = (pri+inves)*c_cost
    y = pri*c_cost + inves*cost
    z = 1 - x/y
    return z
# h
h_p = input("highest point:")
h_p = float(h_p)
l_p = input("lowest point:")
l_p = float(l_p)
c_p = input("current point:")
c_p = float(c_p)
is_down = input("is down ? : ")
if (is_down == 'y') :
    down = -5.0
else:
    down = 5.0
c_p     += down
l_t_h   = h_p - l_p
l_t_c   = c_p - l_p
c_t_h   = h_p - c_p
f1  = c_t_h/l_t_h
f2  = math.pow((1+f1), (1+f1))
print ("down position:", "%.2f%%" % (f1*100.0))
print ("f1: %.2f" % f1, "f2: %.2f" % f2)
# down
down /= 100.0
down = down * f2
principal = 4000.0
principal = principal*f1
print ("principal: %.2f " % principal)
investment_amount = 0.0
if (down > 0.05):
    investment_amount = principal * down
print ("suggested investment principal: %.2f %%" % (down*100.0))
print ("suggested single investment amount: %.2f " % investment_amount)

principal = float(input("principal: "))
position_cost = float(input("position cost: "))
asset_value = float(input("funds' net asset value: "))

estimated   = estimatedRate(position_cost, principal, asset_value, investment_amount)
print("estimated: %.2f " % estimated)









