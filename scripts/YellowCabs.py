# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 17:53:11 2020

@author: joaoa
"""

import pandas as pd
import os

#Verificando para qual diretório está apontando
os.getcwd()
#Alterando para o diretório onde está o CSV
os.chdir("D:/MBA/Desafios e Requisitos dos Projetos Analíticos")

df = pd.read_csv("yellow_tripdata_2020-01.csv")

#eliminando as colunas listadas abaixo
df1 = df.drop(['VendorID', 'RatecodeID','store_and_fwd_flag', 'payment_type','fare_amount',
               'extra', 'mta_tax', 'tip_amount', 'tolls_amount', 'improvement_surcharge', 
               'congestion_surcharge'], axis =1)
df1.dtypes

#alterando timestamps para o tipo datetime
df1['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
df1['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

#Criando uma coluna com o tempo total da corrida
df1['Total_time'] = df1['tpep_dropoff_datetime'] - df1['tpep_pickup_datetime']

#criando colunas de embarque e desembarque com data e hora separadas
df1['PU_Date'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%Y:%M:%D').dt.date
df1['PU_Time'] = pd.to_datetime(df1['tpep_pickup_datetime'], format='%Y:%M:%D').dt.time

df1['DO_Date'] = pd.to_datetime(df1['tpep_dropoff_datetime'], format='%Y:%M:%D').dt.date
df1['DO_Time'] = pd.to_datetime(df1['tpep_dropoff_datetime'], format='%Y:%M:%D').dt.time

df.head(10)