#coding:utf-8

from os import path
import csv


# Fonctions de conversion

def conversionLbsKg(masseLbs):
    masseKg = float(masseLbs) * 0.45359237
    return masseKg

def conversionPiedsM(taillePieds):
    tailleM = float(taillePieds) * 0.3048
    return tailleM

def indiceMasseCorp(masseKg, tailleM):
    imc = masseKg / tailleM ** 2
    return imc
    

# Variable table de résultats IMC

tableImc = """
IMC < 18,5 = Poids insuffisant -> Risque accru d'avoir des probèmes de santé.
IMC entre 18,5 et 24,9 = Poids normal -> Risque moindre d'avoir des probèmes de santé.
IMC entre 25,0 et 29,9 = Excès de poids -> Risque accru d'avoir des probèmes de santé.
IMC entre 30,0 - 34,9 = Obésité, classe I -> Risque élevé d'avoir des probèmes de santé.
IMC entre 35,0 - 39,9 = Obésité, classe II -> Risque très élevé d'avoir des probèmes de santé.
IMC plus de 40,0 = Obésité, classe III -> Risque extrêmement élevé d'avoir des probèmes de santé.
"""


# Fonction CSV

def ecrireCsv(csvName, today,poids, imc, etiquettePoids):
    if path.isfile(csvName):
        with open(csvName, 'a', newline='') as fichier:
            writer = csv.writer(fichier, delimiter = ";")
            writer.writerow([today, poids, imc])
    else:
        with open(csvName, 'w', newline='') as fichier:
            writer = csv.writer(fichier, delimiter = ";")
            writer.writerow(["Date", etiquettePoids,"IMC"])
            writer.writerow([today, poids, imc])


