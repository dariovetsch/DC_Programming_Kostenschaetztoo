import matplotlib.pyplot as plt
import tkinter as tk
from Cost_Calculation import calculate_costs
from Extra import extra_cost

def presentation():
    # Rufen Sie calculate_costs auf, um die BKP-Werte zu erhalten
    gesamtkosten, bkp0, bkp1, bkp2, bkp3, bkp4, bkp5 = calculate_costs()

    # BKP-Kategorien und zugehörige Kosten, einschließlich Gesamtkosten
    bkp_categories = ["BKP0", "BKP1", "BKP2", "BKP3", "BKP4", "BKP5", "Gesamtkosten"]
    
    # Erstellen Sie die Liste der Kostenwerte, einschließlich Gesamtkosten
    bkp_values = [bkp0, bkp1, bkp2, bkp3, bkp4, bkp5, gesamtkosten]
    plt.figure(figsize=(10, 6))
    plt.bar(bkp_categories, bkp_values, color='skyblue')

    # Beschriftung und Titel hinzufügen
    plt.xlabel('BKP-Kategorie')
    plt.ylabel('Kosten CHF in Mio.')
    plt.title('Kostenübersicht nach BKP-Kategorien inkl. Gesamtkosten')

    # Kostenwerte über den Balken anzeigen
    for i, cost in enumerate(bkp_values):
        formatted_cost = '{:,.0f} CHF'.format(cost).replace(',', ' ')
        plt.text(i, cost + 100, formatted_cost, ha='center', va='bottom')

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

def presentation_extra_cost():
    # Rufen Sie extra_cost auf, um die Kosten für Fenster, Türen und Küche zu erhalten
    fenster_cost, tür_cost, küche_cost = extra_cost()

    # Kategorien und Kostenwerte
    categories = ["Fenster", "Türen", "Küche"]
    costs = [fenster_cost, tür_cost, küche_cost]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, costs, color='skyblue')

    # Beschriftung und Titel hinzufügen
    plt.xlabel('Bauteilart')
    plt.ylabel('Kosten in CHF')
    plt.title('Einzelkosten für Fenster, Türen und Küche')

    # Kostenwerte über den Balken anzeigen
    for i, cost in enumerate(costs):
        formatted_cost = '{:,.0f} CHF'.format(cost).replace(',', ' ')
        plt.text(i, cost + 1000, formatted_cost, ha='center', va='bottom')

    # Diagramm anzeigen
    plt.tight_layout()
    plt.show()

# Beispielaufruf der Präsentationsfunktionen
if __name__ == "__main__":
    presentation()
    presentation_extra_cost()
