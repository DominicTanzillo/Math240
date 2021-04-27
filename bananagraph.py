import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import csv

indexes_of_value = []

for count in range(1,21):
    with open("k_layer_small"+str(count)+".csv", newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        row_count = 0
        for row in file:
            ele_count=0
            for element in row:
                if int(float(element)) == 3:
                    indexes_of_value.append([count/10,row_count/10,ele_count/50])
                ele_count+=1
            row_count +=1

B = np.array(indexes_of_value)

x=B[:,0]
z=B[:,1]
y=B[:,2]

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x,y,z)
ax.set_xlabel('Value of k')
ax.set_ylabel('Value of s')
ax.set_zlabel('Value of d')
ax.set_xlim([0,1])
ax.set_ylim([0, .16])
ax.set_yticks([0,.04,.08,.12,.16,.20])
ax.set_zlim([0,4])

# .ylabel('Value of s')
plt.savefig("3D_Graph.png")
#plt.zlabel('Value of s')
plt.show()
plt.clf()

for count in range(1,21):
    one_k = []
    with open("k_layer_small"+str(count)+".csv", newline='') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        row_count = 0
        for row in file:
            ele_count = 0
            for element in row:
                if int(float(element)) == 3:
                    one_k.append([row_count / 10, ele_count / 50])
                ele_count += 1
            row_count += 1

    C = np.array(one_k)
    x_l = C[:, 1]
    y_l = C[:, 0]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_l, y_l)
    ax.set_xlim([0,.16])
    ax.set_ylim([0, 4])
    ax.set_xticks([0, .04, .08, .12, .16, .20])
    plt.xlabel('Value of s')
    plt.ylabel('Value of d')
    plt.savefig("Count"+str(count)+".png")
    plt.show()
    plt.clf()


print("Done")

#for csv in csv list


