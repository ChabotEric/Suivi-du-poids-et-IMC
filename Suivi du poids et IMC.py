#coding:utf-8
"""
Suivi du Poids
Programme qui fait le suivi du poids et de 
l'indice de masse corporel (IMC) et conserne 
le tout dans un fichier CSV.
Version 1.0
Auteur: Eric Chabot
"""

from os import system, path
from includes.fonctions import *
from datetime import date
import csv
import tkinter


# Observateur:
def obtientSysteme(*args):
    if varSysteme.get():
        poidsSysteme.set("Entrez votre poids en livre: ")
        tailleSysteme.set("Entrez votre taille en pieds: ")
    else:
        poidsSysteme.set("Entrez votre poids en kilogramme: ")
        tailleSysteme.set("Entrez votre taille en mètre: ")

    return poidsSysteme, tailleSysteme                

def enregistrer(*args):
    if varSysteme.get():
        nom = varNom.get()
        poids = float(varPoids.get())
        masseKg = conversionLbsKg(poids)
        taillePieds = float(varTaille.get())
        tailleM = conversionPiedsM(taillePieds)
        imc = indiceMasseCorp(masseKg, tailleM)
        etiquettePoids = "Poids en livres"
        today = date.today()
        csvName = "CSV\\" + nom + ".csv"
        ecrireCsv(csvName, today, poids, imc, etiquettePoids)  
        varImc.set("Votre indice de masse corporel (IMC): {}".format(imc))
        varImcTexte.set(tableImc)
        return varImc, varImcTexte
    else:
        nom = varNom.get()
        masseKg = float(varPoids.get())
        poids = masseKg
        tailleM = float(varTaille.get())
        imc = indiceMasseCorp(masseKg, tailleM)
        etiquettePoids = "Poids en Kg"
        today = date.today()
        csvName = "CSV\\" + nom + ".csv"
        ecrireCsv(csvName, today, poids, imc, etiquettePoids)  
        varImc.set("Votre indice de masse corporel (IMC): {}".format(imc))
        varImcTexte.set(tableImc)
        return varImc, varImcTexte

   
# Création et paramètrage de la fenêtre:
app = tkinter.Tk()
app.title("Suivi du poids et IMC")
app.geometry("620x400")

#Frames:

frame1 = tkinter.Frame(app, width = 600, height = 40)
frame1.pack(side = "top")

frame2 = tkinter.Frame(app, width = 600, height = 40)
frame2.pack(side = "top")

frame3 = tkinter.Frame(app, width = 600, height = 40)
frame3.pack(side = "top")

frame4 = tkinter.Frame(app, width = 600, height = 40)
frame4.pack(side = "top")

# Variables:
varNom = tkinter.StringVar()

varSysteme = tkinter.IntVar()
varSysteme.set(1)
varSysteme.trace("w", obtientSysteme)

poidsSysteme = tkinter.StringVar()
poidsSysteme.set("Entrez votre poids en livre: ")
varPoids = tkinter.StringVar()

tailleSysteme = tkinter.StringVar()
tailleSysteme.set("Entrez votre taille en pieds: ")
varTaille = tkinter.StringVar()

varImc = tkinter.StringVar()
varImcTexte = tkinter.StringVar()


# Widgets:
tkLabelNom = tkinter.Label(frame1, text = "Entrez votre nom: ", )
tkNom = tkinter.Entry(frame1, textvariable = varNom)

tkSysteme1 = tkinter.Radiobutton(frame2, text = "Système métrique", value = 0, variable = varSysteme)
tkSysteme2 = tkinter.Radiobutton(frame2, text = "Système impérial", value = 1, variable = varSysteme)

tkLabelPoids = tkinter.Label(frame3, textvariable = poidsSysteme )
tkPoids = tkinter.Entry(frame3, textvariable = varPoids )

tkLabelTaille = tkinter.Label(frame4, textvariable = tailleSysteme )
tkTaille = tkinter.Entry(frame4, textvariable = varTaille )

tkBoutonEnregistrer = tkinter.Button(app, text = "Enregistrer !", command = enregistrer)

tkLabelImc = tkinter.Label(app, textvariable = varImc)

tkImcTexte = tkinter.Message(app, width = 600, textvariable = varImcTexte)

# Packs
tkLabelNom.pack(side = "left", padx = 5, pady = 20)
tkNom.pack(side = "left", pady = 20)
tkSysteme1.pack(side = "top")
tkSysteme2.pack(side = "top")
tkLabelPoids.pack(side = "left", pady = 20)
tkPoids.pack(side = "left", pady = 20)
tkLabelTaille.pack(side = "left")
tkTaille.pack(side = "left")
tkBoutonEnregistrer.pack(pady = 20)
tkLabelImc.pack()
tkImcTexte.pack()

app.mainloop()
