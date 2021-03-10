#!/usr/bin/python3

def total (pri, rate, add_pri, add_rate, count):
    total = pri;
    add = add_pri
    for i in range(0, int(count)):
        if (i == 0):
            total = total*(1.0+rate)
        else:
            if (1 == i):
                total = (total+add_pri)*(1.0+rate)
            else:
                total = (total+add_pri*(1.0+add_rate))*(1.0+rate)

    return total


str = ""
while( str != "y"):
    principal = input("principal: ")
    principal = float(principal)
    rate      = input("rate: ")
    rate      = float(rate)
    add_pri   = input("add principal every year: ")
    add_pri   = float(add_pri)
    add_rate  = input("principal rate every year: ")
    add_rate  = float(add_rate)
    years     = input("years: ")
    years     = float(years)
    total     = total(principal, rate, add_pri, add_rate, years)
    print("tatal: %.2e " % total)
    print("quit ?")
    str = input()

    
       
