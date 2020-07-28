import numpy as np
import pandas as pd

#1
# importation de la data frame titanic
titanic = pd.read_csv('C:/Users/Proprietaire/Desktop/App/TP1/titanic.csv',sep=",")#Importer le fichier csv
#2
# Description de la dataset
# la dataset titanic contient 891 individus x 12 variables
titanic.info()
#3 Basic statistics : mean of each variable, quartiles
titanic.describe()
# moyenne sur toutes les variables
titanic.mean()
# 4 Percentage of missing values for each column. Sort by descending values

############## Exercice 2 #########

colonnes = ['PassengerId','Ticket']
titanic_select = titanic[colonnes]
titanic_select
