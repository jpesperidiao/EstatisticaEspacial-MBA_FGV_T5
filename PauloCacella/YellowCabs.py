# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:11 2020

@author: joaoa
@paulo  cacella

"""

import pandas as pd
import os

#Verificando para qual diretório está apontando
os.getcwd()
#Alterando para o diretório onde está o CSV
os.chdir("D:\GEO")

print("reading  data")
df = pd.read_csv("yellow_tripdata_2020-01.csv")
print(" data read")
#eliminando as colunas listadas abaixo
df1 = df.drop(['VendorID', 'RatecodeID','store_and_fwd_flag', 'payment_type'], axis =1)
df1.dtypes

#alterando timestamps para o tipo datetime
df1['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df1['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

#Criando uma coluna com o tempo total da corrida
df1['Total_time'] = (df1['tpep_dropoff_datetime'] - df1['tpep_pickup_datetime']).dt.seconds/60

#criando colunas de embarque e desembarque com data e hora separadas
#dta  em dia  de semana
df1['PU_Weekday'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%Y:%M:%D').dt.weekday
df1['PU_Time'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%Y:%M:%D').dt.seconds/3600

df1['DO_Weekday'] = pd.to_datetime(df1['tpep_dropoff_datetime'], format='%Y:%M:%D').dt.weekday
df1['DO_Time'] = pd.to_datetime(df1['tpep_dropoff_datetime'], format='%Y:%M:%D').dt.seconds/3600

#cria  preço limpo
df1['CleanPrice']  = df1['total_amount']-df1['improvement_surcharge']-df1['congestion_surcharge']-df1['tolls_amount']-df1['mta_tax']

#remove  campos desnecessarios
df2 = df1.drop(['tip_amount','extra','congestion_surcharge','improvement_surcharge','tolls_amount','mta_tax','tpep_pickup_datetime','tpep_dropoff_datetime'], axis =1)

df2.dtypes

print("writing  data")
df2.to_csv("data.csv")
