import csv
# csv.reader(open('data/rna_import_20221101_dpt_01.csv'),'r')
with open('data/rna_import_20221101_dpt_01.csv','r', encoding='ISO-8859-1') as f:
    reader= csv.reader(f, delimiter=';')
    print(reader)
    for row in reader :
        print (row[0])
import mysql
SQL create table 