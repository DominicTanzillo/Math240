import random
import math
import numpy

def update_apathy(s,c,k):
    #l = c+s
    l = pow(c,2)+pow(s,2)
    A_s = (k*pow(s,2))/l
    A_c = (k*pow(c,2))/l

    return A_s,A_c

def update_propaganda(s,c,d):
    D = 8/(1+math.exp(-d))
    #D = 4/(1+math.exp(-d))
    P_s = D * (1 - c - s) * s
    P_c = D * (1 - c - s) * c
    return P_s, P_c

def new_size(s,c,u,A_s,A_c,P_s,P_c,d):

    s_new = s*(1-A_s)+u*P_s
    c_new = c * (1 - A_c) + u * P_c
    u_new = 1 - c_new - s_new

    return s_new, c_new, u_new,d

def update_donations(d):
    d = d*1.03
    return d
    #return d*(1+(1-u))

def run_sim(s,c,u,d,k):

    A_s,A_c = update_apathy(s,c,k)
    d = update_donations(d)
    P_s, P_c = update_propaganda(s,c,d)
    # d = update_donations(d,u)

    return new_size(s,c,u,A_s,A_c,P_s,P_c,d)

def constant_opponent(s_const,c_const,u,d):
    l_ = math.pow(c_const, 2) + math.pow(s_const, 2)
    A_s = (k * math.pow(s_const, 2)) / l_
    D = 4 / (1 + math.exp(-d))
    P_s = D * (1 - c_const - s_const) * s_const
    s_new_ = s_const * (1 - A_s) + u * P_s
    u_new_ = 1 - s_new_-c_const

    return s_new_,u_new_


def run(s,c,u,d,k):
    vals = []
    vals.append([s,c,u])
    ds = []
    ds.append(d)
    s_const = s
    c_const = c
    #constant_vals = []
    cycles = 0
    while cycles < 30:
        #s_const, u_const = constant_opponent(s_const,c_const,u,d)
        #constant_vals.append((s_const,u_const))
        s,c,u,d = run_sim(s,c,u,d,k)
        ds.append(d)
        vals.append([s,c,u])
        cycles +=1
    return vals, ds #constant_vals

if __name__ == '__main__':
    c = .5
    s = .3
    u = 1-c-s
    d = 3
    k = .1

    vals, ds = run(s,c,u,d)

    A = numpy.array(vals)
    #B = numpy.array(constant_vals)
    print("done?")

    print("haha")