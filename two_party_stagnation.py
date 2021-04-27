import matplotlib.pyplot as plt
import numpy as np
from project import run

def compete(x,s,c,u,dx):
    plt
    plt.clf()
    plt.plot(x, s, label="Square Party")
    plt.plot(x,c, label ="Circle Party")
    plt.plot(x, u, label="Unaffiliated Voters")
    plt.xlabel('Vote Cycle')
    plt.ylabel('Percentage of Vote')
    plt.legend()
    #plt.show()
    plt.savefig("New_d_is_"+str(dx)+"k_is"+str(k)+".png")


if __name__ == '__main__':
    c = .7
    s = .3
    u = 1 - c - s
    d_val = [.5, 1, 3]
    ks = [.1, .4, .7]
    for k_x in range(len(ks)):
        k = ks[k_x]
        for d_x in range(len(d_val)):
            d = d_val[d_x]
            vals, ds = run(s, c, u, d, k)
            A = np.array(vals)
            times = range(1, 27)
            compete(times, A[:,0],A[:,1],A[:,2], d_val[d_x])




