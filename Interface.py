# Importieren der benötigten Module
import os
import pandas as pd
import tkinter as tk
import openpyxl
import xlsxwriter
from tkinter import ttk
from Cost_Calculation import calculate_costs  # Annahme: Sie haben ein Modul namens Cost_Calculation
from Extra import extra_cost

# Die GUI-Klasse, die die Hauptbenutzeroberfläche darstellt
class GUI:
    def __init__(self, root, on_calculate_callback=None):
        self.root = root
        self.root.title("Kostenschätzungsprogramm")
        self.on_calculate_callback = on_calculate_callback
        self.create_greeting_section()
        self.use_var = tk.StringVar()
        self.data = {}

    # Methode zum Erstellen eines Abschnitts in der GUI
    def create_some_section(self):
        calculate_button = ttk.Button(self.root, text="Berechnen", command=self.on_calculate)
        calculate_button.grid(row=..., column=..., padx=..., pady=...)

    # Methode, die aufgerufen wird, wenn der "Berechnen"-Button geklickt wird
    def on_calculate(self):
        if self.on_calculate_callback is not None:
            self.on_calculate_callback()

    # Methode zum Erstellen des Begrüßungsabschnitts
    def create_greeting_section(self):
        greeting_label = ttk.Label(self.root, text="Willkommen zum Kostenschätzungsprogramm!")
        greeting_label.grid(row=0, column=0, padx=10, pady=10)

        self.next_button = ttk.Button(self.root, text="Weiter", command=self.show_usage_selection)
        self.next_button.grid(row=1, column=0, padx=10, pady=10)

    # Methode zum Leeren des Bildschirms
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # Methode zum Speichern der ausgewählten Gebäudenutzung und Fortfahren zur nächsten Seite
    def save_usage_and_continue(self):
        self.data["Gebäudenutzung"] = self.use_var.get()
        self.show_parameter_entry_total()

    # Methode zur Anzeige der Auswahl der Gebäudenutzung
    def show_usage_selection(self):
        self.clear_screen()

        use_label = ttk.Label(self.root, text="Wählen Sie die Gebäudenutzung:")
        use_label.grid(row=0, column=0, padx=10, pady=10)

        self.use_combobox = ttk.Combobox(self.root, textvariable=self.use_var, values=["Industrie", "Gewerbe", "Einfamilienhaus", "Mehrfamilienhaus"])
        self.use_combobox.grid(row=1, column=0, padx=10, pady=10)

        next_button = ttk.Button(self.root, text="Weiter", command=self.save_usage_and_continue)
        next_button.grid(row=2, column=0, padx=10, pady=10)

    # Methode zur Anzeige der Eingabefelder für allgemeine Parameter
    def show_parameter_entry_total(self):
        try:
            self.clear_screen()

            area_label = ttk.Label(self.root, text="Geben Sie die Geschossfläche(GF) an (m2):")
            area_label.grid(row=0, column=0, padx=10, pady=10)

            area_entry = ttk.Entry(self.root)
            area_entry.grid(row=0, column=1, padx=10, pady=10)

            volume_label = ttk.Label(self.root, text="Geben Sie das Gebäudevolumen an (m3):")
            volume_label.grid(row=1, column=0, padx=10, pady=10)

            volume_entry = ttk.Entry(self.root)
            volume_entry.grid(row=1, column=1, padx=10, pady=10)

            property_label = ttk.Label(self.root, text="Geben Sie die Grundstücksfläche an (m2):")
            property_label.grid(row=2, column=0, padx=10, pady=10)

            property_entry = ttk.Entry(self.root)
            property_entry.grid(row=2, column=1, padx=10, pady=10)

            level_label = ttk.Label(self.root, text="Geben Sie die Anzahl Geschosse an:")
            level_label.grid(row=3, column=0, padx=10, pady=10)

            level_entry = ttk.Entry(self.root)
            level_entry.grid(row=3, column=1, padx=10, pady=10)

            next_button = ttk.Button(self.root, text="Weiter zu SIA416", command=lambda: self.show_parameter_entry_SIA416(area_entry.get(), volume_entry.get(), property_entry.get(), level_entry.get()))
            next_button.grid(row=5, column=0, padx=10, pady=10)

        except Exception as e:
            print(f"Fehler in show_parameter_entry_total: {e}")

    # Methode zur Anzeige der Eingabefelder für SIA416-spezifische Parameter
    def show_parameter_entry_SIA416(self, area, volume, property, level):
        try:
            self.clear_screen()

            garage_label = ttk.Label(self.root, text="Geben Sie die Garagenfläche an (m2):")
            garage_label.grid(row=1, column=0, padx=10, pady=10)

            garage_entry = ttk.Entry(self.root)
            garage_entry.grid(row=1, column=1, padx=10, pady=10)

            Nebenraum_label = ttk.Label(self.root, text="Geben Sie die Nebenraumfläche an (m2):")
            Nebenraum_label.grid(row=2, column=0, padx=10, pady=10)

            Nebenraum_entry = ttk.Entry(self.root)
            Nebenraum_entry.grid(row=2, column=1, padx=10, pady=10)

            wohnen_label = ttk.Label(self.root, text="Geben Sie die Wohnungsfläche an (m2):")
            wohnen_label.grid(row=3, column=0, padx=10, pady=10)

            wohnen_entry = ttk.Entry(self.root)
            wohnen_entry.grid(row=3, column=1, padx=10, pady=10)

            balkon_label = ttk.Label(self.root, text="Geben Sie die Balkonfläche an (m2):")
            balkon_label.grid(row=4, column=0, padx=10, pady=10)

            balkon_entry = ttk.Entry(self.root)
            balkon_entry.grid(row=4, column=1, padx=10, pady=10)

            gewerbe_label = ttk.Label(self.root, text="Geben Sie die Gewerbefläche an (m2):")
            gewerbe_label.grid(row=5, column=0, padx=10, pady=10)

            gewerbe_entry = ttk.Entry(self.root)
            gewerbe_entry.grid(row=5, column=1, padx=10, pady=10)

            industrie_label = ttk.Label(self.root, text="Geben Sie die Industriefläche an (m2):")
            industrie_label.grid(row=6, column=0, padx=10, pady=10)

            industrie_entry = ttk.Entry(self.root)
            industrie_entry.grid(row=6, column=1, padx=10, pady=10)

            next_button = ttk.Button(self.root, text="Weiter zu Extra", command=lambda: self.show_parameter_entry_extra(area, volume, property, level, garage_entry.get(), Nebenraum_entry.get(), wohnen_entry.get(), balkon_entry.get(), gewerbe_entry.get(), industrie_entry.get()))
            next_button.grid(row=8, column=0, padx=10, pady=10)

        except Exception as e:
            print(f"Fehler in show_parameter_entry_SIA416: {e}")

    # Methode zur Anzeige der Eingabefelder für zusätzliche Parameter
    def show_parameter_entry_extra(self, area, volume, property, level, garage, Nebenraum, wohnen, balkon, gewerbe, industrie):
        try:
            self.clear_screen()

            window_label = ttk.Label(self.root, text="Geben Sie die Fensterfläche an (m2):")
            window_label.grid(row=1, column=0, padx=10, pady=10)

            window_entry = ttk.Entry(self.root)
            window_entry.grid(row=1, column=1, padx=10, pady=10)

            roof_label = ttk.Label(self.root, text="Geben Sie die Dachfläche an (m2):")
            roof_label.grid(row=2, column=0, padx=10, pady=10)

            roof_entry = ttk.Entry(self.root)
            roof_entry.grid(row=2, column=1, padx=10, pady=10)

            door_label = ttk.Label(self.root, text="Geben Sie die Türfläche an (m2):")
            door_label.grid(row=3, column=0, padx=10, pady=10)

            door_entry = ttk.Entry(self.root)
            door_entry.grid(row=3, column=1, padx=10, pady=10)

            kitchen_label = ttk.Label(self.root, text="Geben Sie die Anzahl Küchen an:")
            kitchen_label.grid(row=4, column=0, padx=10, pady=10)

            kitchen_entry = ttk.Entry(self.root)
            kitchen_entry.grid(row=4, column=1, padx=10, pady=10)

            aufzug_label = ttk.Label(self.root, text="Geben Sie die Anzahl Aufzüge an:")
            aufzug_label.grid(row=5, column=0, padx=10, pady=10)

            aufzug_entry = ttk.Entry(self.root)
            aufzug_entry.grid(row=5, column=1, padx=10, pady=10)

            calculate_button = ttk.Button(self.root, text="Berechnen", command=lambda: self.collect_data_and_save(area, volume, property, level, garage, Nebenraum, wohnen, balkon, gewerbe, industrie, window_entry.get(), roof_entry.get(), door_entry.get(), kitchen_entry.get(), aufzug_entry.get()))
            calculate_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

        except Exception as e:
            print(f"Fehler in show_parameter_entry_extra: {e}")

    # Methode zum Sammeln von Daten und Speichern in einer Excel-Datei
    def collect_data_and_save(self, area, volume, property, level, garage, Nebenraum, wohnen, balkon, gewerbe, industrie, window, roof, door, kitchen, aufzug):
        self.data["GF"] = area
        self.data["GV"] = volume
        self.data["Gru_F"] = property
        self.data["Geschossanzahl"] = level
        self.data["Garagenfläche"] = garage
        self.data["Nebenraumfläche"] = Nebenraum
        self.data["Wohnungsfläche"] = wohnen
        self.data["Balkonfläche"] = balkon
        self.data["Gewerbefläche"] = gewerbe
        self.data["Industriefläche"] = industrie
        self.data["Fensterfläche"] = window
        self.data["Dachfläche"] = roof
        self.data["Türfläche"] = door
        self.data["Küchenfläche"] = kitchen
        self.data["Aufzuganzahl"] = aufzug

        # Erstellen Sie einen DataFrame
        df = pd.DataFrame([self.data])

        # Speichern Sie den DataFrame in einer Excel-Datei
        try:
            df.to_excel('Projektdaten.xlsx', index=False)
            print("Daten erfolgreich gespeichert.")
            calculate_costs()  # Annahme: Diese Funktion führt die Kostenberechnung durch
            extra_cost()

        except Exception as e:
            print(f"Fehler beim Speichern der Daten: {e}")

# Hauptprogramm
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
