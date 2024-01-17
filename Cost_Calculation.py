#COSTCALCULATION
import os
import pandas as pd
import tkinter as tk
    
def calculate_costs():
    # Lesen Sie Projektdaten ein
    df2 = pd.read_excel("Projektdaten.xlsx")
    
    # Holen Sie die Nutzung aus Projektdaten
    Nutzung = df2.at[0, "Gebäudenutzung"]
    print(Nutzung)
    
    # Wählen Sie die richtige Kostendatenbank basierend auf der Nutzung
    if Nutzung == "Einfamilienhaus":
        df1 = pd.read_excel("Kostendatenbank.xlsx", sheet_name="Einfamilienhaus")
    elif Nutzung == "Mehrfamilienhaus":
        df1 = pd.read_excel("Kostendatenbank.xlsx", sheet_name="Mehrfamilienhaus")
    elif Nutzung == "Gewerbe":
        df1 = pd.read_excel("Kostendatenbank.xlsx", sheet_name="Gewerbe")   
    elif Nutzung == "Industrie":
        df1 = pd.read_excel("Kostendatenbank.xlsx", sheet_name="Industrie")    
    else:
        raise ValueError("Ungültige Nutzung") 
    
    #BKP 0
    #Grundstück
    Grundstück = df1.at[0, "Einheitspreis"]
    print("Grundstückquadratmeterpreis:",Grundstück, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    Gru_F = df2.at[0, "Gru_F"]  
    print("Grundstücksfläche:" , Gru_F, "m2")
    # Die Werte multiplizieren
    Gr_Cost = Grundstück * Gru_F
    # Den resultierenden Wert ausgeben
    print("Grundstückskosten:", Gr_Cost, "CHF")

    #Gebühren
    Gebühren_Cost = Gr_Cost * 0.007
    print("Gebühren:", Gebühren_Cost, "CHF")

    BKP0 = Gr_Cost+Gebühren_Cost
    print("Kosten BKP0:", BKP0, "CHF")

    #BKP 1
    #Vorbereitungsarbeiten
    Vorbereitung = df1.at[3, "Einheitspreis"]
    print("Vorbereitungseinheitspreis:",Vorbereitung, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    GF = df2.at[0, "GF"]  
    print("Geschossfläche:" , GF, "m2")
    # Die Werte multiplizieren
    Vorbereitung_Cost = GF/3 * Vorbereitung 
    # Den resultierenden Wert ausgeben
    print("Vorbereitungskosten:", Vorbereitung_Cost, "CHF")

    BKP1 = Vorbereitung_Cost
    print("Kosten BKP1:", BKP1, "CHF")

    #BKP 2 - Gebäude
    GAZ = df2.at[0, "Geschossanzahl"]  
    print("Geschossanzahl:" , GAZ)   
    
    #Rohbau
    Rohbau = df1.at[8, "Einheitspreis"]
    print("Rohbaueinheitspreis:",Rohbau, "pro m3")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    GV = df2.at[0, "GV"]  
    print("Gebäudevolumen:" , GV, "m3")
    # Die Werte multiplizieren
    Rohbau_Cost = Rohbau * GV
    # Den resultierenden Wert ausgeben
    print("Rohbaukosten:", Rohbau_Cost, "CHF")

    #Garage
    #Preis auslesen
    Garage = df1.at[9, "Einheitspreis"]
    print("Garageneinheitspreis:",Garage, "pro m2")
    # Den Wert aus "Projektdaten" auslesen
    df2 = pd.read_excel("Projektdaten.xlsx")
    GAF = df2.at[0, "Dachfläche"]  
    print("Garagenfläche:" , GAF, "m2")
    # Die Werte multiplizieren
    Garage_Cost = Garage * GAF
    # Den resultierenden Wert ausgeben
    print("Garagenkosten:", Garage_Cost, "CHF")

    #Nebenraum
    Nebenraum = df1.at[10, "Einheitspreis"]
    print("Nebenraumflächenkosten:",Nebenraum, "pro m2")
    # Den Wert aus "Projektdaten" auslesen
    df2 = pd.read_excel("Projektdaten.xlsx")
    NRF = df2.at[0, "Nebenraumfläche"]  
    print("Nebenraumfläche:" , NRF, "m2")
    # Die Werte multiplizieren
    Nebenraum_Cost = Nebenraum * NRF
    # Den resultierenden Wert ausgeben
    print("Nebenraumkosten:", Nebenraum_Cost, "CHF")

    #Gewerbe
    Gewerbe = df1.at[11, "Einheitspreis"]
    print("Gewerbeflächekosten:",Gewerbe, "pro m2")
    # Den Wert aus "Projektdaten" auslesen
    df2 = pd.read_excel("Projektdaten.xlsx")
    GWF = df2.at[0, "Gewerbefläche"]  
    print("Gewerbefläche:" , GWF, "m2")
    # Die Werte multiplizieren
    Gewerbe_Cost = Gewerbe * GWF
    # Den resultierenden Wert ausgeben
    print("Gewerbeflächenkosten:", Gewerbe_Cost, "CHF")

    #Wohnen
    Wohnen = df1.at[12, "Einheitspreis"]
    print("Wohnflächekosten:",Wohnen, "pro m2")
    # Den Wert aus "Projektdaten" auslesen
    df2 = pd.read_excel("Projektdaten.xlsx")
    WHF = df2.at[0, "Wohnungsfläche"]  
    print("Wohnungsfläche:" , WHF, "m2")
    # Die Werte multiplizieren
    Wohnen_Cost = Wohnen * WHF
    # Den resultierenden Wert ausgeben
    print("Wohnflächenkosten:",Wohnen_Cost , "CHF")

    #Aussenflächen
    Aussen = df1.at[13, "Einheitspreis"]
    print("Aussenflächenkosten:",Aussen, "pro m2")
    # Den Wert aus "Projektdaten" auslesen
    df2 = pd.read_excel("Projektdaten.xlsx")
    AF = df2.at[0, "Balkonfläche"]  
    print("Aussenfläche:" , AF, "m2")
    # Die Werte multiplizieren
    Aussen_Cost = Aussen * AF
    # Den resultierenden Wert ausgeben
    print("Aussenflächenkosten:",Aussen_Cost , "CHF")

    #Dach
    Dach = df1.at[14, "Einheitspreis"]
    print("Dachflächenkosten:",Dach, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    DF = df2.at[0, "Dachfläche"]  
    print("Dachfläche:" , DF, "m2")
    # Die Werte multiplizieren
    Dach_Cost = Dach * DF
    # Den resultierenden Wert ausgeben
    print("Dachkosten:", Dach_Cost, "CHF")



    BKP2 = Garage_Cost + Nebenraum_Cost + Gewerbe_Cost + Wohnen_Cost + Wohnen_Cost + Aussen_Cost + Dach_Cost 
    print("Kosten BKP2:", BKP2, "CHF")
    
    #Industrieeinrichtung
    Industrieeinrichtung = df1.at[17, "Einheitspreis"]
    print("Industrieeinrichtungseinheitspreis:",Industrieeinrichtung, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    IF = df2.at[0, "Industriefläche"]  
    print("Industriefläche:" , IF, "m2")
    # Die Werte multiplizieren
    Industrieeinrichung_Cost = Industrieeinrichtung * IF
    # Den resultierenden Wert ausgeben
    print("Industrieeinrichungkosten:", Industrieeinrichung_Cost, "CHF")

    #Gewerbeeinrichtung
    Gewerbeeinrichtung = df1.at[18, "Einheitspreis"]
    print("Industrieeinrichtungskosten:",Gewerbeeinrichtung, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    # Den Wert aus "Projektdaten" auslesen
    print("Gewerbefläche:" , GWF, "m2")
    # Die Werte multiplizieren
    Gewerbeinrichtung_Cost = Gewerbeeinrichtung * GWF
    # Den resultierenden Wert ausgeben
    print("Gewerbeeinrichtungskosten:", Gewerbeinrichtung_Cost, "CHF")

    BKP3 = Industrieeinrichung_Cost + Gewerbe_Cost
    print("Kosten BKP3:", BKP3, "CHF")

    #BKP4
    #Umgebung
    Umgebung = df1.at[17, "Einheitspreis"]
    print("Umgebungskosten:",Umgebung, "pro m2")
    df2 = pd.read_excel("Projektdaten.xlsx")
    GF = df2.at[0, "GF"]  
    # Den Wert aus "Projektdaten" auslesen
    UMF = ((Gru_F - 2*GF))
    print("Geschossfläche:", UMF , "m2")
    # Die Werte multiplizieren
    Umgebung_Cost = Umgebung * UMF
    # Den resultierenden Wert ausgeben
    print("Umgebungskosten:", Umgebung_Cost, "CHF")

    BKP4 = Umgebung_Cost
    print("Kosten BKP4:", BKP4, "CHF")

    #BKP5
    #Baunebenkosten
    Baukosten = BKP1 + BKP2 + BKP3 + BKP4
    Bauneben_Cost = Baukosten * 0.06 
    print("Baunebenkosten:", Bauneben_Cost, "CHF")

    BKP5 = Bauneben_Cost
    print("Kosten BKP1:", BKP5, "CHF")

    #Honorare
    Honorar = BKP1 + BKP2 + BKP3 + BKP4
    Honorar_Cost = Honorar * 0.15 
    print("Honorar:", Honorar_Cost, "CHF")

    print("Kosten BKP0:", BKP0, "CHF")
    print("Kosten BKP1:", BKP1, "CHF")
    print("Kosten BKP2:", BKP2, "CHF")
    print("Kosten BKP3:", BKP3, "CHF")
    print("Kosten BKP4:", BKP4, "CHF")
    print("Kosten BKP5:", BKP5, "CHF")
    
    Gesamtkosten = BKP0 + BKP1 + BKP2 + BKP3 + BKP4 + BKP5
    print ("Die Gesamtkosten des Gebäudes sind:" , Gesamtkosten, "CHF") 
      
    return Gesamtkosten, BKP0, BKP1, BKP2, BKP3, BKP4, BKP5
    

if __name__ == "__main__":
    calculate_costs()    