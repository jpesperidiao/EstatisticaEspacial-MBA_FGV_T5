# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:11 2020

@author: paulo  cacella

"""

import pandas as pd
import os

#Verificando para qual diretório está apontando
os.getcwd()
#Alterando para o diretório onde está o CSV
os.chdir("D:\Geo")

print("reading  data")
dt = pd.read_csv("data.csv")


print("data read")

dt['TaxaGanhoDistancia']=dt['CleanPrice']/dt['trip_distance']
dt['TaxaGanhoTempo']=dt['CleanPrice']/dt['Total_time']
dt['TaxaGanhoDistTempo']=dt['CleanPrice']/dt['trip_distance']/dt['Total_time']
# carrega arquivo de dados  de distritos
dlookup = pd.read_csv("shapedataXY.csv")

df = dt.merge(dlookup,left_on='PULocationID',right_on="OBJECTID")
df1 = df.drop(['fare_amount', 'OBJECTID','Shape_Leng', 'Shape_Area', 'zone', 'LocationID', 'borough'], axis =1)
df1 = df1.drop(df1.columns[0], axis=1)
df1 = df1.drop(df1.columns[1], axis=1)
print("writing  data")
df1.to_csv("dataXY.csv")
