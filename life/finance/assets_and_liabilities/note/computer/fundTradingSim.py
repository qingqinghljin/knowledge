#!/usr/bin/python3
import math
# h
h_p = input("highest point:")
h_p = float(h_p)
l_p = input("lowest point:")
l_p = float(l_p)
c_p = input("current point:")
c_p = float(c_p)
l_t_h   = h_p - l_p
l_t_c   = c_p - l_p
c_t_h   = h_p - c_p
f1  = c_t_h/l_t_h
f2  = math.pow((1+f1), (1+f1))
print ("down position:", "%.2f%%" % (f1*100.0))
print ("f1: %.2f" % f1, "f2: %.2f" % f2)
# down
c_h_p  = input("current highest point:")
c_l_p  = input("current lowest point:")
c_val  = input("valuation:")
down = (float(c_h_p) - float(c_l_p)) - float(c_val)
down /= 100.0
down = down * f2
principla = 4000.0
principla = principla*f1
print ("principla: %.2f " % principla)
if (down > 0.05):
    investment_amount = principla * down
print ("suggested investment principal: %.2f %%" % (down*100.0))
print ("suggested single investment amount: %.2f " % investment_amount)








