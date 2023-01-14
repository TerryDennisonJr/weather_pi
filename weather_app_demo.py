# -*- coding: utf-8 -*-
# td_weather_pi app
# 12/24/2022
# Last update: 1/14/2023

# notes for tables; need tablulate module; pip install tabulate

# sites for needed modules:
# numpy and pandas:https://numpy.org/devdocs/user/troubleshooting-importerror.html
# ImageTk:https://github.com/Skiller9090/Lucifer/issues/45:sudo apt-get install python3-pil python3-pil.imagetk
# tabulate:https://bobbyhadz.com/blog/python-install-tabulate#install-tabulate-on-macos-or-linux:sudo pip3 install tabulate

# from sense_hat import SenseHat
from tkinter import *
from tkinter import ttk
import pandas as pd
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tabulate import tabulate
import matplotlib.pyplot as plt
import random

# Creation of main GUI and specifications
main = Tk()
main.title("Weather PI")
main.geometry("1600x800")

# Ceation of form layout with grid format
frm = ttk.Frame(main, padding=10)
frm.grid()

# Creatiion of column labels for Data
ttk.Label(frm, text="Temperature", font=("courier", 30, [
          'bold', 'underline'])).grid(row=0, column=0, padx=75, pady=10)
ttk.Label(frm, text="Humiditiy", font=("courier", 30, [
          'bold', 'underline'])).grid(row=0, column=1, padx=300, pady=10)
ttk.Label(frm, text="Pressure", font=("courier", 30, ['bold', 'underline'])).grid(
    row=0, column=2, padx=150, pady=10)


# Local variables to hold data in labels
temp_val, humi_val, press_val = 13, 28, 810

# Timer function to update data labels
def label_timer():

    # Global variables to hold data in labels
    global temp_val, press_val, humi_val

    temp_val = random.randrange(15, 55)
    humi_val = random.randrange(30, 40)
    press_val = random.randrange(850, 1050)

    # Updates labels with data in miliseconds
    main.after(1000, label_timer)

    # Label to hold data values
    ttk.Label(frm, text=(temp_val,'°F'), font=(
        "courier", 40, 'bold')).grid(row=1, column=0, padx=25)
    ttk.Label(frm, text=humi_val, font=("courier", 40, 'bold')
              ).grid(row=1, column=1, padx=25)
    ttk.Label(frm, text=press_val, font=("courier", 40, 'bold')
              ).grid(row=1, column=2, padx=25)


label_timer()
# Creration of quit button

ttk.Button(frm, text="Quit", width=25, command=lambda: [
           os._exit(0)]).grid(column=2, row=4, pady=500)


# List for the temp, humidity, and pressure values
cumu_temp_values = [temp_val]
temp_data_points = {'Cumulative Temperature': cumu_temp_values}

cumu_humi_values = [humi_val]
humi_data_points = {'Cumulative Humidity': cumu_humi_values}

cumu_press_values = [press_val]
press_data_points = {'Cumulative Pressure': cumu_press_values}


# Timer function to increment list with updated data fro graphs
def graph_timer():
    # High and low tables for temp, humidity, and pressure
    table = [['Low', 'High'],
             [min(cumu_temp_values), max(cumu_temp_values)]]

    table2 = [['Low', 'High'],
             [min(cumu_humi_values), max(cumu_humi_values)]]

    table3 = [['Low', 'High'],
             [min(cumu_press_values), max(cumu_press_values)]]

    # Creation of labels to hold data tables
    ttk.Label(frm, text=tabulate(table), font=("courier", 20, 'bold')
              ).grid(row=3, column=0, padx=25, pady=25)
    ttk.Label(frm, text=tabulate(table2), font=("courier", 20, 'bold')
              ).grid(row=3, column=1, padx=25, pady=25)
    ttk.Label(frm, text=tabulate(table3), font=("courier", 20, 'bold')
              ).grid(row=3, column=2, padx=25, pady=25)

    # Temperature
    cumu_temp_values.append(temp_val)
    temp_data = pd.DataFrame(temp_data_points)
    figure1 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax1 = figure1.add_subplot(111)
    temp_canvas = FigureCanvasTkAgg(figure1, master=main)
    temp_canvas.get_tk_widget().place(relx=.01, rely=.300,)
    temp_data = temp_data[['Cumulative Temperature']]
    temp_data.plot(kind='line', ax=ax1,
                   title="Cumulative Temperature", legend=False)

    # Humidity
    cumu_humi_values.append(humi_val)
    humi_data = pd.DataFrame(humi_data_points)
    figure2 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax2 = figure2.add_subplot(111)
    humi_canvas = FigureCanvasTkAgg(figure2, master=main)
    humi_canvas.get_tk_widget().place(relx=.350, rely=.300,)
    humi_data = humi_data[['Cumulative Humidity']]
    humi_data.plot(kind='line', ax=ax2,
                   title="Cumulative Humidity", color='green', legend=False)

    # Pressure
    cumu_press_values.append(press_val)
    press_data = pd.DataFrame(press_data_points)
    figure3 = plt.Figure(figsize=(4.5, 4), dpi=100)
    ax3 = figure3.add_subplot(111)
    press_canvas = FigureCanvasTkAgg(figure3, master=main)
    press_canvas.get_tk_widget().place(relx=.700, rely=.300,)
    press_data = press_data[['Cumulative Pressure']]
    press_data.plot(kind='line', ax=ax3,
                    title="Cumulative Pressure", color='purple', legend=False)
    # Updates data in graps in miliseconds
    main.after(1000, graph_timer)
    temp_canvas.draw()
    humi_canvas.draw()
    press_canvas.draw()


graph_timer()


# Displays main GUI

main.mainloop()
