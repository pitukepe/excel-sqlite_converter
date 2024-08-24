import pandas as pd
import sqlite3 as sql
import tkinter as tk
from tkinter import filedialog, messagebox

### convert excel file to sqlite database function ###
def convert(filename:str, sheet_name:str, database_name:str, table_name:str):
    ####load excel file into pandas dataframe
    try:
        df = pd.read_excel(filename, sheet_name=sheet_name)
    except Exception as e:
        messagebox.showerror("Error", f"Error occured while loading the excel file: {e}")
        return
    
    ###creating sqlite database
    try:
        conn = sql.connect(database_name)
    except Exception as e:
        messagebox.showerror('Error', f"Error occured while creating the SQLite database: {e}")
        return
    
    ###converting pandas df to sqlite table
    try:
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        messagebox.showinfo("Success", f"Excel file converted to SQLite table {table_name} successfully!")
    except Exception as e:
        messagebox.showerror('Error', f"Error occured while converting the excel file to SQLite table: {e}")
        return
    finally:
        conn.commit()
        conn.close()

    
### run function when button is clicked (if nothing is selected, predefined values in this section are used) ###
def run_import():
    filename = filedialog.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xls *.xlsx")])
    if not filename:
        messagebox.showwarning("Warning", "No file selected")
        return
    sheet_name = sheet_name_entry.get()
    if not sheet_name:
        sheet_name = 'Sheet1'
    database_name = database_name_entry.get()
    table_name = table_name_entry.get()
    if not all([database_name, table_name]):
        messagebox.showwarning("Warning", "Please fill in all fields")
        return
    
    convert(filename, sheet_name, database_name, table_name)


### Create app window ###
#main window
app = tk.Tk()
app.title("Excel to SQLite db Converter")

#labels and entry widgets
tk.Label(app, text="Name of the Excel Sheet:").grid(row=0, column=0, padx=10, pady=5)
sheet_name_entry = tk.Entry(app)
sheet_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(app, text="SQLite Database Name (.db):").grid(row=1, column=0, padx=10, pady=5)
database_name_entry = tk.Entry(app)
database_name_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(app, text="SQLite Table Name:").grid(row=2, column=0, padx=10, pady=5)
table_name_entry = tk.Entry(app)
table_name_entry.grid(row=2, column=1, padx=10, pady=5)

#button to run the conversion
import_button = tk.Button(app, text="Import to SQLite", command=run_import)
import_button.grid(row=3, column=0, columnspan=2, padx=10, pady=20)

#runing the app
app.mainloop()
