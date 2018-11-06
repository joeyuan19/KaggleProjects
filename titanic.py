# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import matplotlib.pyplot as plt
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import random

data = pd.read_csv("train.csv")
for cat in data:
    print(cat)
g = {
    "male":[0,0],
    "female":[0,0]
}

for survived,sex in zip(data.Survived,data.Sex):
    g[sex][0] += survived
    g[sex][1] += 1

for gender,stats in g.items():
    g[gender] = stats[0]/stats[1]

a = {"n/a":[0,0]}
for survived,age in zip(data.Survived,data.Age):
    if np.isnan(age):
        a["n/a"][0]  += survived
        a["n/a"][1]  += 1
    elif age not in a:
        a[age] = [survived,1]
    else:
        a[age][0] += survived
        a[age][1] += 1

for age,stats in a.items():
    a[age] = stats[0]/stats[1]
print(a)

x,y = [],[]
for age,p in a.items():
    if age == "n/a":
        x.append(-1)
    else:
        x.append(age)
    y.append(p)

plt.plot(x,y,'bo')
plt.show()

import sys
sys.exit()

test = pd.read_csv("test.csv")

output = "PassengerId,Survived\n"
for index, row in test.iterrows():
    if random.random() < g[row["Sex"]]:
        Survived = 1
    else:
        Survived = 0
    output += str(row["PassengerId"]) + "," + str(Survived) + "\n"
output = output[:-1]

with open("output.csv","w") as f:
    f.write(output)



