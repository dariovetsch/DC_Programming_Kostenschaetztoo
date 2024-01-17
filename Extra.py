#COSTCALCULATION
import os
import pandas as pd
import tkinter as tk


def extra_cost():
    # Lesen Sie Projektdaten ein
    df2 = pd.read_excel("Projektdaten.xlsx")
    df3 = pd.read_excel("Kostendatenbank.xlsx", sheet_name="Extra")
 
    #Fenster
    Fensterkosten = df3.at[0, "Fenster"]
    print("Fenster:",Fensterkosten, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    FF = df2.at[0, "Fensterfläche"]  
    print("Fensterflfäche:" , FF, "m2")
    # Die Werte multiplizieren
    Fenster_Cost = Fensterkosten * FF
    # Den resultierenden Wert ausgeben
    print("Fensterkosten:", Fenster_Cost, "CHF")      
   
    #Türen
    Türen = df3.at[0, "Türen"]
    print("Türen:", Türen, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    TF = df2.at[0, "Türfläche"]  
    print("Türfläche:" , TF, "m2")
    # Die Werte multiplizieren
    Tür_Cost = Türen * TF
    # Den resultierenden Wert ausgeben
    print("Türkosten:", Tür_Cost, "CHF")   
    
    #Küche
    Küche = df3.at[0, "Küche"]
    print("Küche:", Küche, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    KuZ = df2.at[0, "Küchenfläche"]  
    print("Küchenanzahl:" , KuZ, "m2")
    # Die Werte multiplizieren
    Küche_cost = Küche * KuZ
    # Den resultierenden Wert ausgeben
    print("Türkosten:", Küche_cost, "CHF")   
    
    return Fenster_Cost, Tür_Cost, Küche_cost
    
    
if __name__ == "__main__":
    extra_cost()    