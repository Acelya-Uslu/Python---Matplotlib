# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 16:51:09 2022

@author: Acelya
"""

#matplotlib library
#görselleştirme kütüphanesi
#Line plot,scatter plot ,bar plot , subplots,histogram


#Pandas review
import pandas as pd

df=pd.read_csv("Iris.csv")
print(df.columns)

#Her satıra sample deniyor.
#iris datası-->Bu çiçeğin 3 tane türü var.(Species) = setosa, viginica, versicolor

print(df.Species.unique())
print(df.info())
print(df.describe())
print("*********")
setosa=df[df.Species == "Iris-setosa"]
print(setosa.describe())

versicolor=df[df.Species =="Iris-versicolor"]
print(versicolor.describe())

#%% Line Plot

import matplotlib.pyplot as plt

df1=df.drop(["Id"],axis=1)
#id bilgisini drop ederek veri setinden  çıkartıyoruz.
#axis=1 column 
#axis=0 row
#türlere class da denir.


#df1.plot() # default olarak line plot basar.
#df1.show()#çizilen plotun gösterilmesini sağlar.
#grafikteki keskin geçişler tür geçişleridir.


setosa=df[df.Species =="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]


plt.plot(setosa.Id , setosa.PetalLengthCm, color="red" , label="setosa")
plt.plot(versicolor.Id , versicolor.PetalLengthCm, color="yellow" , label="versicolor")
plt.plot(virginica.Id , virginica.PetalLengthCm, color="blue" , label="virginica")

plt.xlabel("Id")
plt.ylabel("PetalLengthCm")
plt.legend()
plt.show()


df1.plot(grid=True,linestyle=":",alpha=0.5) #arkaplan, alpha=0.5 (saydamlık)0'a yaklaşınca saydamlık artar.
plt.show()




#%% Scatter Plot
# Genelde iki tane featurı karşılaştırmak için  kullanılır.



setosa=df[df.Species =="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]


plt.scatter(setosa.PetalLengthCm , setosa.PetalWidthCm ,color="red", label="setosa")
plt.scatter(versicolor.PetalLengthCm , versicolor.PetalWidthCm ,color="yellow", label="versicolor")
plt.scatter(virginica.PetalLengthCm , virginica.PetalWidthCm ,color="blue", label="virginica")

plt.legend()
plt.xlabel("PetalLengthCm")
plt.ylabel("PetalWidthCm")
plt.title("Scatter Plot")
plt.show()


#%% Histogram
#İstatiksel olarak bilgi edinmek için önemli bir plot

plt.hist(setosa.PetalLengthCm,bins=10)
plt.xlabel("PetalLengthCm Values")
plt.ylabel("Frekans")
plt.title("Hist")
plt.show()



#%% Bar Plot

# import numpy as np

# x = np.array([1,2,3,4,5,6,7])
# y = x*2+5

# plt.bar(x,y)
# plt.title("Bar Plot")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()


import numpy as np

x = np.array([1,2,3,4,5,6,7])
a = ["Turkiye","Usa","a","Turkiye","b","Usa","d"]
y = x*2+5

plt.bar(a,y)
plt.title("Bar Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.show()


#%% Subplots



df1.plot(grid=True,alpha=0.9,subplots=True)
plt.show()


setosa=df[df.Species =="Iris-setosa"]
versicolor=df[df.Species=="Iris-versicolor"]
virginica=df[df.Species=="Iris-virginica"]

plt.subplot(2,1,1) #2 tane subplotum olcak. 1cisinin 1.si çizdiriyoruz
plt.plot(setosa.Id , setosa.PetalWidthCm ,color="red", label="setosa")
plt.ylabel("setosa - PetallengthCm")


plt.subplot(2,1,2) #2 tane subplotum olcaki1.csinin 2.columını çziyoz.
plt.plot(versicolor.Id , versicolor.PetalWidthCm ,color="green", label="versicolor")
plt.ylabel("versicolor - PetallengthCm")
plt.show()

#%% Matplotlib, Python programlama dili ve sayısal matematik uzantısı olan Numpy 
#için bir çizim kütüphanesidir.












