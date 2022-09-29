from ast import Delete, If
from asyncio import start_server
from cProfile import label
from cgitb import enable, text
from email import message
from email.errors import StartBoundaryNotFoundDefect
from email.headerregistry import ContentTransferEncodingHeader
from email.mime import image
from faulthandler import disable
from fileinput import filename
from functools import total_ordering
from importlib.resources import path
from lib2to3.pgen2.token import RPAR, TILDE
from msilib.schema import ComboBox, Font
from multiprocessing import parent_process
from operator import index
from os import stat
from re import search
from select import select
from sre_parse import State
import string
import csv
from symtable import symtable
from tarfile import PAX_FIELDS
from datetime import date, datetime
from tkinter import *
from tkinter import ttk
import pandas as pd
import sqlite3
import os, sys
from tkinter import messagebox
from tkinter import commondialog
import tkinter
from fpdf import FPDF
import locale
from tkcalendar import Calendar, DateEntry
from tkinter import font
from tkinter import simpledialog
from tkinter import filedialog
from tkinter.font import BOLD, ITALIC
from turtle import back, bgcolor, left, right, title, update, width
from types import NoneType, new_class
from webbrowser import get
from winreg import QueryInfoKey
from wsgiref import validate
from xml.dom import ValidationErr
from xmlrpc.client import INVALID_ENCODING_CHAR, FastParser


root = Tk()
root.title('Caja Diaria y Contabilidad')
root.resizable(0,0)
try:
    root.iconbitmap('img\codemy.ico')
except:
    messagebox.showerror(title="Ups..Ups..", message="¡Error! No se encuentra la carpeta con imágenes [img] dentro del directorio del programa.")
#root.geometry("914x536")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

w = 914
h = 536

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

db_name = 'db/Contabilidad_db.db'

# Add Some Style
style = ttk.Style(root)

# Pick A Theme
style.theme_use('vista')

style.configure("title.TLabel", font=("Arial",32, BOLD))
style.configure("subtitle.TLabel", font=("Arial", 20,BOLD))
style.configure("ttk.TButton", font=("Arial",20, BOLD))
style.configure("mainPage.TButton", font=("Arial",18, BOLD), foreground="#1A1A40")
style.configure("conceptosPage.TButton", font=("Arial",16, BOLD), foreground="#395B64")
style.configure("cuentasPage.TButton", font=("Arial",16, BOLD), foreground="#774360")
style.configure("main.TButton", font=("Arial",15, BOLD))
style.configure("TNotebook.Tab", font=("Arial",15, BOLD), foreground="#A4A4A4")
style.map("TNotebook.Tab", font=[("selected", ("Arial",15, BOLD))], foreground=[("selected", "#000000")])
style.configure("style_data.TLabel", font=("Arial", 13,BOLD), background="#BDBDBD")
style.configure("style_tdata.TLabel", font=("Arial", 16,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("companyData.TLabel", font=("Arial", 15,BOLD), background="#BDBDBD")
style.configure("companyDataTitle.TLabel", font=("Arial", 15,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("balance.TLabel", font=("Arial", 14,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("conceptos.TLabel", font=("Arial", 16,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("cuentas.TLabel", font=("Arial", 16,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("movimientos.TLabel", font=("Arial", 16,BOLD), background="#1C1C1C", foreground="#FFFFFF")
style.configure("button.TButton", font=("Arial", 18,BOLD))
style.configure("cuentas.TButton", font=("Arial", 16,BOLD))
style.configure("mov_caja.TLabel", font=("Arial", 13,BOLD))
style.configure("mov_cajat.TLabel", font=("Arial", 18,BOLD))
style.configure("TEntry", font=("Arial", 13, BOLD), backgroud="#538cc6")
style.configure("totaltitle.TLabel", font=("Arial", 13, BOLD))

maintitlelabel = ttk.Label(root, text="Caja Diaria y Contabilidad", foreground="#2C3639",style='title.TLabel')
maintitlelabel.pack()
subtitlelabel = ttk.Label(root, text="-", foreground="#3F4E4F",style='subtitle.TLabel')
subtitlelabel.pack()
separator_title = ttk.Separator(root, orient='horizontal')
separator_title.pack(fill='x')

notebook_main = ttk.Notebook(root)
notebook_main.pack(fill='x')

data_entry_frame = ttk.Frame(notebook_main, width=400, height=320)
concepto_report_frame = ttk.Frame(notebook_main, width=400, height=320)
cuenta_report_frame = ttk.Frame(notebook_main, width=400, height=320)

#Button Fuction

def company_data():
    #create and customize frame
    company_data_frame = Toplevel()
    company_data_frame.grab_set()
    company_data_frame.resizable(0,0)
    company_data_frame.iconbitmap('img\codemy.ico')
    company_data_frame.title("Datos de la Empresa")
    w = 716
    h = 233

    ws = company_data_frame.winfo_screenwidth()
    hs = company_data_frame.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    company_data_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #Edit function
    def edit_data():
        if company_name_entry.get() == "" or address_entry.get() == "" or tel_entry.get() == "": 
            messagebox.showerror(title="Ups..Ups..", message="¡Los campos [Nombre de la Empresa], [Domicilio Completo] y [Teléfono] son obligatorios y no pueden estar vacíos!", parent= company_data_frame)
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            company_name = company_name_entry.get()
            address_c = address_entry.get()
            tel_c = tel_entry.get()


            c.execute("""UPDATE Datos_Empresa SET 
                                NOMBRE_EMPRESA = :name,
                                DOMICILIO = :addr,
                                TELEFONO = :tel""", {
                                    'name' : company_name,
                                    'addr' : address_c,
                                    'tel' : tel_c
                                })

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()
            messagebox.showinfo(title="Datos Modificados", message="Se han modificado los Datos de la Empresa", parent= company_data_frame)

    def exitData():
        close_window()
        company_data_frame.destroy()


    #close without saving function
    def close_window():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO, TELEFONO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]
        tel = records[2]

        # Commit changes
        conn.commit()
		# Close our connection
        conn.close()

        if company_name != company_name_entry.get() or address != address_entry.get() or tel != tel_entry.get():
            response = messagebox.askyesno(title="Cerrar ventana", message="¡No se han guardado los cambios! ¿Guardar modificaciones?", parent=company_data_frame)
            if response:
                edit_data()
                company_data_frame.destroy()
            else:
                company_data_frame.destroy()
        else:
            company_data_frame.destroy()
                
    #Entry boxes validation
    def only_text(inp):
        if len(inp) > 50:
            return False
        elif inp == "":
            return True
        elif inp == " ":
            return False
        elif " " in inp:
            return True
        elif inp.isalnum():
            return True
        else:
            return False

    def only_number_tel(inp):
        if len(inp) > 15:
            return False
        elif inp.isdigit():
            return True
        elif inp == "":
            return True
        else:
            return False

    only_text_validation = root.register(only_text)
    only_number_validation = root.register(only_number_tel)

    #Manage close window without saving
    company_data_frame.protocol("WM_DELETE_WINDOW", close_window)


    #Entry boxes and label
    company_name_label = ttk.Label(company_data_frame, text="Nombre de la Empresa", style='companyDataTitle.TLabel', width=61, borderwidth=2, relief="solid")
    company_name_label.place(x=21, y=18)
    company_name_entry = ttk.Entry(company_data_frame, font=("Arial", 15), width=61)
    company_name_entry.config(validate="key", validatecommand=(only_text_validation, '%P'))
    company_name_entry.place(x=20, y=44)

    address_label = ttk.Label(company_data_frame, text="Domicilio Completo", style='companyData.TLabel', width=61, borderwidth=2, relief="solid")
    address_label.place(x=21, y=88)
    address_entry = ttk.Entry(company_data_frame, font=("Arial", 15), width=61)
    address_entry.config(validate="key", validatecommand=(only_text_validation, '%P'))
    address_entry.place(x=20, y=114)

    tel_label = ttk.Label(company_data_frame, text="Teléfono", style='companyData.TLabel', width=30, borderwidth=2, relief="solid")
    tel_label.place(x=21, y=158)
    tel_entry = ttk.Entry(company_data_frame, font=("Arial", 15), width=30)
    tel_entry.config(validate="key", validatecommand=(only_number_validation, '%P'))
    tel_entry.place(x=20, y=184)

    #edit Button
    modificar_btn = ttk.Button(company_data_frame, text="Editar", style='button.TButton', command=edit_data)
    modificar_btn.place(x=371, y=165)

    exit_btn = ttk.Button(company_data_frame, text="Salir", style='button.TButton', command=exitData)
    exit_btn.place(x=541, y=165)


    #add data to entry function
    def add_data():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO, TELEFONO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]
        tel = records[2]
        
        company_name_entry.insert(0, company_name)
        address_entry.insert(0, address)
        tel_entry.insert(0, tel)

        # Commit changes
        conn.commit()
		# Close our connection
        conn.close()

    add_data()

def concepts():
    #create and customize frame
    concepts_frame = Toplevel()
    concepts_frame.grab_set()
    concepts_frame.resizable(0,0)
    concepts_frame.iconbitmap('img\codemy.ico')
    concepts_frame.title("Administrar Conceptos")
    w = 753
    h = 646

    ws = concepts_frame.winfo_screenwidth()
    hs = concepts_frame.winfo_screenheight()

    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    concepts_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Configure the Treeview Colors
    style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3", font=("Arial", 14))

    style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

    # Change Selected Color
    style.map('Treeview',
        background=[('selected', "#347083")])

    # Create a Treeview Frame
    tree_frame = Frame(concepts_frame)
    #tree_frame.pack(pady=10)
    tree_frame.place(x=10, y=150)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame, width=20)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=15)
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("ID_CONCEPTO", "NOMBRE_CONCEPTO")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID_CONCEPTO", width=0, stretch=NO)
    my_tree.column("NOMBRE_CONCEPTO", anchor=W, width=720)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID_CONCEPTO", text="", anchor=W)
    my_tree.heading("NOMBRE_CONCEPTO", text="Concepto", anchor=W)

    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#A5C9CA")

    # Create a database or connect to one that exists
    conn = sqlite3.connect(db_name)

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
    records = c.fetchone()

    company_name = records[0]
    address = records[1]

    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()

    #clean table function
    def clean_table():
        for item in my_tree.get_children():
            my_tree.delete(item)

    #add concepts to treeview
    def add_conceptos():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT ID_CONCEPTO, NOMBRE_CONCEPTO FROM Conceptos")

        records = c.fetchall()
       
        clean_table()
        # Add our data to the screen
        global count
        count = 0

        for record in records:
            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('oddrow',))
            # increment counter
            count += 1

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()
    
    #execute function
    add_conceptos()

    #search concepts in db
    def search_concept():
        id_concept_entry.delete(0, END)
        addConcepto_label.place_forget()
        if search_concept_entry.get() == "":
            add_conceptos()
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            concept_search = "%" + search_concept_entry.get() + "%"

            c.execute("""SELECT ID_CONCEPTO, NOMBRE_CONCEPTO FROM Conceptos WHERE NOMBRE_CONCEPTO LIKE :concept""",{'concept': concept_search})

            records = c.fetchall()

            # Add our data to the screen
            global count
            count = 0

            clean_table()

            for record in records:
                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1]), tags=('oddrow',))
                # increment counter
                count += 1

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

    #clean search function
    def clean_search():
        id_concept_entry.delete(0, END)
        addConcepto_label.place_forget()
        add_conceptos()
        search_concept_entry.delete(0, END)
        search_concept_entry.focus()

    #Create concept validation input
    def only_text(inp):
        if len(inp) > 40:
            return False
        elif inp == "":
            return True
        elif inp == " ":
            return False
        elif " " in inp:
            return True
        elif inp.isalnum():
            return True
        else:
            return False

    only_text_validation = root.register(only_text)  

    #Funciones de Texto temporal Entry Search
    def temp_text_concepto(e):
        search_concept_entry.delete(0, END)
        search_concept_entry.config(font=("Arial", 16), foreground="black")


    def temp_text_add_concepto(e):
        if search_concept_entry.get() == "":
            search_concept_entry.delete(0, END)
            search_concept_entry.insert(0, "Buscar Concepto...")
            search_concept_entry.config(foreground="grey")


    def searchBind(e):
        search_concept()

    def cleanSearchBind(e):
        clean_search()

    #Entry boxes and label
    search_concept_entry = ttk.Entry(concepts_frame, font=("Arial", 16), width=23)
    search_concept_entry.config(validate="key", validatecommand=(only_text_validation, "%P"))
    search_concept_entry.config(foreground="grey")
    search_concept_entry.insert(0, "Buscar Concepto...")
    search_concept_entry.place(x=11, y=100, height=36)

    search_concept_entry.bind("<Return>", searchBind)
    search_concept_entry.bind("<Escape>", cleanSearchBind)
    search_concept_entry.bind("<FocusIn>", temp_text_concepto)
    search_concept_entry.bind("<FocusOut>", temp_text_add_concepto)

    window_label = ttk.Label(concepts_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Gestionar Conceptos")
    window_label.place(x=10, y=5)
    title_name_label = ttk.Label(concepts_frame, foreground="#000000", style="mov_cajat.TLabel")
    title_name_label.place(x=10, y=35)
    address_label = ttk.Label(concepts_frame, foreground="#808080", style="mov_caja.TLabel")
    address_label.place(x=10, y=65)

    title_name_label.config(text=company_name)
    address_label.config(text=address)

    search_concept_btn = ttk.Button(concepts_frame, text="Buscar", style='button.TButton', command=search_concept)
    search_concept_btn.place(x=310, y=98)
    clean_search_btn = ttk.Button(concepts_frame, text="X", width=4, style='button.TButton', command=clean_search)
    clean_search_btn.place(x=470, y=98)

    #add concept function
    def add_new_concept():
        if concepts_entry.get() == "":
            messagebox.showerror(title="Ups..Ups..", message="¡El campo [Nuevo Concepto] no debe estar vacío!", parent= concepts_frame)
        else:
            try:
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)

                # Create a cursor instance
                c = conn.cursor()

                concept_name = (concepts_entry.get()).upper()
                
                sql_add = "INSERT INTO Conceptos (EMPRESA, NOMBRE_CONCEPTO) VALUES (?,?)"
                sql_args = (1, concept_name)
                c.execute(sql_add, sql_args)

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                concepts_entry.delete(0, END) 
                add_conceptos()
                addConcepto_label.place(x=299, y=558)
            except:
                messagebox.showerror(title="Ups..Ups..", message="¡Ya existe un concepto con ese nombre! Seleccione otro.", parent= concepts_frame)
                concepts_entry.delete(0, END) 

    #focus selected function
    def selected(e):
        selected_filter = my_tree.focus()
        if selected_filter != "":
            # Grab record Number
            selected = my_tree.focus()
            # Grab record values
            values = my_tree.item(selected, 'values')
            id_concept_entry.delete(0, END)
            name_concept_entry.delete(0, END)

            # output to entry boxes
            id_concept_entry.insert(0, values[0])
            name_concept_entry.insert(0, values[1])
            addConcepto_label.place_forget()

    def conceptBind(e):
        add_new_concept()

    def conceptDelBind(e):
        concepts_entry.delete(0, END)

    def deleteLabeladd(e):
        addConcepto_label.place_forget()

    #Bind the treeview
    my_tree.bind("<ButtonRelease-1>", selected)


    #entryboxes for selected and create concept
    addConcepto_label = ttk.Label(concepts_frame, text="¡Concepto Agregado!", font=("Arial", 16, BOLD), anchor="n", foreground="red")
    addConcepto_label.place_forget()

    id_concept_entry = ttk.Entry(concepts_frame)
    name_concept_entry = ttk.Entry(concepts_frame)
    concepts_label = ttk.Label(concepts_frame, text="Nuevo Concepto", style='conceptos.TLabel', width=23, borderwidth=2, relief="solid", anchor="center")
    concepts_label.place(x=11, y=563)
    concepts_entry = ttk.Entry(concepts_frame, font=("Arial", 16), width=23)
    concepts_entry.config(validate="key", validatecommand=(only_text_validation, '%P'))
    concepts_entry.place(x=11, y=591, height=36)
    concepts_entry.bind("<Return>", conceptBind)
    concepts_entry.bind("<Escape>", conceptDelBind)
    concepts_entry.bind("<Key>", deleteLabeladd)

    #Revisar esto
    def del_concept():
        addConcepto_label.place_forget()
        if id_concept_entry.get() == "":
            messagebox.showerror(title="Ups..Ups..", message="¡Debe seleccionar un registro del listado primero!", parent=concepts_frame)     
        else: 
            concepto_id = id_concept_entry.get()
            concepto_name = name_concept_entry.get()
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            
            # Create a cursor instance
            c = conn.cursor()

            concept_del_list = c.execute("""SELECT ID_MOVIMIENTO FROM Movimientos WHERE CONCEPTO = :name""",{ 'name': concepto_name})
            concept_del_list = c.fetchone()
            if concept_del_list == None:
                confirmation = messagebox.askquestion(title="Eliminar Concepto", message="¿Está seguro que desea eliminar el concepto [" + concepto_name + "]?", parent=concepts_frame)
                if confirmation == 'yes':
                    query_del = "DELETE FROM Conceptos WHERE ID_CONCEPTO = ?"
                    args_del = (concepto_id)
                    c.execute(query_del, [args_del])
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
                    add_conceptos() 
                    messagebox.showinfo(title="Eliminar concepto", message="¡Concepto Eliminado con Éxito!", parent=concepts_frame)
                    id_concept_entry.delete(0, END)        
                    
            else: 
                messagebox.showerror(title="Ups..Ups..", message="El concepto se encuentra relacionado con el movimiento de caja N° " + str(concept_del_list[0]) + ". ¡Elimine el movimiento e intente nuevamente!", parent= concepts_frame)      
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
        

    def exit_concept():
        concepts_frame.destroy()

    #Create buttons
    add_concepto_btn = ttk.Button(concepts_frame, text="Agregar", width=8,style='button.TButton', command=add_new_concept)
    add_concepto_btn.place(x=301, y=589)
    del_concept_btn = ttk.Button(concepts_frame, text="Eliminar", width=8, style='button.TButton', command=del_concept)
    del_concept_btn.place(x=424, y=589)
    exit_concept_btn = ttk.Button(concepts_frame, text="Salir", width=12, style='button.TButton', command=exit_concept)
    exit_concept_btn.place(x=570, y=589)

def cuentas_adm():
    cuentas_frame = Toplevel()
    cuentas_frame.grab_set()
    cuentas_frame.resizable(0,0)
    cuentas_frame.iconbitmap('img\codemy.ico')
    cuentas_frame.title("Administrar Cuentas")

    ws = cuentas_frame.winfo_screenwidth()
    hs = cuentas_frame.winfo_screenheight()

    if ws == 1366 and hs == 768:
        cuentas_frame.state('zoomed')
    else:
        w = 1366
        h = 768

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        cuentas_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        

    # Configure the Treeview Colors
    style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3", font=("Arial", 14))

    style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

    # Change Selected Color
    style.map('Treeview',
        background=[('selected', "#B25068")])

    # Create a Treeview Frame
    tree_frame = Frame(cuentas_frame)
    #tree_frame.pack(pady=10)
    tree_frame.place(x=10, y=155)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame, width=20)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=15)
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("ID_CUENTA", "COD_CUENTA", "NOMBRE_CUENTA", "SALDO_ACTUAL", "DESCRIPCION")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID_CUENTA", width=0, stretch=NO)
    my_tree.column("COD_CUENTA", anchor=W, width=115)
    my_tree.column("NOMBRE_CUENTA", anchor=W, width=570)
    my_tree.column("SALDO_ACTUAL", anchor=W, width=150)
    my_tree.column("DESCRIPCION", anchor=W, width=495)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID_CUENTA", text="", anchor=W)
    my_tree.heading("COD_CUENTA", text="Código", anchor=W)
    my_tree.heading("NOMBRE_CUENTA", text="Nombre de Cuenta", anchor=W)
    my_tree.heading("SALDO_ACTUAL", text="Saldo Actual", anchor=W)
    my_tree.heading("DESCRIPCION", text="Descripción", anchor=W)

    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#e0b8c2")

    def clean_table():
        for item in my_tree.get_children():
            my_tree.delete(item)

    def add_cuentas():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT ID_CUENTA, COD_CUENTA, NOMBRE_CUENTA, DESCRIPCION FROM Cuentas ORDER BY COD_CUENTA ASC")

        records = c.fetchall()
       
        clean_table()
        # Add our data to the screen
        global count
        count = 0


        for record in records:
            c.execute("""SELECT IFNULL(SUM(DEBE), 0.0), IFNULL(SUM(HABER), 0.0) FROM Movimientos WHERE ID_CUENTA = :idCuenta""", {'idCuenta': record[0]})
            saldoActual = c.fetchone()
            totalActual = round(saldoActual[0] - saldoActual[1],2)

            trans = str.maketrans('.,', ',.')
            totalActual = str(format(totalActual, ',.2f').translate(trans))

            if totalActual == "0,00":
                totalActual = ""


            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], totalActual, record[3]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], totalActual, record[3]), tags=('oddrow',))
            # increment counter
            count += 1

        my_tree.yview_moveto('1.0')
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

    add_cuentas()

    window_label = ttk.Label(cuentas_frame, foreground="#774360", style="mov_cajat.TLabel", text="Gestionar Cuentas")
    window_label.place(x=10, y=5)
    title_name_label = ttk.Label(cuentas_frame, foreground="#000000", style="mov_cajat.TLabel")
    title_name_label.place(x=10, y=35)
    address_label = ttk.Label(cuentas_frame, foreground="#808080", style="mov_caja.TLabel")
    address_label.place(x=10, y=65)

    # Create a database or connect to one that exists
    conn = sqlite3.connect(db_name)

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
    records = c.fetchone()

    company_name = records[0]
    address = records[1]

    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()

    def update_data():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT SUM(DEBE) FROM Movimientos")
        records = c.fetchone()

        if records[0] == None:
            total_debe = 0.00
        else:
            total_debe = records[0]

        c.execute("SELECT SUM(HABER) FROM Movimientos")
        records = c.fetchone()

        if records[0] == None:
            total_haber = 0.00
        else:
            total_haber = records[0]

        total_debe_haber = (total_debe - total_haber)
        trans = str.maketrans('.,', ',.')
        total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)
        
        total_entry.config(state="normal")
        total_entry.delete(0, END)
        total_entry.insert(0, "$ " + total_debe_haber)
        total_entry.config(state="readonly")
        
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

    def clear_entry():
        # Configure id_entry in state Normal
        saldoActual_entry.config(state="normal")
        # Clear entry boxes
        idCuenta_entry.delete(0, END)
        codCuenta_entry.delete(0, END)
        nombreCuenta_entry.delete(0, END)
        saldoActual_entry.delete(0, END)
        descripcion_entry.delete(0, END)
        # Configure id_entry in readonly
        saldoActual_entry.config(state="readonly")


    #Select Record
    def select_record(e):
        selected_filter = my_tree.focus()
        if selected_filter != "":
            filter = my_tree.item(selected_filter, 'values')
            if filter[0] != "Totales" and selected_filter != "":	 
                #Enable again add_init_button
                add_cuenta_btn.config(state="disable")
                new_cuenta_btn.config(state="normal")
                edit_cuenta_btn.config(state="normal")
                del_cuenta_btn.config(state="normal")
                # Configure id_entry in state Normal
                saldoActual_entry.config(state="normal")
                # Clear entry boxes
                idCuenta_entry.delete(0, END)
                codCuenta_entry.delete(0, END)
                nombreCuenta_entry.delete(0, END)
                saldoActual_entry.delete(0, END)
                descripcion_entry.delete(0, END)
                
                

                # Grab record Number
                selected = my_tree.focus()
            

                # Grab record values
                values = my_tree.item(selected, 'values')

                # output to entry boxes
                idCuenta_entry.insert(0, values[0])
                codCuenta_entry.insert(0, values[1])
                nombreCuenta_entry.insert(0, values[2])
                saldoActual_entry.insert(0, str(values[3]).replace('.',''))
                descripcion_entry.insert(0, values[4])

                # Configure id_entry in readonly
                saldoActual_entry.config(state="readonly")
                editCuenta_label.place_forget()
                nombreCuenta_entry.focus()




    def add_new_cuenta():
        try:
            if codCuenta_entry.get() == "" or nombreCuenta_entry.get() == "":
                messagebox.showerror(title="Ups..Ups..", message="¡Los campos [Código] y [Nombre] son obligatorios para crear una cuenta!", parent=cuentas_frame)
            else:
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)

                # Create a cursor instance
                c = conn.cursor()
                
                nombreCuenta = nombreCuenta_entry.get().upper()
                codCuenta = codCuenta_entry.get()
                descCuenta = descripcion_entry.get()

                sql_add = "INSERT INTO Cuentas (COD_CUENTA, NOMBRE_CUENTA, DESCRIPCION) VALUES (?, ?, ?)"
                sql_add_args = (codCuenta, nombreCuenta, descCuenta)

                c.execute(sql_add, sql_add_args)

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()

                new_cuenta_btn.config(state="normal")
                add_cuenta_btn.config(state="disable")
                clear_entry()
                add_cuentas()
                update_data()
                messagebox.showinfo(title="Cuenta Agregada", message="¡Nueva Cuenta creada con éxito!", parent= cuentas_frame)
        except:
            cod = codCuenta_entry.get()
            c.execute("SELECT COD_CUENTA, NOMBRE_CUENTA FROM Cuentas WHERE COD_CUENTA = :cod_input", {'cod_input': cod})
            cuenta_repeat = c.fetchone()
            cuenta = str(cuenta_repeat[0])
            name = cuenta_repeat[1]
            messagebox.showerror(title="Ups.. Ups..", message="El Código de cuenta ya existe en la cuenta [" + cuenta + " - " + name + "]", parent= cuentas_frame)
            conn.close()
            


    def clean_search_bind(e):
        search_entry_name.delete(0, END)
        search_entry_cod.delete(0, END)
        add_cuentas()
        search_entry_cod.delete(0, END)
        search_entry_cod.insert(0, "Buscar Código...")
        search_entry_cod.config(foreground="grey")
        search_entry_name.focus()


    def clean_search():
        search_entry_name.delete(0, END)
        search_entry_cod.delete(0, END)
        add_cuentas()
        search_entry_cod.delete(0, END)
        search_entry_cod.insert(0, "Buscar Código...")
        search_entry_cod.config(foreground="grey")
        search_entry_name.focus()	


    def edit_cuenta():
        try:
            if codCuenta_entry.get() == "" or nombreCuenta_entry.get() == "":
                messagebox.showerror(title="Ups..Ups..", message="¡Los campos [Código] y [Nombre] son obligatorios!", parent=cuentas_frame)
            else:
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)

                # Create a cursor instance
                c = conn.cursor()

                nombreCuenta = nombreCuenta_entry.get().upper()
                codCuenta = codCuenta_entry.get()
                descCuenta = descripcion_entry.get()

                c.execute("""UPDATE Cuentas SET
                    COD_CUENTA = :codCuenta,
                    NOMBRE_CUENTA = :nombre,
                    DESCRIPCION = :desc
                    WHERE ID_CUENTA = :oid""",
                {
                    'codCuenta': codCuenta,
                    'nombre': nombreCuenta,
                    'desc': descCuenta,
                    'oid': idCuenta_entry.get()
                })

                c.execute("""UPDATE Movimientos SET
                    CUENTA = :nombre
                    WHERE ID_CUENTA = :oid""",
                {
                    'nombre': nombreCuenta,
                    'oid': idCuenta_entry.get()
                })

                # Commit changes
                conn.commit()

                #Ejecuto función para que limpie las casillas y recarguen nuevamente los socios
                clear_entry()
                clean_search()
                add_cuentas()

                # Close our connection
                conn.close()
                editCuenta_label.place(x=924, y=640)
        except:
             cod = codCuenta_entry.get()
             c.execute("SELECT COD_CUENTA, NOMBRE_CUENTA FROM Cuentas WHERE COD_CUENTA = :cod_input", {'cod_input': cod})
             cuenta_repeat = c.fetchone()
             cuenta = str(cuenta_repeat[0])
             name = cuenta_repeat[1]
             messagebox.showerror(title="Ups.. Ups..", message="El Código de cuenta ya existe en la cuenta [" + cuenta + " - " + name + "]", parent= cuentas_frame)
             conn.close()


    #Delete socios function
    def del_cuenta():
        if idCuenta_entry.get() == "":
            messagebox.showerror(message="Debe seleccionar un [SOCIO] de la tabla primero!", title="Ups.. Ups..", parent=cuentas_frame)
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            idCuenta = idCuenta_entry.get()
            codCuenta = codCuenta_entry.get()
            nameCuenta = nombreCuenta_entry.get()

            del_cuenta = c.execute("""SELECT ID_MOVIMIENTO FROM Movimientos WHERE ID_CUENTA = :oid""", {'oid': idCuenta})
            del_cuenta = c.fetchone()

            if del_cuenta == None:
                confirmation = messagebox.askquestion(title="Eliminar Cuenta", message="¿Está seguro que desea eliminar la cuenta N° [" + codCuenta + " - " + nameCuenta + "]?", parent=cuentas_frame)
                if confirmation == 'yes':
                    query_del = "DELETE FROM Cuentas WHERE ID_CUENTA = ?"
                    args_del = (idCuenta)
                    c.execute(query_del, [args_del])

                    #Commit changes
                    conn.commit()

                    #Clear Entry Boxes
                    clear_entry()
                    add_cuentas()

                    #Clouse out connection
                    conn.close()
                    messagebox.showinfo(title="Eliminar Cuenta", message="¡Cuenta Eliminada con Éxito!", parent=cuentas_frame)
                else:
                    #Clouse out connection
                    conn.close()
            else:
                messagebox.showerror(title="Ups..Ups..", message="La cuenta se encuentra relacionado con el movimiento de caja N° " + str(del_cuenta[0]) + ". ¡Elimine el movimiento e intente nuevamente!", parent=cuentas_frame)      
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()


    #Search Socio function
    def search_cuentas():
        editCuenta_label.place_forget()
        if str(search_entry_name.get()) == "Buscar Nombre..." and str(search_entry_cod.get()) == "Buscar Código...":
            messagebox.showerror(title="Ups.. Ups..", message="Los campos [Buscar Nombre...] y [Buscar Código...] se encuentran vacíos", parent=cuentas_frame)
        else:
            if search_entry_cod.get() == "Buscar Código..." or search_entry_cod.get() == "":
                cod_cuenta_search = "%"
            else:
                cod_cuenta_search = search_entry_cod.get() + "%"
			

            if search_entry_name.get() == "Buscar Nombre..." or search_entry_name.get() == "":
                nombre_search = "%"
            else:
                nombre_search = "%" + search_entry_name.get() + "%"

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            clean_table()
            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT ID_CUENTA,
					    COD_CUENTA,
					    NOMBRE_CUENTA,
                        DESCRIPCION FROM Cuentas WHERE COD_CUENTA LIKE :cod_cuenta AND NOMBRE_CUENTA like :nombre ORDER BY COD_CUENTA ASC""",
						{
						'cod_cuenta': cod_cuenta_search,
						'nombre': nombre_search
						})

            records = c.fetchall()

            # Add our data to the screen
            global count
            count = 0

            for record in records:
                c.execute("""SELECT IFNULL(SUM(DEBE), 0.0), IFNULL(SUM(HABER), 0.0) FROM Movimientos WHERE ID_CUENTA = :idCuenta""", {'idCuenta': record[0]})
                saldoActual = c.fetchone()
                totalActual = round(saldoActual[0] - saldoActual[1],2)

                trans = str.maketrans('.,', ',.')
                totalActual = str(format(totalActual, ',.2f').translate(trans))

                if totalActual == "0,00":
                    totalActual = ""

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], totalActual, record[3]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], totalActual, record[3]), tags=('oddrow',))
                # increment counter
                count += 1

            # Commit changes
            conn.commit()

            # Close our connection
            conn.close()


    def new_cuenta():
        clear_entry()
        edit_cuenta_btn.config(state="disable")
        add_cuenta_btn.config(state="normal")
        del_cuenta_btn.config(state="disable")
        new_cuenta_btn.config(state="disable")
        codCuenta_entry.focus()
        editCuenta_label.place_forget()



    title_name_label.config(text=company_name)
    address_label.config(text=address)

    #Funciones de Texto temporal Entry Search
    def temp_text_nombre(e):
        search_entry_name.delete(0, END)
        search_entry_name.config(font=("Arial", 16), foreground="black")


    def temp_text_add_nombre(e):
        if search_entry_name.get() == "":
            search_entry_name.delete(0, END)
            search_entry_name.insert(0, "Buscar Nombre...")
            search_entry_name.config(foreground="grey")

	#Funciones de Texto temporal Entry Search
    def temp_text_cod(e):
        search_entry_cod.delete(0, END)
        search_entry_cod.config(font=("Arial", 16), foreground="black")


    def temp_text_add_cod(e):
        if search_entry_cod.get() == "":
            search_entry_cod.delete(0, END)
            search_entry_cod.insert(0, "Buscar Código...")
            search_entry_cod.config(foreground="grey")


    def only_number_cod(inp):
            if len(inp) > 8:
                return False
            elif inp.isdigit():
                return True
            elif inp == "":
                return True
            else:
                return False


    def only_text_name(inp):
        if len(inp) > 40:
            return False
        elif inp.isalnum():
            return True
        elif inp == "":
            return True
        elif inp.isspace():
            return False
        elif ' ' in inp:
            return True
        elif '.' in inp:
            return True
        elif '-' in inp:
            return True
        else:
            return False

    def only_text_obs(inp):
        if len(inp) > 80:
            return False
        elif inp.isalnum():
            return True
        elif inp == "":
            return True
        elif inp.isspace():
            return False
        elif ' ' in inp:
            return True
        elif '.' in inp:
            return True
        elif '-' in inp:
            return True
        else:
            return False


    #Register the functions to validate entry   	
    cod_validation = root.register(only_number_cod)
    name_validation = root.register(only_text_name)
    obs_validation = root.register(only_text_obs)

    #Create entry and buttons in search frame.
    search_entry_cod = ttk.Entry(cuentas_frame, font= ("Arial", 16), foreground="grey")
    search_entry_cod.insert(0, "Buscar Código...")
    search_entry_cod.config(validate="key", validatecommand=(name_validation, "%P"))
    search_entry_cod.place(x=10,y=105, width=190, height=36)

    search_entry_name = ttk.Entry(cuentas_frame, font= ("Arial", 16), foreground="grey")
    search_entry_name.insert(0, "Buscar Nombre...")
    search_entry_name.config(validate="key", validatecommand=(name_validation, "%P"))
    search_entry_name.place(x=220,y=105, width=190, height=36)

    search_btn = ttk.Button(cuentas_frame, text="Buscar", style='button.TButton', command=search_cuentas)
    search_btn.place(x=430, y=104)
    clean_search_btn = ttk.Button(cuentas_frame, text="X", style='button.TButton', command=clean_search, width=5)
    clean_search_btn.place(x=600, y=104)

    def search_log_bind(e):
        search_cuentas()

	#Bind events in search entry
    search_entry_name.bind("<FocusIn>", temp_text_nombre)
    search_entry_name.bind("<FocusOut>", temp_text_add_nombre)
    search_entry_name.bind("<Return>", search_log_bind)
    search_entry_name.bind("<Escape>", clean_search_bind)
    search_entry_cod.bind("<FocusIn>", temp_text_cod)
    search_entry_cod.bind("<FocusOut>", temp_text_add_cod)
    search_entry_cod.bind("<Return>", search_log_bind)
    search_entry_cod.bind("<Escape>", clean_search_bind)

    #Bind the treeview for select
    my_tree.bind("<ButtonRelease-1>", select_record)


    editCuenta_label = ttk.Label(cuentas_frame, text="¡Cuenta modificada con Éxito!", font=("Arial", 15, BOLD), anchor="n", foreground="red")
    editCuenta_label.place_forget()

    total_label = ttk.Label(cuentas_frame, text="Saldo Total", style='cuentas.TLabel', anchor="n", width=12)
    total_label.place(x=1027, y=115, height=26)
    total_entry = Entry(cuentas_frame, font=("Arial", 16, BOLD), width=14)
    total_entry.config(state="readonly")
    total_entry.place(x=1170, y=115, height=26)

    idCuenta_entry = ttk.Entry(cuentas_frame)


    codCuenta_label = ttk.Label(cuentas_frame, text="Código", style='cuentas.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
    codCuenta_label.place(x=11, y=595, height=36)
    codCuenta_entry = ttk.Entry(cuentas_frame, font=("Arial", 16), width=12)
    codCuenta_entry.config(validate="key", validatecommand=(cod_validation, "%P"))
    codCuenta_entry.place(x=130, y=595, height=36)

    nombreCuenta_label = ttk.Label(cuentas_frame, text="Nombre", style='cuentas.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
    nombreCuenta_label.place(x=310, y=595, height=36)
    nombreCuenta_entry = ttk.Entry(cuentas_frame, font=("Arial", 16), width=45)
    nombreCuenta_entry.config(validate="key", validatecommand=(name_validation, "%P"))
    nombreCuenta_entry.place(x=424, y=595, height=36)

    saldoActual_label = ttk.Label(cuentas_frame, text="Saldo Actual", style='cuentas.TLabel', width=12, borderwidth=2, relief="solid", anchor="center")
    saldoActual_label.place(x=1000, y=595, height=36)
    saldoActual_entry = ttk.Entry(cuentas_frame, font=("Arial", 16), width=12)
    saldoActual_entry.config(state="readonly")
    saldoActual_entry.place(x=1147, y=595, height=36)

    descripcion_label = ttk.Label(cuentas_frame, text="Descripción", style='cuentas.TLabel', width=13, borderwidth=2, relief="solid", anchor="center")
    descripcion_label.place(x=11, y=655, height=56)
    descripcion_entry = ttk.Entry(cuentas_frame, font=("Arial", 16), width=25)
    descripcion_entry.config(validate="key", validatecommand=(obs_validation, "%P"))
    descripcion_entry.place(x=169, y=655, height=56)

    
    update_data()

    def exit_cuenta():
        cuentas_frame.destroy()

    new_cuenta_btn = ttk.Button(cuentas_frame, text="+", style='button.TButton', command=new_cuenta, width=4)
    new_cuenta_btn.place(x=525, y=675)
    new_cuenta_btn.config(state="disable")
    add_cuenta_btn = ttk.Button(cuentas_frame, text="Agregar", style='button.TButton', command=add_new_cuenta)
    add_cuenta_btn.place(x=615, y=675)
    del_cuenta_btn = ttk.Button(cuentas_frame, text="Eliminar", style='button.TButton', command=del_cuenta)
    del_cuenta_btn.place(x=805, y=675)
    del_cuenta_btn.config(state="disable")
    edit_cuenta_btn = ttk.Button(cuentas_frame, text="Editar", style='button.TButton', command=edit_cuenta)
    edit_cuenta_btn.place(x=995, y=675)
    edit_cuenta_btn.config(state="disable")
    exit_cuenta_btn = ttk.Button(cuentas_frame, text="Salir", style='button.TButton', command=exit_cuenta)
    exit_cuenta_btn.place(x=1185, y=675)

def mov_caja_adm():
    mov_caja_adm_frame = Toplevel()
    mov_caja_adm_frame.grab_set()
    mov_caja_adm_frame.resizable(0,0)
    mov_caja_adm_frame.iconbitmap('img\codemy.ico')
    mov_caja_adm_frame.title("Administrar Movimientos de Caja")
    
    ws = mov_caja_adm_frame.winfo_screenwidth()
    hs = mov_caja_adm_frame.winfo_screenheight()

    if ws == 1366 and hs == 768:
        mov_caja_adm_frame.state('zoomed')
    else:
        w = 1366
        h = 768

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        mov_caja_adm_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))
        

    topFrame = Label(mov_caja_adm_frame, height=11)
    topFrame.pack(fill="x", pady=1, padx=1)


    # Configure the Treeview Colors
    style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3", font=("Arial", 14))

    style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#162447")

    # Change Selected Color
    style.map('Treeview',
        background=[('selected', "#4f88c9")])

    # Create a Treeview Frame
    tree_frame = Frame(mov_caja_adm_frame)
    tree_frame.pack(pady=1, padx=10)
    #tree_frame.place(x=8, y=90)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame, width=20)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_scroll_h = Scrollbar(tree_frame, orient='horizontal', width=25)
    tree_scroll_h.pack(side=BOTTOM, fill=X)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, xscrollcommand=tree_scroll_h.set, selectmode="extended", height=12)
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)
    tree_scroll_h.config(command=my_tree.xview)

    # Define Our Columns
    my_tree['columns'] = ("ID_CUENTA", "ID_CONCEPTO", "ID_MOVIMIENTO", "FECHA", "CUENTA", "CONCEPTO", "DEBE", "HABER", "DESCRIPCION")

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID_CUENTA", width=0, stretch=NO)
    my_tree.column("ID_CONCEPTO", width=0, stretch=NO)
    my_tree.column("ID_MOVIMIENTO", anchor=W, width=100)
    my_tree.column("FECHA", anchor=W, width=120)
    my_tree.column("CUENTA", anchor=W, width=350)
    my_tree.column("CONCEPTO", anchor=W, width=450)
    my_tree.column("DEBE", anchor=W, width=140)
    my_tree.column("HABER", anchor=W, width=140)
    my_tree.column("DESCRIPCION", anchor=W, width=500)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID_CUENTA", text="", anchor=W)
    my_tree.heading("ID_CONCEPTO", text="", anchor=W)
    my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
    my_tree.heading("FECHA", text="Fecha", anchor=W)
    my_tree.heading("CUENTA", text="Cuenta", anchor=W)
    my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
    my_tree.heading("DEBE", text="Debe", anchor=W)
    my_tree.heading("HABER", text="Haber", anchor=W)
    my_tree.heading("DESCRIPCION", text="Descripción", anchor=W)


    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#c4d7ed")


    def clean_table():
        for item in my_tree.get_children():
            my_tree.delete(item)

    def add_data():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT ID_CUENTA, ID_CONCEPTO, ID_MOVIMIENTO, FECHA, CUENTA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER, IFNULL(DESCRIPCION, '') AS DESCRIPCION FROM Movimientos ORDER BY FECHA ASC")

        records = c.fetchall()
       
        clean_table()
        # Add our data to the screen
        global count
        count = 0


        for record in records:
            if record[6] == "":
                debe = float(0)
            else:
                debe = float(record[6])
            trans = str.maketrans('.,', ',.')
            debe = str(format(debe, ',.2f').translate(trans))

            if debe == "0,00":
                debe = ""

            if record[7] == "":
                haber = float(0)
            else:
                haber = float(record[7])
            haber = str(format(haber, ',.2f').translate(trans))

            if haber == "0,00":
                haber = ""

            date = datetime.strptime(record[3], '%Y/%m/%d').strftime('%d/%m/%Y')

            if count % 2 == 0:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], date, record[4], record[5], debe, haber, record[8]), tags=('evenrow',))
            else:
                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], date, record[4], record[5], debe, haber, record[8]), tags=('oddrow',))
            # increment counter
            count += 1

        my_tree.yview_moveto('1.0')
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

    add_data()

    window_label = ttk.Label(mov_caja_adm_frame, foreground="#162447", style="mov_cajat.TLabel", text="Carga de Movimientos de Caja")
    window_label.place(x=10, y=5)
    title_name_label = ttk.Label(mov_caja_adm_frame, foreground="#000000", style="mov_cajat.TLabel")
    title_name_label.place(x=10, y=35)
    address_label = ttk.Label(mov_caja_adm_frame, foreground="#808080", style="mov_caja.TLabel")
    address_label.place(x=10, y=65)

    # Create a database or connect to one that exists
    conn = sqlite3.connect(db_name)

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
    records = c.fetchone()

    company_name = records[0]
    address = records[1]

    c.execute("SELECT NOMBRE_CONCEPTO FROM Conceptos")
    conceptos_list = [item[0] for item in c.fetchall()]

    c.execute("SELECT NOMBRE_CUENTA, COD_CUENTA FROM Cuentas")
    cuentas_list = []
    for records in c.fetchall():
        cuentas_list.append(records[0] + " (" + records[1] + ")") 

    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()

    def clear_entry():
        id_mov_entry.config(state="normal")
        date_mov_entry.config(state="normal")
        cuentas_cmbox.config(state="normal")
        conceptos_cmbox.config(state="normal")

        id_mov_entry.delete(0, END)
        date_mov_entry.delete(0, END)
        cuentas_cmbox.set("[Cuenta...]")
        conceptos_cmbox.set("[Concepto...]")
        debe_entry.delete(0, END)
        haber_entry.delete(0, END)
        desc_mov_entry.delete(0, END)

        conceptos_cmbox.config(state="readonly")
        cuentas_cmbox.config(state="readonly")
        date_mov_entry.config(state="readonly")
        id_mov_entry.config(state="readonly")

    def update_data():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()
        sql_id_mov = "SELECT seq from sqlite_sequence WHERE name ='Movimientos'"
        c.execute(sql_id_mov)
        
        id_mov = sum([int(record[0]) for record in c.fetchall()], 1)

        c.execute("SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos")
        records = c.fetchone()

        total_debe_haber = (records[0] - records[1])
        trans = str.maketrans('.,', ',.')
        total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

        debe_total = records[0]
        debe_total = format(debe_total, ',.2f').translate(trans)

        haber_total = records[1]
        haber_total = format(haber_total, ',.2f').translate(trans)

        today_date = datetime.today().strftime('%d/%m/%Y')

        c.execute("SELECT IFNULL(MAX(FECHA), '2020/01/01'), IFNULL(MIN(FECHA), '2020/01/01') FROM Movimientos")
        dates_sql = c.fetchone()
        max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
        min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')
        
        debe_total_entry.config(state="normal")
        haber_total_entry.config(state="normal")
        total_entry.config(state="normal")
        id_mov_entry.config(state="normal")
        conceptos_cmbox.config(state="normal")
        cuentas_cmbox.config(state="normal")
        date_mov_entry.config(state="normal")
        search_end_date.config(state="normal")
        search_start_date.config(state="normal")

        debe_total_entry.delete(0, END)
        haber_total_entry.delete(0, END)
        total_entry.delete(0, END)
        id_mov_entry.delete(0, END)
        debe_entry.delete(0, END)
        haber_entry.delete(0, END)
        date_mov_entry.delete(0, END)
        search_end_date.delete(0, END)
        search_start_date.delete(0, END)
        desc_mov_entry.delete(0, END)

        debe_total_entry.insert(0, "$ " + debe_total)
        haber_total_entry.insert(0, "$ " + haber_total)
        total_entry.insert(0, "$ " + total_debe_haber)
        id_mov_entry.insert(0, id_mov)
        conceptos_cmbox.set("[Concepto...]")
        cuentas_cmbox.set("[Cuenta...]")
        date_mov_entry.insert(0, today_date)
        search_end_date.insert(0, max_date)
        search_start_date.insert(0, min_date)
        

        debe_total_entry.config(state="readonly")
        haber_total_entry.config(state="readonly")
        total_entry.config(state="readonly")
        id_mov_entry.config(state="readonly")
        conceptos_cmbox.config(state="readonly")
        cuentas_cmbox.config(state="readonly")
        date_mov_entry.config(state="readonly")
        search_end_date.config(state="readonly")
        search_start_date.config(state="readonly")

        
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


    def selected_mov(e):
        selected_filter = my_tree.focus()
        if selected_filter != "":
            # Grab record Number
            selected = my_tree.focus()
            # Grab record values
            values = my_tree.item(selected, 'values')

            id_mov_entry.config(state="normal")
            date_mov_entry.config(state="normal")
            cuentas_cmbox.config(state="normal")
            conceptos_cmbox.config(state="normal")

            idConcepto_mov_entry.delete(0, END)
            idCuenta_mov_entry.delete(0, END)
            id_mov_entry.delete(0, END)
            debe_entry.delete(0, END)
            haber_entry.delete(0, END)
            desc_mov_entry.delete(0, END)
            date_mov_entry.delete(0, END)

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT COD_CUENTA FROM Cuentas WHERE NOMBRE_CUENTA = :cuenta""",{'cuenta': values[4]})
            codCuenta = c.fetchone()
            cuentaSelect = str(values[4]) + " (" + str(codCuenta[0]) + ")"
            

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            mov_caja_adm_frame.var_cuentas_cbox.set(cuentaSelect)
            mov_caja_adm_frame.var_conceptos_cbox.set(values[5])
            idConcepto_mov_entry.insert(0, values[0])
            idCuenta_mov_entry.insert(0, values[1])
            id_mov_entry.insert(0, values[2])
            date_mov_entry.insert(0, values[3])
            debe_entry.insert(0, str(values[6]).replace('.',''))
            haber_entry.insert(0, str(values[7]).replace('.',''))
            desc_mov_entry.insert(0, values[8])

            id_mov_entry.config(state="readonly")
            date_mov_entry.config(state="readonly")
            cuentas_cmbox.config(state="readonly")
            conceptos_cmbox.config(state="readonly")
            add_mov_btn.config(state="disable")
            edit_mov_btn.config(state="normal")
            del_mov_btn.config(state="normal")
            new_mov_btn.config(state="normal")
            editCuenta_label.place_forget()
            
            
    #Bind the treeview for select
    my_tree.bind("<ButtonRelease-1>", selected_mov)


    def clean_search():
        id_mov_entry.delete(0, END)
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)
        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT IFNULL(MAX(FECHA), '2020/01/01'), IFNULL(MIN(FECHA), '2020/01/01') FROM Movimientos")
        dates_sql = c.fetchone()
        max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
        min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        search_end_date.config(state="normal")
        search_start_date.config(state="normal")

        search_end_date.delete(0, END)
        search_start_date.delete(0, END)
        searchCuenta_entry.delete(0, END)
        searchConcepto_entry.delete(0, END)
        searchConcepto_entry.insert(0, "Buscar Concepto...")
        searchConcepto_entry.config(foreground="grey")
        search_end_date.insert(0, max_date)
        search_start_date.insert(0, min_date)
        
        add_mov_btn.config(state="disable")
        edit_mov_btn.config(state="disable")
        del_mov_btn.config(state="disable")
        new_mov_btn.config(state="normal")
        search_end_date.config(state="readonly")
        search_start_date.config(state="readonly")
        editCuenta_label.place_forget()
        searchCuenta_entry.focus()
        clear_entry()
        add_data()




    def search_mov():
        id_mov_entry.delete(0, END)
        start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')
        end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')

        if start_date > end_date:
            messagebox.showerror(title="Ups..Ups..", message="La fecha [Desde] no puede ser mayor a la de [Hasta]. Intente nuevamente.", parent=mov_caja_adm_frame)
            clean_search()
        else:
            if searchConcepto_entry.get() == "Buscar Concepto..." or searchConcepto_entry.get() == "":
                conceptoSearch = "%"
            else:        
                conceptoSearch = "%" + searchConcepto_entry.get() + "%"

            if searchCuenta_entry.get() == "Buscar Cuenta..." or searchCuenta_entry.get() == "":
                cuentaSearch = "%"
            else:
                cuentaSearch = "%" + searchCuenta_entry.get() + "%"

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()
            
            c.execute("""SELECT ID_CUENTA, ID_CONCEPTO, ID_MOVIMIENTO, FECHA, CUENTA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER, IFNULL(DESCRIPCION, '') AS DESCRIPCION FROM Movimientos WHERE CONCEPTO LIKE :concepto AND CUENTA LIKE :cuenta AND FECHA BETWEEN :date_start AND :date_end ORDER BY FECHA ASC""", {'concepto': conceptoSearch, 'cuenta': cuentaSearch, 'date_start':start_date, 'date_end':end_date})

            records = c.fetchall()
        
            clean_table()
            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[6] == "":
                    debe = float(0)
                else:
                    debe = float(record[6])
                trans = str.maketrans('.,', ',.')
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if record[7] == "":
                    haber = float(0)
                else:
                    haber = float(record[7])
                haber = str(format(haber, ',.2f').translate(trans))

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[3], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], date, record[4], record[5], debe, haber, record[8]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], date, record[4], record[5], debe, haber, record[8]), tags=('oddrow',))
                # increment counter
                count += 1

            add_mov_btn.config(state="disable")
            edit_mov_btn.config(state="disable")
            del_mov_btn.config(state="disable")
            new_mov_btn.config(state="normal")

            clear_entry()
            editCuenta_label.place_forget()
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

    def new_mov_caja():
        update_data()
        add_mov_btn.config(state="normal")
        new_mov_btn.config(state="disable")
        edit_mov_btn.config(state="disable")
        del_mov_btn.config(state="disable")
        for item in my_tree.selection():
            my_tree.selection_remove(item)
        
        

    def add_mov_caja():
        if debe_entry.get() == "" and haber_entry.get() == "":
            messagebox.showerror(title="Ups..Ups..", message="¡Debe ingresar algún valor en [Debe] o [Haber] para agregar un movimiento!", parent=mov_caja_adm_frame)
        elif debe_entry.get() != "" and haber_entry.get() != "":
            messagebox.showerror(title="Ups..Ups..", message="Un único movimiento no puede tener [Debe] y [Haber] en simultaneo. Revise los datos!", parent=mov_caja_adm_frame)
        elif mov_caja_adm_frame.var_cuentas_cbox.get() == "[Cuenta...]" or mov_caja_adm_frame.var_conceptos_cbox.get() == "[Concepto...]":
            messagebox.showerror(title="Ups..Ups..", message="¡Los campos [Cuenta...] y [Concepto...] son obligatorios!", parent=mov_caja_adm_frame)
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT ID_CONCEPTO FROM Conceptos WHERE NOMBRE_CONCEPTO = :concepto""",{'concepto': mov_caja_adm_frame.var_conceptos_cbox.get()})
            idConcepto = c.fetchone()


            if debe_entry.get() == "":
                debeMov = float(0)
            else:
                debeMov = float(str(debe_entry.get()).replace(',', '.'))

            if haber_entry.get() == "":
                haberMov = float(0)
            else:
                haberMov = float(str(haber_entry.get()).replace(',', '.'))
            
            dateMov = datetime.strptime(date_mov_entry.get(), '%d/%m/%Y' ).strftime('%Y/%m/%d')
            nombreConcepto = mov_caja_adm_frame.var_conceptos_cbox.get()
            idCuenta = (str(mov_caja_adm_frame.var_cuentas_cbox.get()).partition("(")[2]).rpartition(")")[0]
            c.execute("""SELECT ID_CUENTA FROM Cuentas WHERE COD_CUENTA = :codCuenta""", {'codCuenta':idCuenta})
            idCuenta = c.fetchone()
            idCuenta = idCuenta[0]
            idConcepto = idConcepto[0]
            nombreCuenta = str(mov_caja_adm_frame.var_cuentas_cbox.get()).rpartition(" (")[0]
            descMov = desc_mov_entry.get()

            sql_add = "INSERT INTO Movimientos (ID_CUENTA, ID_CONCEPTO, FECHA, CUENTA, CONCEPTO, DEBE, HABER, DESCRIPCION) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            sql_add_args = (idCuenta, idConcepto, dateMov, nombreCuenta, nombreConcepto, debeMov, haberMov, descMov)

            c.execute(sql_add, sql_add_args)

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            clean_table()
            add_data()
            update_data()
            messagebox.showinfo(title="Movimiento Agregado", message="¡Nuevo Movimiento de Caja creado con éxito!", parent= mov_caja_adm_frame)


    def edit_mov():
        if debe_entry.get() == "" and haber_entry.get() == "":
            messagebox.showerror(title="Ups..Ups..", message="¡Debe ingresar algún valor en [Debe] o [Haber] para agregar un movimiento!", parent=mov_caja_adm_frame)
        elif debe_entry.get() != "" and haber_entry.get() != "":
            messagebox.showerror(title="Ups..Ups..", message="Un único movimiento no puede tener [Debe] y [Haber] en simultaneo. Revise los datos!", parent=mov_caja_adm_frame)
        elif mov_caja_adm_frame.var_cuentas_cbox.get() == "[Cuenta...]" or mov_caja_adm_frame.var_conceptos_cbox.get() == "[Concepto...]":
            messagebox.showerror(title="Ups..Ups..", message="¡Los campos [Cuenta...] y [Concepto...] son obligatorios!", parent=mov_caja_adm_frame)
        else:
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT ID_CONCEPTO FROM Conceptos WHERE NOMBRE_CONCEPTO = :concepto""",{'concepto': mov_caja_adm_frame.var_conceptos_cbox.get()})
            idConcepto = c.fetchone()

            if debe_entry.get() == "":
                debeMov = float(0)
            else:
                debeMov = float(str(debe_entry.get()).replace(',', '.'))

            if haber_entry.get() == "":
                haberMov = float(0)
            else:
                haberMov = float(str(haber_entry.get()).replace(',', '.'))
    
            dateMov = datetime.strptime(date_mov_entry.get(), '%d/%m/%Y' ).strftime('%Y/%m/%d')
            nombreConcepto = mov_caja_adm_frame.var_conceptos_cbox.get()
            idConcepto = idConcepto[0]
            idCuenta = (str(mov_caja_adm_frame.var_cuentas_cbox.get()).partition("(")[2]).rpartition(")")[0]
            c.execute("""SELECT ID_CUENTA FROM Cuentas WHERE COD_CUENTA = :codCuenta""", {'codCuenta':idCuenta})
            idCuenta = c.fetchone()
            idCuenta = idCuenta[0]
            nombreCuenta = str(mov_caja_adm_frame.var_cuentas_cbox.get()).rpartition(" (")[0]
            descMov = desc_mov_entry.get()

            c.execute("""UPDATE Movimientos SET
                ID_CUENTA = :idCuenta,
                ID_CONCEPTO = :idConcepto,
                FECHA = :date,
                CUENTA = :cuenta,
                CONCEPTO = :concepto,
                DEBE = :debe,
                HABER = :haber,
                DESCRIPCION = :desc
                WHERE ID_MOVIMIENTO = :oid""",
            {
                'idCuenta': idCuenta,
                'idConcepto': idConcepto,
                'date': dateMov,
                'cuenta': nombreCuenta,
                'concepto': nombreConcepto,
                'debe': debeMov,
                'haber': haberMov,
                'desc': descMov,
                'oid': id_mov_entry.get()
            })

            # Commit changes
            conn.commit()

            #Ejecuto función para que limpie las casillas y recarguen nuevamente los socios
            clean_search()
            add_data()
            editCuenta_label.place(x=255, y=690)

            # Close our connection
            conn.close()
    
    def delete_mov():
        if id_mov_entry.get() == "":
            messagebox.showerror(title="Ups..Ups..", message="¡Debe seleccionar un registro del listado primero!", parent=mov_caja_adm_frame)
        else:
            id_mov_del = id_mov_entry.get()
            confirmation = messagebox.askquestion(title="Eliminar Movimiento", message="¿Está seguro que desea eliminar el movimiento N° [" + str(id_mov_del) + "]?", parent=mov_caja_adm_frame)
            if confirmation == 'yes':
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("""DELETE FROM Movimientos WHERE ID_MOVIMIENTO = :del_id""", {'del_id': id_mov_del})
            
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                update_data()
                add_data()
                add_mov_btn.config(state="normal")
                del_mov_btn.config(state="disable")
                edit_mov_btn.config(state="disable")
                new_mov_btn.config(state="disable")
                messagebox.showinfo(title="Movimiento Eliminado", message="¡Movimento eliminado con Éxito!", parent=mov_caja_adm_frame)
                id_mov_entry.delete(0, END)
                

                    


    title_name_label.config(text=company_name)
    address_label.config(text=address)

    debe_total_label = ttk.Label(mov_caja_adm_frame, text="Total Debe", font=("Arial", 15, BOLD), anchor="n", background="grey", foreground="#ffffff", width=10)
    debe_total_label.place(x=797, y=20)
    debe_total_entry = Entry(mov_caja_adm_frame, font=("Arial", 15, BOLD), width=14)
    debe_total_entry.config(state="readonly")
    debe_total_entry.place(x=910, y=20)

    haber_total_label = ttk.Label(mov_caja_adm_frame, text="Total Haber", font=("Arial", 15, BOLD), anchor="n", background="grey", foreground="#ffffff", width=11)
    haber_total_label.place(x=1075, y=20)
    haber_total_entry = Entry(mov_caja_adm_frame, font=("Arial", 15, BOLD), width=14)
    haber_total_entry.config(state="readonly")
    haber_total_entry.place(x=1200, y=20)

    total_label = ttk.Label(mov_caja_adm_frame, text="Total", font=("Arial", 16, BOLD), anchor="n",  background="#14141f", foreground="#ffffff", width=8)
    total_label.place(x=930, y=60)
    total_entry = Entry(mov_caja_adm_frame, font=("Arial", 16, BOLD), width=14)
    total_entry.config(state="readonly")
    total_entry.place(x=1030, y=60)


    class MyDateEntry(DateEntry):
        def __init__(self, master=None, align='left', **kw):
            DateEntry.__init__(self, master, **kw)
            self.align = align

        def drop_down(self):
            """Display or withdraw the drop-down calendar depending on its current state."""
            if self._calendar.winfo_ismapped():
                self._top_cal.withdraw()
            else:
                self._validate_date()
                date = self.parse_date(self.get())
                h = self._top_cal.winfo_reqheight()
                w = self._top_cal.winfo_reqwidth()
                x_max = self.winfo_screenwidth()
                y_max = self.winfo_screenheight()
                # default: left-aligned drop-down below the entry
                x = self.winfo_rootx()
                y = self.winfo_rooty() + self.winfo_height()
                if x + w > x_max:  # the drop-down goes out of the screen
                    # right-align the drop-down
                    x += self.winfo_width() - w
                if y + h > y_max:  # the drop-down goes out of the screen
                    # bottom-align the drop-down
                    y -= self.winfo_height() + h
                if self.winfo_toplevel().attributes('-topmost'):
                    self._top_cal.attributes('-topmost', True)
                else:
                    self._top_cal.attributes('-topmost', False)
                self._top_cal.geometry('+%i+%i' % (x, y))
                self._top_cal.deiconify()
                self._calendar.focus_set()
                self._calendar.selection_set(date)

    editCuenta_label = ttk.Label(mov_caja_adm_frame, text="¡Modificado!", font=("Arial", 18, BOLD), anchor="n", foreground="red")
    editCuenta_label.place_forget()
    
    idConcepto_mov_entry = ttk.Entry(mov_caja_adm_frame)
    idCuenta_mov_entry = ttk.Entry(mov_caja_adm_frame)

    search_start_date_l = ttk.Label(mov_caja_adm_frame, text="Desde", style='movimientos.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
    search_start_date_l.place(x=10, y=100)
    search_start_date = MyDateEntry(mov_caja_adm_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
    search_start_date.config(state="readonly")
    search_start_date.place(x=10, y=125, height=36)

    search_end_date_l = ttk.Label(mov_caja_adm_frame, text="Hasta", style='movimientos.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
    search_end_date_l.place(x=170, y=100)
    search_end_date = MyDateEntry(mov_caja_adm_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
    search_end_date.config(state="readonly")
    search_end_date.place(x=170, y=125, height=36)

    #Funciones de Texto temporal Entry Search
    def temp_text_concepto(e):
        searchConcepto_entry.delete(0, END)
        searchConcepto_entry.config(font=("Arial", 16), foreground="black")


    def temp_text_add_concepto(e):
        if searchConcepto_entry.get() == "":
            searchConcepto_entry.delete(0, END)
            searchConcepto_entry.insert(0, "Buscar Concepto...")
            searchConcepto_entry.config(foreground="grey")

	#Funciones de Texto temporal Entry Search
    def temp_text_cuenta(e):
        searchCuenta_entry.delete(0, END)
        searchCuenta_entry.config(font=("Arial", 16), foreground="black")


    def temp_text_add_cuenta(e):
        if searchCuenta_entry.get() == "":
            searchCuenta_entry.delete(0, END)
            searchCuenta_entry.insert(0, "Buscar Cuenta...")
            searchCuenta_entry.config(foreground="grey")

    #Create entry and buttons in search frame.
    searchConcepto_entry = ttk.Entry(mov_caja_adm_frame, font= ("Arial", 16), foreground="grey")
    searchConcepto_entry.insert(0, "Buscar Concepto...")
    searchConcepto_entry.place(x=600,y=125, width=250, height=36)

    searchCuenta_entry = ttk.Entry(mov_caja_adm_frame, font= ("Arial", 16), foreground="grey")
    searchCuenta_entry.insert(0, "Buscar Cuenta...")
    searchCuenta_entry.place(x=330,y=125, width=250, height=36)

    def searchBind(e):
        search_mov()

    def cleanSearchBind(e):
        clean_search()

    #Bind events in search entry
    searchConcepto_entry.bind("<FocusIn>", temp_text_concepto)
    searchConcepto_entry.bind("<FocusOut>", temp_text_add_concepto)
    searchConcepto_entry.bind("<Return>", searchBind)
    searchConcepto_entry.bind("<Escape>", cleanSearchBind)
    searchCuenta_entry.bind("<FocusIn>", temp_text_cuenta)
    searchCuenta_entry.bind("<FocusOut>", temp_text_add_cuenta)
    searchCuenta_entry.bind("<Return>", searchBind)
    searchCuenta_entry.bind("<Escape>", cleanSearchBind)

    search_btn = ttk.Button(mov_caja_adm_frame, text="Buscar", style='button.TButton', command=search_mov)
    search_btn.place(x=870, y=124)
    clean_search_btn = ttk.Button(mov_caja_adm_frame, text="X", style='button.TButton', width=5, command=clean_search)
    clean_search_btn.place(x=1040, y=124)

    #label_background = ttk.Label(mov_caja_adm_frame, background="#e6e6e6")
    #label_background.place(x=1, y=490, width=1140, height=210)

    id_mov_label = ttk.Label(mov_caja_adm_frame, text="N°", style='movimientos.TLabel', width=7, borderwidth=2, relief="solid", anchor="center")
    id_mov_label.place(x=21, y=530)
    id_mov_entry = ttk.Entry(mov_caja_adm_frame, font=("Arial", 16), width=7)
    id_mov_entry.config(state="readonly")
    id_mov_entry.place(x=21, y=557, height=36)

    date_mov_label = ttk.Label(mov_caja_adm_frame, text="Fecha", style='movimientos.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
    date_mov_label.place(x=140, y=530)
    date_mov_entry = MyDateEntry(mov_caja_adm_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
    date_mov_entry.config(state="readonly")
    date_mov_entry.place(x=140, y=557, height=36)

    cuentas_mov_label = ttk.Label(mov_caja_adm_frame, text="Cuenta", style='movimientos.TLabel', width=55, borderwidth=2, relief="solid", anchor="center")
    cuentas_mov_label.place(x=312, y=530)

    mov_caja_adm_frame.var_cuentas_cbox = StringVar()
	
    cuentas_cmbox = ttk.Combobox(mov_caja_adm_frame, font=("Arial", 15, BOLD), textvariable=mov_caja_adm_frame.var_cuentas_cbox, state="readonly", width=60, height=12)
    cuentas_cmbox['values'] = cuentas_list
    cuentas_cmbox.set("[Cuenta...]")
    cuentas_cmbox.place(x=312, y=557,  height=36)

    conceptos_mov_label = ttk.Label(mov_caja_adm_frame, text="Concepto", style='movimientos.TLabel', width=50, borderwidth=2, relief="solid", anchor="center")
    conceptos_mov_label.place(x=21, y=610)

    mov_caja_adm_frame.var_conceptos_cbox = StringVar()
	
    conceptos_cmbox = ttk.Combobox(mov_caja_adm_frame, font=("Arial", 15, BOLD), textvariable=mov_caja_adm_frame.var_conceptos_cbox, state="readonly", width=55, height=12)
    conceptos_cmbox['values'] = conceptos_list
    conceptos_cmbox.set("[Concepto...]")
    conceptos_cmbox.place(x=21, y=637, height=36)

    def only_text_obs(inp):
        if len(inp) > 80:
            return False
        elif inp.isalnum():
            return True
        elif inp == "":
            return True
        elif inp.isspace():
            return False
        elif ' ' in inp:
            return True
        elif '.' in inp:
            return True
        elif '-' in inp:
            return True
        else:
            return False

    obs_validation = root.register(only_text_obs)

    desc_mov_label = ttk.Label(mov_caja_adm_frame, text="Descripción", style='movimientos.TLabel', width=54, borderwidth=2, relief="solid", anchor="center")
    desc_mov_label.place(x=682, y=610)
    desc_mov_entry = ttk.Entry(mov_caja_adm_frame, font=("Arial", 16), width=54)
    desc_mov_entry.config(validate="key", validatecommand=(obs_validation, "%P"))
    desc_mov_entry.place(x=682, y=637, height=36)


    def only_number_imp(inp):
        try:
            if len(inp) > 10:
                return False
            elif "." in inp:
                return False
            else:
                float(str(inp).replace(',', '.'))
        except:
            if inp == "":
                return True
            else:
                return False
        return True

    num_validation = mov_caja_adm_frame.register(only_number_imp)

    debe_label = ttk.Label(mov_caja_adm_frame, text="Debe", style='movimientos.TLabel', width=11, borderwidth=2, relief="solid", anchor="center")
    debe_label.place(x=1027, y=530)
    debe_entry = Entry(mov_caja_adm_frame, font=("Arial", 16), width=11)
    debe_entry.config(validate="key", validatecommand=(num_validation, "%P"))
    debe_entry.place(x=1027, y=557, height=36)

    haber_label = ttk.Label(mov_caja_adm_frame, text="Haber", style='movimientos.TLabel', width=11, borderwidth=2, relief="solid", anchor="center")
    haber_label.place(x=1195, y=530)
    haber_entry = Entry(mov_caja_adm_frame, font=("Arial", 16), width=11)
    haber_entry.config(validate="key", validatecommand=(num_validation, "%P"))
    haber_entry.place(x=1195, y=557, height=36)
    
    update_data()

    new_mov_btn = ttk.Button(mov_caja_adm_frame, text="+", style='button.TButton', command=new_mov_caja, width=4)
    new_mov_btn.place(x=420, y=690)
    new_mov_btn.config(state="disable")

    add_mov_btn = ttk.Button(mov_caja_adm_frame, text="Agregar", style='button.TButton', command=add_mov_caja)
    add_mov_btn.place(x=510, y=690)
    
    edit_mov_btn = ttk.Button(mov_caja_adm_frame, text="Editar", style='button.TButton', command=edit_mov)
    edit_mov_btn.place(x=700, y=690)
    edit_mov_btn.config(state="disable")

    del_mov_btn = ttk.Button(mov_caja_adm_frame, text="Eliminar", style='button.TButton', command=delete_mov)
    del_mov_btn.place(x=890, y=690)
    del_mov_btn.config(state="disable")

    def exit_mov():
        mov_caja_adm_frame.destroy()

    exit_mov_btn = ttk.Button(mov_caja_adm_frame, text="Salir", style='button.TButton', command=exit_mov)
    exit_mov_btn.place(x=1180, y=690)

def all_movements():
    all_mov_frame = Toplevel()
    all_mov_frame.grab_set()
    all_mov_frame.resizable(0,0)
    all_mov_frame.iconbitmap('img\codemy.ico')
    all_mov_frame.title("Todos los Movimientos de Caja por Conceptos")
    

    ws = all_mov_frame.winfo_screenwidth()
    hs = all_mov_frame.winfo_screenheight()

    if ws == 1366 and hs == 768:
        all_mov_frame.state('zoomed')
    else:
        w = 1366
        h = 768

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        
        all_mov_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # Configure the Treeview Colors
    style.configure("Treeview",
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3", font=("Arial", 14))

    style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

    # Change Selected Color
    style.map('Treeview',
        background=[('selected', "#347083")])

    # Create a Treeview Frame
    tree_frame = Frame(all_mov_frame)
    #tree_frame.pack(pady=10)
    tree_frame.place(x=8, y=95)

    # Create a Treeview Scrollbar
    tree_scroll = Scrollbar(tree_frame, width=20)
    tree_scroll.pack(side=RIGHT, fill=Y)

    # Create The Treeview
    my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=20)
    my_tree.pack()

    # Configure the Scrollbar
    tree_scroll.config(command=my_tree.yview)

    # Define Our Columns
    my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CONCEPTO", "DEBE", "HABER", 'DEUDOR', 'ACREEDOR')

    # Format Our Columns
    my_tree.column("#0", width=0, stretch=NO)
    my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
    my_tree.column("FECHA", anchor=W, width=120)
    my_tree.column("CONCEPTO", anchor=W, width=535)
    my_tree.column("DEBE", anchor=W, width=170)
    my_tree.column("HABER", anchor=W, width=170)
    my_tree.column("DEUDOR", anchor=W, width=170)
    my_tree.column("ACREEDOR", anchor=W, width=170)

    # Create Headings
    my_tree.heading("#0", text="", anchor=W)
    my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
    my_tree.heading("FECHA", text="Fecha", anchor=W)
    my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
    my_tree.heading("DEBE", text="Debe", anchor=W)
    my_tree.heading("HABER", text="Haber", anchor=W)
    my_tree.heading("DEUDOR", text="Deudor", anchor=W)
    my_tree.heading("ACREEDOR", text="Acreedor", anchor=W)

    # Create Striped Row Tags
    my_tree.tag_configure('oddrow', background="white")
    my_tree.tag_configure('evenrow', background="#A5C9CA")

    def update_data():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT IFNULL(SUM(DEBE), 0.00), IFNULL(SUM(HABER), 0.00) FROM Movimientos")
        records = c.fetchone()

        total_debe_haber = (records[0] - records[1])
        trans = str.maketrans('.,', ',.')
        total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

        debe_total = records[0]
        debe_total = format(debe_total, ',.2f').translate(trans)

        haber_total = records[1]
        haber_total = format(haber_total, ',.2f').translate(trans)
        
        debe_total_entry.config(state="normal")
        haber_total_entry.config(state="normal")
        total_entry.config(state="normal")

        debe_total_entry.delete(0, END)
        haber_total_entry.delete(0, END)
        total_entry.delete(0, END)

        debe_total_entry.insert(0, "$ " + debe_total)
        haber_total_entry.insert(0, "$ " + haber_total)
        total_entry.insert(0, "$ " + total_debe_haber)

        debe_total_entry.config(state="readonly")
        haber_total_entry.config(state="readonly")
        total_entry.config(state="readonly")
        
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

    def add_conceptos():
        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT ID_MOVIMIENTO, FECHA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos ORDER BY FECHA ASC")

        records = c.fetchall()
        
        # Add our data to the screen
        global count
        count = 0
           

        for record in records:       
            if record[3] == "":
                debe_total = float(0)
            else:
                debe_total = float(record[3])

            if record[4] == "":
                haber_total = float(0)
            else:
                haber_total = float(record[4])
            
            total_record = debe_total - haber_total

            if count == 0:
                total_init = debe_total - haber_total
                total_deudor = float(0)
                total_acreedor = float(0)
            elif count == 1:
                total_deudor = total_deudor + total_init + total_record
                total_acreedor = (total_acreedor + total_init + total_record)
            else:
                total_deudor = total_deudor + total_record
                total_acreedor = (total_acreedor + total_record)

            if float(total_deudor) < 0.00:
                if count == 0:
                    total_deudor = ""
                    total_acreedor = ""
                else:
                    str.maketrans('.,', ',.')
                    total_acreedor_backup = round(total_acreedor,2)
                    total_acreedor = str(format(round(total_acreedor * -1,2), ',.2f').translate(trans))
                    

                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])
                trans = str.maketrans('.,', ',.')
                debe = str(format(debe, ',.2f').translate(trans))            

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])
                haber = str(format(haber, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('oddrow',))

                if count == 0:
                    total_deudor = float(0)
                    total_acreedor = float(0)
                else:
                    total_acreedor = total_acreedor_backup

                # increment counter
                count += 1

                

            else:
                if count == 0:
                    total_deudor = ""
                    total_acreedor = ""
                else:
                    str.maketrans('.,', ',.')
                    total_deudor_backup = round(total_deudor, 2)
                    total_deudor = str(format(round(total_deudor, 2), ',.2f').translate(trans))

                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])
                trans = str.maketrans('.,', ',.')
                debe = str(format(debe, ',.2f').translate(trans))            

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])
                haber = str(format(haber, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('oddrow',))

                

                if count == 0:
                    total_deudor = float(0)
                    total_acreedor = float(0)
                else:
                    total_deudor = total_deudor_backup

                # increment counter
                count += 1

                

        my_tree.yview_moveto('1.0')
        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

    add_conceptos()

    window_label = ttk.Label(all_mov_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Todos los Movimientos de Caja por Conceptos")
    window_label.place(x=10, y=5)
    title_name_label = ttk.Label(all_mov_frame, foreground="#000000", style="mov_cajat.TLabel")
    title_name_label.place(x=10, y=35)
    address_label = ttk.Label(all_mov_frame, foreground="#808080", style="mov_caja.TLabel")
    address_label.place(x=10, y=65)

    # Create a database or connect to one that exists
    conn = sqlite3.connect(db_name)

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
    records = c.fetchone()

    company_name = records[0]
    address = records[1]

    # Commit changes
    conn.commit()
    # Close our connection
    conn.close()


    def exportData():
        confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos de Caja por Conceptos?", parent=all_mov_frame)

        if confirmation == 'yes':
            mov_lst = []
            count = 0
            for row_id in my_tree.get_children():
                count += 1
                row = my_tree.item(row_id, 'values')
                mov_lst.append(row)
            mov_lst = list(map(list, mov_lst))
            pdf = FPDF('P', 'mm', 'A4')
            pdf.add_page()
            pdf.set_font("Arial", "BI", 8)
            pdf.set_text_color(0,0,0)
            pdf.set_y(-25)
            today_date = datetime.today().strftime('%d-%m-%Y')
            pdf.cell(0, 0, today_date, 0, 0, 'L')
            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
            pdf.set_xy(0,5)
            pdf.set_font("Times", "B", 20)
            pdf.set_text_color(128,0,0)
            pdf.cell(10)
            pdf.cell(70, 10, 'Todos los Movimientos de Caja por Conceptos', 0, 2, 'L')
            pdf.set_text_color(0,0,0)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(70, 5, company_name,0, 2, 'L')
            pdf.set_font("Arial", "B", 9)
            pdf.set_text_color(128,128,128)
            pdf.cell(70, 5, address,0, 2, 'L')
            pdf.set_text_color(128,0,0)
            pdf.set_font("Arial", "B", 10)
            pdf.cell(20, 5, 'Fecha', 1, 0, 'C')
            pdf.cell(70, 5, 'Concepto', 1, 0, 'C')
            pdf.cell(25, 5, 'Debe', 1, 0, 'C')
            pdf.cell(25, 5, 'Haber', 1, 0, 'C')
            pdf.cell(25, 5, 'Deudor', 1, 0, 'C')
            pdf.cell(25, 5, 'Acreedor', 1, 0, 'C')
            pdf.set_auto_page_break(True, 30)
            page_num = pdf.page_no()
            for record in mov_lst:
                if page_num != pdf.page_no():
                    page_num = pdf.page_no()
                    pdf.set_auto_page_break(False, 0)
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_y(10)
                    pdf.set_auto_page_break(True, 30)
                pdf.set_font('arial', '', 8)
                pdf.set_text_color(0,0,0)
                pdf.multi_cell(190,5," ", 0, 1)
                pdf.cell(20, 5, record[1], 'B', 0, 'C')
                pdf.cell(70, 5, record[2], 'B', 0, 'C')
                pdf.cell(25, 5, record[3], 'B', 0, 'C')
                pdf.cell(25, 5, record[4], 'B', 0, 'C')
                pdf.set_font('arial', 'B', 8)
                pdf.cell(25, 5, record[5], 'B', 0, 'C')
                pdf.set_text_color(255, 0, 0)
                pdf.cell(25, 5, record[6], 'B', 0, 'C')
            pdf.multi_cell(190,8," ", 0, 1)  
            pdf.set_font("Arial", "B", 8)
            pdf.set_text_color(255,255,255)
            pdf.set_fill_color(0,0,0)
            pdf.cell(131, 5, ' ', 0, 0, 'C')
            pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
            pdf.set_text_color(0)
            pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
            path = os.path.expanduser("~/Desktop")
            if not os.path.exists(path + "/Reportes Conceptos"):
                os.makedirs(path + "/Reportes Conceptos")
            pdf.output(path + '/Reportes Conceptos/Todos Los Movimientos - Concepto.pdf', 'F')
            messagebox.showinfo(title="Listado Exportado", message="El listado [Todos Los Movimientos - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= all_mov_frame)


    def exitAllMov():
        all_mov_frame.destroy()


    title_name_label.config(text=company_name)
    address_label.config(text=address)

    export_btn = ttk.Button(all_mov_frame, text="Exportar", style='button.TButton', command=exportData)
    export_btn.place(x=1180, y=40)
    
    exit_btn = ttk.Button(all_mov_frame, text="Salir", style='button.TButton', command=exitAllMov)
    exit_btn.place(x=1180, y=670)

    debe_total_entry = Entry(all_mov_frame, font=("Arial", 14, BOLD), width=14)
    debe_total_entry.config(state="readonly")
    debe_total_entry.place(x=672, y=635)

    haber_total_entry = Entry(all_mov_frame, font=("Arial", 14, BOLD), width=14)
    haber_total_entry.config(state="readonly")
    haber_total_entry.place(x=840, y=635)

    total_entry = Entry(all_mov_frame, font=("Arial", 14, BOLD), width=14)
    total_entry.config(state="readonly")
    total_entry.place(x=1015, y=635)

    update_data()

def movementsBetweenDates():
    try:
        bet_dates_mov_frame = Toplevel()
        bet_dates_mov_frame.grab_set()
        bet_dates_mov_frame.resizable(0,0)
        bet_dates_mov_frame.iconbitmap('img\codemy.ico')
        bet_dates_mov_frame.title("Impresión de Caja entre Fechas")

        ws = bet_dates_mov_frame.winfo_screenwidth()
        hs = bet_dates_mov_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            bet_dates_mov_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            bet_dates_mov_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(bet_dates_mov_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CONCEPTO", "DEBE", "HABER", 'DEUDOR', 'ACREEDOR')

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=120)
        my_tree.column("CONCEPTO", anchor=W, width=575)
        my_tree.column("DEBE", anchor=W, width=160)
        my_tree.column("HABER", anchor=W, width=160)
        my_tree.column("DEUDOR", anchor=W, width=160)
        my_tree.column("ACREEDOR", anchor=W, width=160)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("DEUDOR", text="Deudor", anchor=W)
        my_tree.heading("ACREEDOR", text="Acreedor", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT IFNULL(SUM(DEBE), 0.00), IFNULL(SUM(HABER), 0.00) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            saldo_init_entry.delete(0, END)
        

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)
            saldo_init_entry.insert(0, "0,00")

            saldo_init_entry.config(state="readonly")
            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")
            
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT ID_MOVIMIENTO, FECHA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos ORDER BY FECHA ASC")

            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0
            
            clean_table()

            for record in records:       
                if record[3] == "":
                    debe_total = float(0)
                else:
                    debe_total = float(record[3])

                if record[4] == "":
                    haber_total = float(0)
                else:
                    haber_total = float(record[4])
                
                total_record = debe_total - haber_total

                if count == 0:
                    total_init = debe_total - haber_total
                    total_deudor = float(0)
                    total_acreedor = float(0)
                elif count == 1:
                    total_deudor = total_deudor + total_init + total_record
                    total_acreedor = (total_acreedor + total_init + total_record)
                else:
                    total_deudor = total_deudor + total_record
                    total_acreedor = (total_acreedor + total_record)

                if float(total_deudor) < 0.00:
                    if count == 0:
                        total_deudor = ""
                        total_acreedor = ""
                    else:
                        str.maketrans('.,', ',.')
                        total_acreedor_backup = round(total_acreedor,2)
                        total_acreedor = str(format(round(total_acreedor * -1,2), ',.2f').translate(trans))
                        

                    if record[3] == "":
                        debe = float(0)
                    else:
                        debe = float(record[3])
                    trans = str.maketrans('.,', ',.')
                    debe = str(format(debe, ',.2f').translate(trans))            

                    if record[4] == "":
                        haber = float(0)
                    else:
                        haber = float(record[4])
                    haber = str(format(haber, ',.2f').translate(trans))

                    if debe == "0,00":
                        debe = ""

                    if haber == "0,00":
                        haber = ""

                    date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                    

                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('oddrow',))

                    if count == 0:
                        total_deudor = float(0)
                        total_acreedor = float(0)
                    else:
                        total_acreedor = total_acreedor_backup

                    # increment counter
                    count += 1

                    

                else:
                    if count == 0:
                        total_deudor = ""
                        total_acreedor = ""
                    else:
                        str.maketrans('.,', ',.')
                        total_deudor_backup = round(total_deudor, 2)
                        total_deudor = str(format(round(total_deudor, 2), ',.2f').translate(trans))

                    if record[3] == "":
                        debe = float(0)
                    else:
                        debe = float(record[3])
                    trans = str.maketrans('.,', ',.')
                    debe = str(format(debe, ',.2f').translate(trans))            

                    if record[4] == "":
                        haber = float(0)
                    else:
                        haber = float(record[4])
                    haber = str(format(haber, ',.2f').translate(trans))

                    if debe == "0,00":
                        debe = ""

                    if haber == "0,00":
                        haber = ""

                    date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('oddrow',))

                    

                    if count == 0:
                        total_deudor = float(0)
                        total_acreedor = float(0)
                    else:
                        total_deudor = total_deudor_backup

                    # increment counter
                    count += 1

                    

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(bet_dates_mov_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Impresión de Caja entre Fechas")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(bet_dates_mov_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(bet_dates_mov_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Impresión de Caja entre Fechas?", parent=bet_dates_mov_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No se puede exportar resultados vacíos! Intente con otro filtro.", parent=bet_dates_mov_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Impresión de Caja entre Fechas', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(128, 3, company_name,0, 0, 'L')
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(22, 5, 'Saldo Inicial', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(40, 5, "$" + saldo_init_entry.get(), 1, 0, 'C')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(20, 5, 'Fecha', 1, 0, 'C')
                    pdf.cell(70, 5, 'Concepto', 1, 0, 'C')
                    pdf.cell(25, 5, 'Debe', 1, 0, 'C')
                    pdf.cell(25, 5, 'Haber', 1, 0, 'C')
                    pdf.cell(25, 5, 'Deudor', 1, 0, 'C')
                    pdf.cell(25, 5, 'Acreedor', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(10)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 8)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(20, 5, record[1], 'B', 0, 'C')
                        pdf.cell(70, 5, record[2], 'B', 0, 'C')
                        pdf.cell(25, 5, record[3], 'B', 0, 'C')
                        pdf.cell(25, 5, record[4], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 8)
                        pdf.cell(25, 5, record[5], 'B', 0, 'C')
                        pdf.set_text_color(255, 0, 0)
                        pdf.cell(25, 5, record[6], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(128, 5, ' ', 0, 0, 'C')
                    pdf.cell(22, 5, 'Saldo Final', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(40, 5, total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                    pdf.output(path + '/Reportes Conceptos/Movimientos entre Fechas - Concepto.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Movimientos entre Fechas - Concepto.pdf] se exportó correctamente en el Escritorio.", parent=bet_dates_mov_frame)

            
        def clean_search():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT IFNULL(MAX(FECHA), '2020/01/01'), IFNULL(MIN(FECHA), '2020/01/01') FROM Movimientos")
            dates_sql = c.fetchone()
            max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
            min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            search_end_date.config(state="normal")
            search_start_date.config(state="normal")
            saldo_init_entry.config(state="normal")


            saldo_init_entry.delete(0, END)
            search_end_date.delete(0, END)
            search_start_date.delete(0, END)

            search_end_date.insert(0, max_date)
            search_start_date.insert(0, min_date)
            saldo_init_entry.insert(0, "0,00")

            saldo_init_entry.config(state="readonly")
            search_end_date.config(state="readonly")
            search_start_date.config(state="readonly")
            add_conceptos()
            update_data()
            

        def search_mov():
            try: 
                start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')
                end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')  

                if start_date > end_date:
                    messagebox.showerror(title="Ups..Ups..", message="¡Error! La fecha DESDE no puede ser mayor a la fecha HASTA, intenta nuevamente.", parent=bet_dates_mov_frame)
                    clean_search()
                else:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)
                    # Create a cursor instance
                    c = conn.cursor()

                    c.execute("SELECT MIN(FECHA) FROM Movimientos")
                    dates_sql = c.fetchone()
                    min_date = dates_sql[0]

                    if min_date == start_date:
                        saldo_init_entry.config(state="normal")
                        saldo_init_entry.delete(0, END)
                        saldo_init_entry.insert(0, "0,00")
                        saldo_init_entry.config(state="readonly")
                        saldo_init = float(0.00)
                    else:
                        c.execute("""SELECT IFNULL(SUM(DEBE), 0.00), IFNULL(SUM(HABER), 0.00) FROM Movimientos WHERE FECHA < :min_date""", {'min_date': start_date})
                        
                        saldo_init_records = c.fetchone()

                        if saldo_init_records[0] == 0.00 and saldo_init_records[1] == 0.00:
                            saldo_init_format = "0,00"
                            saldo_init = float(0.00)
                        else:
                            trans = str.maketrans('.,', ',.')
                            saldo_init_format =  str(format(round((saldo_init_records[0] - saldo_init_records[1]),2), ',.2f').translate(trans))
                            saldo_init = float((saldo_init_records[0] - saldo_init_records[1]))
                            
                        
                        saldo_init_entry.config(state="normal")
                        saldo_init_entry.delete(0, END)
                        saldo_init_entry.insert(0, saldo_init_format)
                        saldo_init_entry.config(state="readonly")

                    c.execute("""SELECT ID_MOVIMIENTO, FECHA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos WHERE FECHA BETWEEN :date_start AND :date_end ORDER BY FECHA ASC""", {'date_start':start_date, 'date_end':end_date})

                    records = c.fetchall()
                
                    clean_table()

                    # Add our data to the screen
                    global count
                    count = 0
                    
                    sum_debe = float(0.00)
                    sum_haber = float(0.00)
                    total_acreedor_backup = float(0.00)
                    total_deudor_backup = float(0.00)
                    last_register = 1

                    for record in records:       
                        if record[3] == "":
                            debe_total = float(0)
                        else:
                            debe_total = float(record[3])

                        if record[4] == "":
                            haber_total = float(0)
                        else:
                            haber_total = float(record[4])
                        
                        total_record = debe_total - haber_total

                        if count == 0:
                            total_init = saldo_init + (debe_total - haber_total)
                            total_deudor = float(0)
                            total_acreedor = float(0)
                        elif count == 1:
                            total_deudor = total_deudor + total_init + total_record
                            total_acreedor = (total_acreedor + total_init + total_record)
                        else:
                            total_deudor = total_deudor + total_record
                            total_acreedor = (total_acreedor + total_record)

                        if float(total_deudor) < 0.00:
                            if count == 0:
                                total_deudor = ""
                                total_acreedor = ""
                            else:
                                trans = str.maketrans('.,', ',.')
                                total_acreedor_backup = round(total_acreedor,2)
                                total_acreedor = str(format(round(total_acreedor * -1,2), ',.2f').translate(trans))

                            if record[3] == "":
                                debe = float(0)
                            else:
                                debe = float(record[3])
                            sum_debe = sum_debe + debe
                            trans = str.maketrans('.,', ',.')
                            debe = str(format(debe, ',.2f').translate(trans))            

                            if record[4] == "":
                                haber = float(0)
                            else:
                                haber = float(record[4])
                            sum_haber = sum_haber + haber
                            haber = str(format(haber, ',.2f').translate(trans))

                            if debe == "0,00":
                                debe = ""

                            if haber == "0,00":
                                haber = ""

                            date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                            

                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, "", total_acreedor), tags=('oddrow',))

                            if count == 0:
                                total_deudor = float(0)
                                total_acreedor = float(0)
                            else:
                                total_acreedor = total_acreedor_backup

                            last_register = 0
                            # increment counter
                            count += 1

                            

                        else:
                            if count == 0:
                                total_deudor = ""
                                total_acreedor = ""
                            else:
                                total_deudor_backup = round(total_deudor, 2)
                                total_deudor = str(format(round(total_deudor, 2), ',.2f').translate(trans))

                            if record[3] == "":
                                debe = float(0)
                            else:
                                debe = float(record[3])
                            sum_debe = sum_debe + debe
                            trans = str.maketrans('.,', ',.')
                            debe = str(format(debe, ',.2f').translate(trans))            

                            if record[4] == "":
                                haber = float(0)
                            else:
                                haber = float(record[4])
                            sum_haber = sum_haber + haber
                            haber = str(format(haber, ',.2f').translate(trans))

                            if debe == "0,00":
                                debe = ""

                            if haber == "0,00":
                                haber = ""

                            date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, total_deudor, ""), tags=('oddrow',))

                            

                            if count == 0:
                                total_deudor = float(0)
                                total_acreedor = float(0)
                            else:
                                total_deudor = total_deudor_backup

                            last_register = 1
                            # increment counter
                            count += 1

                    trans = str.maketrans('.,', ',.')
                    if last_register == 0:
                        total_entry.config(state="normal")
                        total_entry.delete(0, END)
                        total_entry.insert(0 , "$ " + str(format(round(total_acreedor_backup, 2), ',.2f').translate(trans)))
                        total_entry.config(state="readonly")
                    else:
                        total_entry.config(state="normal")
                        total_entry.delete(0, END)
                        total_entry.insert(0 , "$ " + str(format(round(total_deudor_backup, 2), ',.2f').translate(trans)))
                        total_entry.config(state="readonly")
                    
                    haber_total_entry.config(state="normal")
                    haber_total_entry.delete(0, END)
                    haber_total_entry.insert(0 , "$ " + str(format(round(sum_haber, 2), ',.2f').translate(trans)))
                    haber_total_entry.config(state="readonly")

                    debe_total_entry.config(state="normal")
                    debe_total_entry.delete(0, END)
                    debe_total_entry.insert(0 , "$ " + str(format(round(sum_debe, 2), ',.2f').translate(trans)))
                    debe_total_entry.config(state="readonly")

                    my_tree.yview_moveto('1.0')

                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
            except:
                messagebox.showerror(title="Ups..Ups..", message="¡Ocurrió un error al ejecutar el filtro! Por favor, intenta nuevamente con parámetros similares.", parent=bet_dates_mov_frame)




        title_name_label.config(text=company_name)
        address_label.config(text=address)

        search_start_date_l = ttk.Label(bet_dates_mov_frame, text="Desde", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_start_date_l.place(x=10, y=90)
        search_start_date = DateEntry(bet_dates_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_start_date.config(state="readonly")
        search_start_date.place(x=10, y=115, height=35)

        search_end_date_l = ttk.Label(bet_dates_mov_frame, text="Hasta", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_end_date_l.place(x=180, y=90)
        search_end_date = DateEntry(bet_dates_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_end_date.config(state="readonly")
        search_end_date.place(x=180, y=115, height=35)

        search_btn = ttk.Button(bet_dates_mov_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=350, y= 113)
        clean_search_btn = ttk.Button(bet_dates_mov_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=520, y=113)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        saldo_init_label = ttk.Label(bet_dates_mov_frame, text="Saldo Inicial", style='style_tdata.TLabel', width=15, borderwidth=2, relief="solid", anchor="center")
        saldo_init_label.place(x=880, y=15)
        saldo_init_entry = Entry(bet_dates_mov_frame, font=("Arial", 16, BOLD), width=15, justify="center")
        saldo_init_entry.insert(0, "0,00")
        saldo_init_entry.config(state="readonly")
        saldo_init_entry.place(x=880, y=40)

        export_btn = ttk.Button(bet_dates_mov_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        def exitMovBetDates():
            bet_dates_mov_frame.destroy()

        exit_btn = ttk.Button(bet_dates_mov_frame, text="Salir", style='button.TButton', command=exitMovBetDates)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(bet_dates_mov_frame, font=("Arial", 14, BOLD), width=14,  justify="center")
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=685, y=635)

        haber_total_entry = Entry(bet_dates_mov_frame, font=("Arial", 14, BOLD), width=14,  justify="center")
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=852, y=635)

        total_entry = Entry(bet_dates_mov_frame, font=("Arial", 14, BOLD), width=14,  justify="center")
        total_entry.config(state="readonly")
        total_entry.place(x=1015, y=635)

        update_data()
        clean_search()
    except:
        bet_dates_mov_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def movementsPerConceptBetweenDates():
    try:
        concept_bet_dates_frame = Toplevel()
        concept_bet_dates_frame.grab_set()
        concept_bet_dates_frame.resizable(0,0)
        concept_bet_dates_frame.iconbitmap('img\codemy.ico')
        concept_bet_dates_frame.title("Movimientos de un Concepto entre Fechas")

        ws = concept_bet_dates_frame.winfo_screenwidth()
        hs = concept_bet_dates_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            concept_bet_dates_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            concept_bet_dates_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(concept_bet_dates_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=16)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CONCEPTO", "DEBE", "HABER")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=130)
        my_tree.column("CONCEPTO", anchor=W, width=740)
        my_tree.column("DEBE", anchor=W, width=230)
        my_tree.column("HABER", anchor=W, width=230)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            search_concept_cmbox.config(state="normal")
            search_concept_cmbox.current(0)
            searchConcept = concept_bet_dates_frame.var_pant_cbox.get()
            search_concept_cmbox.config(state="readonly")
            
            c.execute("""SELECT IFNULL(SUM(DEBE), 0.00), IFNULL(SUM(HABER), 0.00) FROM Movimientos WHERE CONCEPTO = :concept_name""", {'concept_name': searchConcept})
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")
            
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            search_concept_cmbox.config(state="normal")
            search_concept_cmbox.current(0)
            searchConcept = concept_bet_dates_frame.var_pant_cbox.get()
            search_concept_cmbox.config(state="readonly")

            c.execute("""SELECT ID_MOVIMIENTO, FECHA, CONCEPTO, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos WHERE CONCEPTO = :concept_name ORDER BY FECHA ASC""", {'concept_name': searchConcept})

            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0
            
            clean_table()

            for record in records:
                    if record[3] == "":
                        debe = float(0)
                    else:
                        debe = float(record[3])
                    trans = str.maketrans('.,', ',.')
                    debe = str(format(debe, ',.2f').translate(trans))            

                    if record[4] == "":
                        haber = float(0)
                    else:
                        haber = float(record[4])
                    haber = str(format(haber, ',.2f').translate(trans))

                    if debe == "0,00":
                        debe = ""

                    if haber == "0,00":
                        haber = ""

                    date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('oddrow',))

                    # increment counter
                    count += 1
                    

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        window_label = ttk.Label(concept_bet_dates_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Movimientos de un Concepto entre Fechas")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(concept_bet_dates_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(concept_bet_dates_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        c.execute("SELECT NOMBRE_CONCEPTO FROM Conceptos")
        conceptos_list = [item[0] for item in c.fetchall()]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Movimientos de un Concepto entre Fechas?", parent=concept_bet_dates_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No se puede exportar resultados vacíos! Intente con otro filtro.", parent=concept_bet_dates_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Movimientos de un Concepto entre Fechas', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(148, 3, company_name,0, 0, 'L')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 12)
                    pdf.cell(30, 5, 'Fecha', 1, 0, 'C')
                    pdf.cell(100, 5, 'Concepto', 1, 0, 'C')
                    pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                    pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(10)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 12)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(30, 5, record[1], 'B', 0, 'C')
                        if len(record[2]) > 20:
                            pdf.set_font('arial', '', 10)   
                        pdf.cell(100, 5, record[2], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 12)
                        pdf.cell(30, 5, record[3], 'B', 0, 'C')
                        pdf.set_text_color(255,0,0)
                        pdf.cell(30, 5, record[4], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)  
                    pdf.set_font("Arial", "B", 12)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(100, 5, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, debe_total_entry.get(), 1, 0, 'C')
                    pdf.cell(30, 5, haber_total_entry.get(), 1, 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)
                    pdf.set_font("Arial", "B", 12)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(115, 3, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Saldo Final', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                    pdf.output(path + '/Reportes Conceptos/Movimiento de Conceptos entre Fechas - Concepto.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Movimiento de Conceptos entre Fechas - Concepto.pdf] se exportó correctamente en el Escritorio.", parent=concept_bet_dates_frame)
            
        def clean_search():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT MAX(FECHA), MIN(FECHA) FROM Movimientos")
            dates_sql = c.fetchone()
            max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
            min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            search_end_date.config(state="normal")
            search_start_date.config(state="normal")
        
            search_end_date.delete(0, END)
            search_start_date.delete(0, END)

            search_end_date.insert(0, max_date)
            search_start_date.insert(0, min_date)

            search_end_date.config(state="readonly")
            search_start_date.config(state="readonly")
            add_conceptos()
            update_data()
            

        def search_mov():
                start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')
                end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')  

                if start_date > end_date:
                    messagebox.showerror(title="Ups..Ups..", message="¡Error! La fecha DESDE no puede ser mayor a la fecha HASTA, intenta nuevamente.", parent=concept_bet_dates_frame)
                    clean_search()
                else:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)
                    # Create a cursor instance
                    c = conn.cursor()

                    searchConcept = concept_bet_dates_frame.var_pant_cbox.get()
                    c.execute("""SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CONCEPTO = :concept_name AND FECHA BETWEEN :date_start AND :date_end ORDER BY FECHA ASC""", {'concept_name':searchConcept,'date_start':start_date, 'date_end':end_date})
                    total_concept = c.fetchone()
                    
                    total_entry.config(state="normal")
                    haber_total_entry.config(state="normal")
                    debe_total_entry.config(state="normal")

                    total_entry.delete(0, END)
                    haber_total_entry.delete(0, END)
                    debe_total_entry.delete(0, END)

                    trans = str.maketrans('.,', ',.')
                    total_imp = str(format(round(total_concept[0]-total_concept[1], 2), ',.2f').translate(trans))

                    trans = str.maketrans('.,', ',.')
                    total_entry.insert(0, "$ " + total_imp)
                    haber_total_entry.insert(0, "$ " + str(format(round(total_concept[1], 2), ',.2f').translate(trans)))
                    debe_total_entry.insert(0, "$ " + str(format(round(total_concept[0], 2), ',.2f').translate(trans)))

                    total_entry.config(state="readonly")
                    haber_total_entry.config(state="readonly")
                    debe_total_entry.config(state="readonly")
                    
                    c.execute("""SELECT ID_MOVIMIENTO, FECHA, CONCEPTO, IFNULL(DEBE,0.00) AS DEBE, IFNULL(HABER,0.00) AS HABER FROM Movimientos WHERE CONCEPTO = :concept_name AND FECHA BETWEEN :date_start AND :date_end ORDER BY FECHA ASC""", {'concept_name':searchConcept,'date_start':start_date, 'date_end':end_date})

                    records = c.fetchall()
                
                    clean_table()
                    
                    # Add our data to the screen
                    global count
                    count = 0
                    
                    clean_table()

                    for record in records:
                            trans = str.maketrans('.,', ',.')
                            debe = str(format(record[3], ',.2f').translate(trans))            

                            haber = str(format(record[4], ',.2f').translate(trans))

                            if debe == "0,00":
                                debe = ""

                            if haber == "0,00":
                                haber = ""

                            date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('oddrow',))

                            # increment counter
                            count += 1

                    my_tree.yview_moveto('1.0')

                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
            


        title_name_label.config(text=company_name)
        address_label.config(text=address)

        search_start_date_l = ttk.Label(concept_bet_dates_frame, text="Desde", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_start_date_l.place(x=10, y=90)
        search_start_date = DateEntry(concept_bet_dates_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_start_date.config(state="readonly")
        search_start_date.place(x=10, y=115, height=35)

        search_end_date_l = ttk.Label(concept_bet_dates_frame, text="Hasta", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_end_date_l.place(x=185, y=90)
        search_end_date = DateEntry(concept_bet_dates_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_end_date.config(state="readonly")
        search_end_date.place(x=185, y=115, height=35)

        search_btn = ttk.Button(concept_bet_dates_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=890, y= 113)
        clean_search_btn = ttk.Button(concept_bet_dates_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=1055, y= 113)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        concepts_mov_label = ttk.Label(concept_bet_dates_frame, text="Concepto", style='style_tdata.TLabel', width=40, borderwidth=2, relief="solid", anchor="center")
        concepts_mov_label.place(x=359, y=90)

        concept_bet_dates_frame.var_pant_cbox = StringVar()
        
        search_concept_cmbox = ttk.Combobox(concept_bet_dates_frame, font=("Arial", 16), textvariable=concept_bet_dates_frame.var_pant_cbox, state="readonly", width=40, height=12)
        search_concept_cmbox['values'] = conceptos_list
        search_concept_cmbox.current(0)
        search_concept_cmbox.place(x=359, y=115, height=35)

        export_btn = ttk.Button(concept_bet_dates_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        def exitMovPerConceptBetDates():
            concept_bet_dates_frame.destroy()

        exit_btn = ttk.Button(concept_bet_dates_frame, text="Salir", style='button.TButton', command=exitMovPerConceptBetDates)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(concept_bet_dates_frame, font=("Arial", 15, BOLD), width=14,  justify="center")
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=882, y=600)

        haber_total_entry = Entry(concept_bet_dates_frame, font=("Arial", 15, BOLD), width=14,  justify="center")
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=1120, y=600)

        total_entry = Entry(concept_bet_dates_frame, font=("Arial", 15, BOLD), width=14,  justify="center")
        total_entry.config(state="readonly")
        total_entry.place(x=1005, y=640)

        add_conceptos()
        update_data()
        clean_search()
    except:
        concept_bet_dates_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")
    
def totalmovementsPerConcept():
    try:
        total_concept_frame = Toplevel()
        total_concept_frame.grab_set()
        total_concept_frame.resizable(0,0)
        total_concept_frame.iconbitmap('img\codemy.ico')
        total_concept_frame.title("Totales por Concepto")
        

        ws = total_concept_frame.winfo_screenwidth()
        hs = total_concept_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            total_concept_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            total_concept_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(total_concept_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("CONCEPTO", "DEBE", "HABER", "TOTAL")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("CONCEPTO", anchor=W, width=732)
        my_tree.column("DEBE", anchor=W, width=200)
        my_tree.column("HABER", anchor=W, width=200)
        my_tree.column("TOTAL", anchor=W, width=200)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("TOTAL", text="Total", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT CONCEPTO,IFNULL(SUM(DEBE), 0.00) AS DEBE, IFNULL(SUM(HABER), 0.00) AS HABER FROM Movimientos GROUP BY CONCEPTO")

            records = c.fetchall()
        
            clean_table()
            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[1] == "":
                    debe = float(0)
                else:
                    debe = float(record[1])

                if record[2] == "":
                    haber = float(0)
                else:
                    haber = float(record[2])

                trans = str.maketrans('.,', ',.')
                totalDif =  str(format(round(debe - haber,2), ',.2f').translate(trans)) 
                
                haber = str(format(haber, ',.2f').translate(trans))    
                
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""


                if haber == "0,00":
                    haber = ""

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], debe, haber, totalDif), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], debe, haber, totalDif), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(total_concept_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Totales por Concepto")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(total_concept_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(total_concept_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        c.execute("SELECT NOMBRE_CONCEPTO FROM Conceptos")
        conceptos_list = [item[0] for item in c.fetchall()]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            
            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)
            search_concept_cmbox.current(0)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            search_concept_cmbox.config(state="normal")
            search_concept_cmbox.current(0)
            search_concept_cmbox.config(state="readonly")
            add_conceptos()
            update_data()

        def search_mov():
            conceptSearch = total_concept_frame.var_pant_cbox.get()   

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT IFNULL(CONCEPTO, :concept_name), IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO = :concept_name""", {'concept_name': conceptSearch})

            records = c.fetchall()
            clean_table()

            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[1] == "":
                    debe = float(0)
                else:
                    debe = float(record[1])

                if record[2] == "":
                    haber = float(0)
                else:
                    haber = float(record[2])

                trans = str.maketrans('.,', ',.')
                totalDif =  str(format(round(debe - haber,2), ',.2f').translate(trans))

                haber = str(format(haber, ',.2f').translate(trans))    
                
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""


                if haber == "0,00":
                    haber = ""


                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], debe, haber, totalDif), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], debe, haber, totalDif), tags=('oddrow',))
                # increment counter
                count += 1

            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            

            debe_total_entry.insert(0, "$ " + debe)
            haber_total_entry.insert(0, "$ " + haber)
            total_entry.insert(0, "$ " + totalDif)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Totales por Concepto?", parent=total_concept_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 8)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,0)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(130, 10, 'Totales por Concepto', 0, 0, 'L')
                pdf.multi_cell(190,10," ", 0, 1)
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(148, 3, company_name,0, 0, 'L')
                pdf.multi_cell(190,4," ", 0, 1)
                pdf.set_font("Arial", "B", 9)
                pdf.set_text_color(128,128,128)
                pdf.cell(70, 3, address,0, 0, 'L')
                pdf.set_text_color(128,0,0)
                pdf.multi_cell(190,4," ", 0, 1)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(101, 5, 'Concepto', 1, 0, 'C')
                pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                pdf.cell(30, 5, 'Total', 1, 0, 'C')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                trans = str.maketrans('.,', ',.')
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 8)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(10)
                        pdf.set_auto_page_break(True, 30)
                    pdf.set_font('arial', '', 10)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(190,5," ", 0, 1)
                    pdf.cell(101, 5, record[0], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 10)
                    pdf.set_text_color(0,0,0)
                    pdf.cell(30, 5, record[1], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 10)
                    pdf.set_text_color(255,0,0)
                    pdf.cell(30, 5, record[2], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 10)
                    pdf.set_text_color(0,0,0)
                    if float(str(format(record[3]).translate(trans)).replace(',', '')) < 0.00:
                        pdf.set_text_color(255, 0, 0)
                    pdf.cell(30, 5, record[3], 'B', 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 10)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(71, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(30, 5, debe_total_entry.get(), 1, 0, 'C')
                pdf.cell(30, 5, haber_total_entry.get(), 1, 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)
                pdf.set_font("Arial", "B", 10)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(131, 3, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Saldo Final', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                pdf.output(path + '/Reportes Conceptos/Totales por Concepto - Concepto.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Totales por Concepto - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= total_concept_frame)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        concepts_mov_label = ttk.Label(total_concept_frame, text="Concepto", style='style_tdata.TLabel', width=40, borderwidth=2, relief="solid")
        concepts_mov_label.place(x=10, y=90)

        total_concept_frame.var_pant_cbox = StringVar()
        
        search_concept_cmbox = ttk.Combobox(total_concept_frame, font=("Arial", 16), textvariable=total_concept_frame.var_pant_cbox, state="readonly", width=40, height=12)
        search_concept_cmbox['values'] = conceptos_list
        search_concept_cmbox.current(0)
        search_concept_cmbox.place(x=10, y=115, height=35)

        search_btn = ttk.Button(total_concept_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=540, y= 113)
        clean_search_btn = ttk.Button(total_concept_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=710, y= 113)

        export_btn = ttk.Button(total_concept_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        def exitTotalConcept():
            total_concept_frame.destroy()

        exit_btn = ttk.Button(total_concept_frame, text="Salir", style='button.TButton', command=exitTotalConcept)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(total_concept_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=745, y=630)

        haber_total_entry = Entry(total_concept_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=945, y=630)

        total_entry = Entry(total_concept_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1145, y=630)

        update_data()
        clean_search()
    except:
        total_concept_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def allmovementsPerConcept():
    try:
        all_mov_concept_frame = Toplevel()
        all_mov_concept_frame.grab_set()
        all_mov_concept_frame.resizable(0,0)
        all_mov_concept_frame.iconbitmap('img\codemy.ico')
        all_mov_concept_frame.title("Todos los Movimientos de un Concepto")

        ws = all_mov_concept_frame.winfo_screenwidth()
        hs = all_mov_concept_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            all_mov_concept_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            all_mov_concept_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(all_mov_concept_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=16)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("FECHA", "CONCEPTO", "DEBE", "HABER")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=140)
        my_tree.column("CONCEPTO", anchor=W, width=793)
        my_tree.column("DEBE", anchor=W, width=200)
        my_tree.column("HABER", anchor=W, width=200)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT FECHA, CONCEPTO,IFNULL(DEBE, 0.00) AS DEBE, IFNULL(HABER, 0.00) AS HABER FROM Movimientos ORDER BY FECHA ASC")

            records = c.fetchall()
        
            clean_table()
            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                if record[3] == "":
                    haber = float(0)
                else:
                    haber = float(record[3])

                trans = str.maketrans('.,', ',.')            
                haber = str(format(haber, ',.2f').translate(trans))    
                
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""


                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(all_mov_concept_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Todos los Movimentos de un Concepto")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(all_mov_concept_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(all_mov_concept_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        c.execute("SELECT NOMBRE_CONCEPTO FROM Conceptos")
        conceptos_list = [item[0] for item in c.fetchall()]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT IFNULL(SUM(DEBE), 0.00), IFNULL(SUM(HABER), 0.00) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            
            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)
            search_concept_cmbox.current(0)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            search_concept_cmbox.config(state="normal")
            search_concept_cmbox.current(0)
            search_concept_cmbox.config(state="readonly")
            add_conceptos()
            update_data()

        def search_mov():
            conceptSearch = all_mov_concept_frame.var_pant_cbox.get()   

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("""SELECT FECHA, IFNULL(CONCEPTO,:concept_name), IFNULL(DEBE,0.00) AS DEBE, IFNULL(HABER,0.00) AS HABER FROM Movimientos WHERE CONCEPTO = :concept_name ORDER BY FECHA ASC""", {'concept_name': conceptSearch})

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                if record[3] == "":
                    haber = float(0)
                else:
                    haber = float(record[3])

                trans = str.maketrans('.,', ',.')
                haber = str(format(haber, ',.2f').translate(trans))    
                
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                if record[0] == None:
                    date = ""
                else:
                    date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber), tags=('oddrow',))
                # increment counter
                count += 1


            c.execute("""SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CONCEPTO = :concept_name""", {'concept_name': conceptSearch})
            totals_concept = c.fetchone()

            trans = str.maketrans('.,', ',.')
            debe_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))
            haber_total = str(format(round(totals_concept[1],2), ',.2f').translate(trans))
            total = str(format(round(totals_concept[0] - totals_concept[1],2), ',.2f').translate(trans))

            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos por Concepto?", parent=all_mov_concept_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No es posible exportar registro vacío! Intente con otro Concepto.", parent=all_mov_concept_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Todos los Movimientos de un Concepto', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(148, 3, company_name,0, 0, 'L')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(30, 5, 'Fecha', 1, 0, 'C')
                    pdf.cell(101, 5, 'Concepto', 1, 0, 'C')
                    pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                    pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(10)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 10)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(30, 5, record[0], 'B', 0, 'C')
                        pdf.cell(101, 5, record[1], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 10)
                        pdf.set_text_color(0,0,0)
                        pdf.cell(30, 5, record[2], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 10)
                        pdf.set_text_color(255,0,0)
                        pdf.cell(30, 5, record[3], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)  
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(101, 5, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, debe_total_entry.get(), 1, 0, 'C')
                    pdf.cell(30, 5, haber_total_entry.get(), 1, 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(116, 3, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Saldo Final', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                    pdf.output(path + '/Reportes Conceptos/Movimientos por Concepto - Concepto.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Movimientos por Concepto - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= all_mov_concept_frame)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        concepts_mov_label = ttk.Label(all_mov_concept_frame, text="Concepto", style='style_tdata.TLabel', width=40, borderwidth=2, relief="solid", anchor="center")
        concepts_mov_label.place(x=10, y=90)

        all_mov_concept_frame.var_pant_cbox = StringVar()
        
        search_concept_cmbox = ttk.Combobox(all_mov_concept_frame, font=("Arial", 16), textvariable=all_mov_concept_frame.var_pant_cbox, state="readonly", width=40, height=12)
        search_concept_cmbox['values'] = conceptos_list
        search_concept_cmbox.current(0)
        search_concept_cmbox.place(x=10, y=115, height=35)

        search_btn = ttk.Button(all_mov_concept_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=540, y= 113)
        clean_search_btn = ttk.Button(all_mov_concept_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=710, y= 113)

        export_btn = ttk.Button(all_mov_concept_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        def exitMovPerConcept():
            all_mov_concept_frame.destroy()

        exit_btn = ttk.Button(all_mov_concept_frame, text="Salir", style='button.TButton', command=exitMovPerConcept)
        exit_btn.place(x=1180, y=690)

        debe_total_entry = Entry(all_mov_concept_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=942, y=600)

        haber_total_entry = Entry(all_mov_concept_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=1145, y=600)

        total_entry = Entry(all_mov_concept_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1045, y=640)

        update_data()
        clean_search()
    except:
        all_mov_concept_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def mov_debe():
    try:
        mov_debe_frame = Toplevel()
        mov_debe_frame.grab_set()
        mov_debe_frame.resizable(0,0)
        mov_debe_frame.iconbitmap('img\codemy.ico')
        mov_debe_frame.title("Movimientos del Debe")

        ws = mov_debe_frame.winfo_screenwidth()
        hs = mov_debe_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            mov_debe_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            mov_debe_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(mov_debe_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=165)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=18)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("FECHA", "CONCEPTO", "DEBE")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=140)
        my_tree.column("CONCEPTO", anchor=W, width=800)
        my_tree.column("DEBE", anchor=W, width=395)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT FECHA, CONCEPTO, DEBE AS DEBE FROM Movimientos WHERE DEBE IS NOT NULL AND DEBE IS NOT 0.00 ORDER BY FECHA ASC")

            records = c.fetchall()
        
            clean_table()
            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                trans = str.maketrans('.,', ',.')            
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(mov_debe_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Movimientos del Debe")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(mov_debe_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(mov_debe_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE) FROM Movimientos")
            records = c.fetchone()

        
            trans = str.maketrans('.,', ',.')
            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            debe_total_entry.delete(0, END)
            debe_total_entry.insert(0, "$ " + debe_total)
            debe_total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            importe_min_entry.delete(0, END)
            importe_max_entry.delete(0, END)
            add_conceptos()
            update_data()

        def search_mov():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT MIN(DEBE), MAX(DEBE) FROM Movimientos WHERE DEBE IS NOT NULL AND DEBE IS NOT 0.00")
            min_max_imp = c.fetchone()
            
            if importe_min_entry.get() == "":
                imp_min = min_max_imp[0]
            else: 
                imp_min = float(str(importe_min_entry.get()).replace(',', '.'))


            if importe_max_entry.get() == "":
                imp_max = min_max_imp[1]
            else:
                imp_max = float(str(importe_max_entry.get()).replace(',', '.'))

            c.execute("""SELECT FECHA, CONCEPTO, DEBE FROM Movimientos WHERE DEBE IS NOT NULL AND DEBE IS NOT 0.00 AND DEBE >= :imp_min AND DEBE <= :imp_max ORDER BY FECHA ASC""", {'imp_min': imp_min, 'imp_max': imp_max})

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                trans = str.maketrans('.,', ',.')            
                debe = str(format(debe, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if record[0] == None:
                    date = ""
                else:
                    date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe), tags=('oddrow',))
                # increment counter
                count += 1


            c.execute("""SELECT IFNULL(SUM(DEBE),0.00) FROM Movimientos WHERE DEBE IS NOT NULL AND DEBE >= :imp_min AND DEBE <= :imp_max ORDER BY FECHA ASC""", {'imp_min': imp_min, 'imp_max': imp_max})
            totals_concept = c.fetchone()

            trans = str.maketrans('.,', ',.')
            debe_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))

            debe_total_entry.config(state="normal")
            debe_total_entry.delete(0, END)
            debe_total_entry.insert(0, "$ " + debe_total)
            debe_total_entry.config(state="readonly")

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos del Debe?", parent=mov_debe_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No es posible exportar registro vacío! Intente con otro Concepto.", parent=mov_debe_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Movimientos del Debe', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(118, 3, company_name,0, 0, 'L')
                    pdf.cell(148, 3, "Importe desde [$" + importe_min_entry.get() + "] hasta [$" + importe_max_entry.get() + "]",0, 0, 'L')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 12)
                    pdf.cell(30, 5, 'Fecha', 1, 0, 'C')
                    pdf.cell(131, 5, 'Concepto', 1, 0, 'C')
                    pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(10)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 12)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(30, 5, record[0], 'B', 0, 'C')
                        pdf.cell(131, 5, record[1], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 12)
                        pdf.cell(30, 5, record[2], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)  
                    pdf.set_font("Arial", "B", 12)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(131, 5, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, debe_total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                    pdf.output(path + '/Reportes Conceptos/Movimientos Debe - Concepto.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Movimientos Debe - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= mov_debe_frame)

        title_name_label.config(text=company_name)
        address_label.config(text=address)


        def only_number_imp(inp):
            try:
                if len(inp) > 10:
                    return False
                elif "." in inp:
                    return False
                else:
                    float(str(inp).replace(',', '.'))
            except:
                if inp == "":
                    return True
                else:
                    return False
            return True


        num_validation = mov_debe_frame.register(only_number_imp)

        def exitMovDeb():
            mov_debe_frame.destroy()

        importe_min_label = ttk.Label(mov_debe_frame, text="Importe Min", style='style_tdata.TLabel', width=12, borderwidth=2, relief="solid", anchor="center")
        importe_min_label.place(x=10, y=90)
        importe_min_entry = ttk.Entry(mov_debe_frame, font=("Arial", 16, BOLD), width=12)
        importe_min_entry.config(validate="key", validatecommand=(num_validation, "%P"))
        importe_min_entry.place(x=10, y=115, height=35)

        importe_max_label = ttk.Label(mov_debe_frame, text="Importe Max", style='style_tdata.TLabel', width=12, borderwidth=2, relief="solid", anchor="center")
        importe_max_label.place(x=190, y=90)
        importe_max_entry = ttk.Entry(mov_debe_frame, font=("Arial", 16, BOLD), width=12)
        importe_max_entry.config(validate="key", validatecommand=(num_validation, "%P"))
        importe_max_entry.place(x=190, y=115, height=35)

        search_btn = ttk.Button(mov_debe_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=365, y= 113)
        clean_search_btn = ttk.Button(mov_debe_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=535, y= 113)

        export_btn = ttk.Button(mov_debe_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        exit_btn = ttk.Button(mov_debe_frame, text="Salir", style='button.TButton', command=exitMovDeb)
        exit_btn.place(x=1180, y=690)

        debe_total_entry = Entry(mov_debe_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=950, y=660)

        update_data()
        clean_search()
    except:
        mov_debe_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def mov_haber():
    try:
        mov_haber_frame = Toplevel()
        mov_haber_frame.grab_set()
        mov_haber_frame.resizable(0,0)
        mov_haber_frame.iconbitmap('img\codemy.ico')
        mov_haber_frame.title("Movimientos del Haber")

        ws = mov_haber_frame.winfo_screenwidth()
        hs = mov_haber_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            mov_haber_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            mov_haber_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(mov_haber_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=165)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=18)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("FECHA", "CONCEPTO", "HABER")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=140)
        my_tree.column("CONCEPTO", anchor=W, width=800)
        my_tree.column("HABER", anchor=W, width=395)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Concepto", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT FECHA, CONCEPTO, HABER AS HABER FROM Movimientos WHERE HABER IS NOT NULL AND HABER IS NOT 0.00 ORDER BY FECHA ASC")

            records = c.fetchall()
        
            clean_table()
            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    haber = float(0)
                else:
                    haber = float(record[2])

                trans = str.maketrans('.,', ',.')            
                haber = str(format(haber, ',.2f').translate(trans))

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], haber), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], haber), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(mov_haber_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Movimientos del Haber")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(mov_haber_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(mov_haber_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(HABER) FROM Movimientos")
            records = c.fetchone()

        
            trans = str.maketrans('.,', ',.')
            haber_total = records[0]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            haber_total_entry.config(state="normal")
            haber_total_entry.delete(0, END)
            haber_total_entry.insert(0, "$ " + haber_total)
            haber_total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            importe_min_entry.delete(0, END)
            importe_max_entry.delete(0, END)
            add_conceptos()
            update_data()

        def search_mov():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT MIN(HABER), MAX(HABER) FROM Movimientos WHERE HABER IS NOT NULL AND HABER IS NOT 0.00")
            min_max_imp = c.fetchone()
            
            if importe_min_entry.get() == "":
                imp_min = min_max_imp[0]
            else: 
                imp_min = float(str(importe_min_entry.get()).replace(',', '.'))


            if importe_max_entry.get() == "":
                imp_max = min_max_imp[1]
            else:
                imp_max = float(str(importe_max_entry.get()).replace(',', '.'))

            c.execute("""SELECT FECHA, CONCEPTO, HABER FROM Movimientos WHERE HABER IS NOT NULL AND HABER IS NOT 0.00 AND HABER >= :imp_min AND HABER <= :imp_max ORDER BY FECHA ASC""", {'imp_min': imp_min, 'imp_max': imp_max})

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0


            for record in records:
                if record[2] == "":
                    haber = float(0)
                else:
                    haber = float(record[2])

                trans = str.maketrans('.,', ',.')            
                haber = str(format(haber, ',.2f').translate(trans))

                if haber == "0,00":
                    haber = ""

                if record[0] == None:
                    date = ""
                else:
                    date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], haber), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], haber), tags=('oddrow',))
                # increment counter
                count += 1


            c.execute("""SELECT IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE HABER IS NOT NULL AND HABER >= :imp_min AND HABER <= :imp_max ORDER BY FECHA ASC""", {'imp_min': imp_min, 'imp_max': imp_max})
            totals_concept = c.fetchone()

            trans = str.maketrans('.,', ',.')
            haber_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))

            haber_total_entry.config(state="normal")
            haber_total_entry.delete(0, END)
            haber_total_entry.insert(0, "$ " + haber_total)
            haber_total_entry.config(state="readonly")

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos del Haber?", parent=mov_haber_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No es posible exportar registro vacío! Intente con otro Concepto.", parent=mov_haber_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Movimientos del Haber', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(118, 3, company_name,0, 0, 'L')
                    pdf.cell(148, 3, "Importe desde [$" + importe_min_entry.get() + "] hasta [$" + importe_max_entry.get() + "]",0, 0, 'L')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 12)
                    pdf.cell(30, 5, 'Fecha', 1, 0, 'C')
                    pdf.cell(131, 5, 'Concepto', 1, 0, 'C')
                    pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(10)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 12)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(30, 5, record[0], 'B', 0, 'C')
                        pdf.cell(131, 5, record[1], 'B', 0, 'C')
                        pdf.set_font('arial', 'B', 12)
                        pdf.set_text_color(255,0,0)
                        pdf.cell(30, 5, record[2], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)  
                    pdf.set_font("Arial", "B", 12)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(131, 5, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, haber_total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Conceptos"):
                        os.makedirs(path + "/Reportes Conceptos")
                    pdf.output(path + '/Reportes Conceptos/Movimientos Haber - Concepto.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Movimientos Haber - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= mov_haber_frame)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        def only_number_imp(inp):
            try:
                if len(inp) > 10:
                    return False
                elif "." in inp:
                    return False
                else:
                    float(str(inp).replace(',', '.'))
            except:
                if inp == "":
                    return True
                else:
                    return False
            return True

        num_validation = mov_haber_frame.register(only_number_imp)

        def exitMovBetDate():
            mov_haber_frame.destroy()

        importe_min_label = ttk.Label(mov_haber_frame, text="Importe Min", style='style_tdata.TLabel', width=12, borderwidth=2, relief="solid", anchor="center")
        importe_min_label.place(x=10, y=90)
        importe_min_entry = ttk.Entry(mov_haber_frame, font=("Arial", 16, BOLD), width=12)
        importe_min_entry.config(validate="key", validatecommand=(num_validation, "%P"))
        importe_min_entry.place(x=10, y=115, height=35)

        importe_max_label = ttk.Label(mov_haber_frame, text="Importe Max", style='style_tdata.TLabel', width=12, borderwidth=2, relief="solid", anchor="center")
        importe_max_label.place(x=190, y=90)
        importe_max_entry = ttk.Entry(mov_haber_frame, font=("Arial", 16, BOLD), width=12)
        importe_max_entry.config(validate="key", validatecommand=(num_validation, "%P"))
        importe_max_entry.place(x=190, y=115, height=35)

        search_btn = ttk.Button(mov_haber_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=365, y= 113)
        clean_search_btn = ttk.Button(mov_haber_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=535, y= 113)

        export_btn = ttk.Button(mov_haber_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)

        exit_btn = ttk.Button(mov_haber_frame, text="Salir", style='button.TButton', command=exitMovBetDate)
        exit_btn.place(x=1180, y=690)

        haber_total_entry = Entry(mov_haber_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=950, y=660)

        update_data()
        clean_search()
    except:
        mov_haber_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def mayorConceptos():
    try:
        mayorConceptos_frame = Toplevel()
        mayorConceptos_frame.grab_set()
        mayorConceptos_frame.resizable(0,0)
        mayorConceptos_frame.iconbitmap('img\codemy.ico')
        mayorConceptos_frame.title("Mayor por Conceptos")

        ws = mayorConceptos_frame.winfo_screenwidth()
        hs = mayorConceptos_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            mayorConceptos_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            mayorConceptos_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#395B64")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#347083")])

        # Create a Treeview Frame
        tree_frame = Frame(mayorConceptos_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("FECHA", "CONCEPTO", "DEBE", "HABER", "SALDO")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=140)
        my_tree.column("CONCEPTO", anchor=W, width=655)
        my_tree.column("DEBE", anchor=W, width=180)
        my_tree.column("HABER", anchor=W, width=180)
        my_tree.column("SALDO", anchor=W, width=180)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CONCEPTO", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("SALDO", text="Saldo", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#A5C9CA")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT FECHA, CONCEPTO, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos GROUP BY FECHA, CONCEPTO ORDER BY CUENTA ASC")

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0

            for record in records:
                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                if record[3] == "":
                    haber = float(0)
                else:
                    haber = float(record[3])

                saldoTotal = round(debe - haber, 2)

                trans = str.maketrans('.,', ',.')
                haber = str(format(haber, ',.2f').translate(trans))    
                debe = str(format(debe, ',.2f').translate(trans))
                saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                if saldoTotal == "0,00":
                    saldoTotal = ""

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber, saldoTotal), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber, saldoTotal), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(mayorConceptos_frame, foreground="#395B64", style="mov_cajat.TLabel", text="Mayor por Conceptos")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(mayorConceptos_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(mayorConceptos_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            
            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("DELETE FROM Filters")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            add_conceptos()
            update_data()

        def filters():
            filter_frame = Toplevel()
            filter_frame.grab_set()
            filter_frame.iconbitmap('img\codemy.ico')
            filter_frame.title("Filtrar Concepto")
            w = 700
            h = 300

            ws = filter_frame.winfo_screenwidth()
            hs = filter_frame.winfo_screenheight()

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)

            filter_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

            # Configure the Treeview Colors
            style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3", font=("Arial", 14))

            style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#800000")

            # Change Selected Color
            style.map('Treeview',
                background=[('selected', "#d1d1e0")])

            # Create a Treeview Frame
            tree_frame_filter = Frame(filter_frame)
            tree_frame_filter.place(x=8, y=90)

            # Create a Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame_filter, width=20)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            my_tree_filter = ttk.Treeview(tree_frame_filter, yscrollcommand=tree_scroll.set, selectmode="extended", height=5)
            my_tree_filter.pack()

            # Configure the Scrollbar
            tree_scroll.config(command=my_tree_filter.yview)

            # Define Our Columns
            my_tree_filter['columns'] = ("ID", "FILTRO", "CONCEPTO")

            # Format Our Columns
            my_tree_filter.column("#0", width=0, stretch=NO)
            my_tree_filter.column("ID", width=0, stretch=NO)
            my_tree_filter.column("FILTRO", anchor=W, width=250)
            my_tree_filter.column("CONCEPTO", anchor=W, width=420)

            # Create Headings
            my_tree_filter.heading("#0", text="", anchor=W)
            my_tree_filter.heading("ID", text="", anchor=W)
            my_tree_filter.heading("FILTRO", text="Filtro", anchor=W)
            my_tree_filter.heading("CONCEPTO", text="Cuenta", anchor=W)
            
            # Create Striped Row Tags
            my_tree_filter.tag_configure('oddrow', background="white")
            my_tree_filter.tag_configure('evenrow', background="grey")

            titleLabel = ttk.Label(filter_frame, style='mov_cajat.TLabel', text="Filtros", foreground="#800000")
            titleLabel.place(x=8, y=5)

            filter_frame.var_filter_cbox = StringVar()
            filterOpt = []
            filterOpt.append("Igual a")
            filterOpt.append("Distinto de")
        
            filtro_cmbox = ttk.Combobox(filter_frame, font=("Arial", 14), textvariable=filter_frame.var_filter_cbox, state="readonly", width=15, height=15)
            filtro_cmbox['values'] = filterOpt
            filtro_cmbox.set("[Filtro...]")
            filtro_cmbox.place(x=8, y=40)

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT DISTINCT NOMBRE_CONCEPTO FROM Conceptos")
            conceptos_list = [item[0] for item in c.fetchall()]
            

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            filter_frame.var_conceptos_cbox = StringVar()

            conceptos_cmbox = ttk.Combobox(filter_frame, font=("Arial", 14), textvariable=filter_frame.var_conceptos_cbox, state="readonly", width=25, height=15)
            conceptos_cmbox['values'] = conceptos_list
            conceptos_cmbox.set("[Cuenta...]")
            conceptos_cmbox.place(x=220, y=40)

            def cleanFilter_table():
                for item in my_tree_filter.get_children():
                    my_tree_filter.delete(item)

            def add_actualFilter():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)

                # Create a cursor instance
                c = conn.cursor()

                c.execute("SELECT ID, Tipo, Cuenta FROM Filters")

                actualFilters = c.fetchall()

                if actualFilters != None:         
                    cleanFilter_table()


                    # Add our data to the screen
                    global count
                    count = 0

                    for record in actualFilters:
                        if count % 2 == 0:
                            my_tree_filter.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                        else:
                            my_tree_filter.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
                        # increment counter
                        count += 1

                    idFilter_entry.delete(0, END)
                    my_tree_filter.yview_moveto('1.0')
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close() 
                    

            add_actualFilter() 


            def selectedFilter(e):
                selected_filter = my_tree_filter.focus()
                if selected_filter != "":
                    # Grab record Number
                    selected = my_tree_filter.focus()
                    # Grab record values
                    values = my_tree_filter.item(selected, 'values')
                    idFilter_entry.delete(0, END)
                    idFilter_entry.insert(0, values[0])


            #Bind the treeview
            my_tree_filter.bind("<ButtonRelease-1>", selectedFilter)

            def addfilter():
                try:
                    idFilter_entry.delete(0, END)
                    if filter_frame.var_conceptos_cbox.get() == "[Concepto...]" or filter_frame.var_filter_cbox.get() == "[Filtro...]":
                        messagebox.showerror(title="Ups.. Ups..", message="El campo [Filtro..] y [Concepto...] se encuentran vacíos. Son obligatorios.", parent=filter_frame)
                    elif len(my_tree_filter.get_children()) > 5:
                        messagebox.showerror(title="Ups.. Ups..", message="Se alcanzó el límite de condiciones [5]. Elimine alguna si desea filtrar.", parent=filter_frame)
                    else:
                        filterCuenta = filter_frame.var_conceptos_cbox.get()
                        filterSelect = filter_frame.var_filter_cbox.get()

                        # Create a database or connect to one that exists
                        conn = sqlite3.connect(db_name)

                        # Create a cursor instance
                        c = conn.cursor()

                        sql_addFilter = "INSERT INTO Filters (Tipo, Cuenta) VALUES (?,?)"
                        sql_argsFilter = (filterSelect, filterCuenta)
                        c.execute(sql_addFilter, sql_argsFilter)

                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close() 

                        add_actualFilter()
                except:
                    messagebox.showerror(title="Ups.. Ups..", message="¡No es posible aplicar dos veces un filtro al mismo [Concepto]! Intente con otro registro.", parent=filter_frame)
                        

            def delFilter():
                try:
                    if idFilter_entry.get() == "":
                        messagebox.showerror(title="Ups.. Ups..", message="¡Debe seleccionar el filtro a eliminar primero!", parent=filter_frame)
                    else:
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect(db_name)

                        # Create a cursor instance
                        c = conn.cursor()

                        query_del = "DELETE FROM Filters WHERE ID = ?"
                        args_del = (idFilter_entry.get())
                        c.execute(query_del, [args_del])

                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close() 

                        add_actualFilter()
                except:
                    messagebox.showerror(title="Ups.. Ups..", message="Error al eliminar! Intente nuevamente.", parent=filter_frame)



                    
                    
            def acceptFilter():
                try:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)
                    # Create a cursor instance
                    c = conn.cursor()

                    def convertTuple(tup):
                        str = ','.join(tup)
                        return str

                    c.execute("SELECT CUENTA FROM FILTERS WHERE Tipo = 'Distinto de'")

                    distrecords = c.fetchall()
                    distList = ""

                    if distrecords == []:
                        distList = "-"
                    else:
                        for record in distrecords:
                            if distList != "":
                                distList = distList + "', "    
                            distList = distList + "'" + convertTuple(record)
                        distList = distList + "'"
                    

                    c.execute("SELECT CUENTA FROM FILTERS WHERE Tipo = 'Igual a'")
                    

                    
                    eqrecords = c.fetchall()
                    eqList = ""

                    if eqrecords == []:
                        eqList = "-"
                    else:
                        for record in eqrecords:
                            if eqList != "":
                                eqList = eqList + "', "    
                            eqList = eqList + "'" + convertTuple(record)
                        eqList = eqList + "'"

        
                    if distList == "-":
                        query = "SELECT FECHA, CONCEPTO, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO IN " + "(" + eqList + ")" +  " GROUP BY FECHA, CONCEPTO ORDER BY CONCEPTO ASC"
                        c.execute(query)
                    elif eqList == "-":
                        query = "SELECT FECHA, CONCEPTO, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO NOT IN " + "(" + distList + ")" + " GROUP BY FECHA, CONCEPTO ORDER BY CONCEPTO ASC"
                        c.execute(query)
                    else:
                        query = "SELECT FECHA, CONCEPTO, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO IN " + "(" + eqList + ")" + " AND CONCEPTO NOT IN " + "(" + distList + ")" + " GROUP BY FECHA, CONCEPTO ORDER BY CONCEPTO ASC"
                        c.execute(query)

                    records = c.fetchall()
                    
                    if records != []:
                    
                        clean_table()

                        # Add our data to the screen
                        global count
                        count = 0


                        for record in records:
                            if record[2] == "":
                                debe = float(0)
                            else:
                                debe = float(record[2])

                            if record[3] == "":
                                haber = float(0)
                            else:
                                haber = float(record[3])

                            saldoTotal = round(debe - haber, 2)

                            trans = str.maketrans('.,', ',.')
                            haber = str(format(haber, ',.2f').translate(trans))    
                            debe = str(format(debe, ',.2f').translate(trans))
                            saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                            if debe == "0,00":
                                debe = ""

                            if haber == "0,00":
                                haber = ""

                            if saldoTotal == "0,00":
                                saldoTotal = ""

                            date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber, saldoTotal), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(date, record[1], debe, haber, saldoTotal), tags=('oddrow',))
                            # increment counter
                            count += 1

                        if distList == "-":
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CONCEPTO IN " + "(" + eqList + ")"
                            c.execute(query)
                        elif eqList == "-":
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CONCEPTO NOT IN " + "(" + distList + ")"
                            c.execute(query)
                        else:
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CONCEPTO IN " + "(" + eqList + ")" + " AND CONCEPTO NOT IN " + "(" + distList + ")"
                            c.execute(query)

                        totals_concept = c.fetchone()

                        trans = str.maketrans('.,', ',.')
                        debe_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))
                        haber_total = str(format(round(totals_concept[1],2), ',.2f').translate(trans))
                        total = str(format(round(totals_concept[0] - totals_concept[1],2), ',.2f').translate(trans))

                        debe_total_entry.config(state="normal")
                        haber_total_entry.config(state="normal")
                        total_entry.config(state="normal")
                        

                        debe_total_entry.delete(0, END)
                        haber_total_entry.delete(0, END)
                        total_entry.delete(0, END)
                        

                        debe_total_entry.insert(0, "$ " + debe_total)
                        haber_total_entry.insert(0, "$ " + haber_total)
                        total_entry.insert(0, "$ " + total)

                        debe_total_entry.config(state="readonly")
                        haber_total_entry.config(state="readonly")
                        total_entry.config(state="readonly")
                        filter_frame.destroy()
                        

                        my_tree.yview_moveto('1.0')
                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close()
                    else:
                        messagebox.showerror(title="Ups.. Ups..", message="No se encontraron resultados! Intente con otro [Concepto].", parent=filter_frame)
                except:
                    messagebox.showerror(title="Ups.. Ups..", message="Error en la búsqueda! Intente nuevamente.", parent=filter_frame)
                

            def cancelFilter():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("DELETE FROM Filters")

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                add_conceptos()
                filter_frame.destroy()          

            

            addfilter_btn = ttk.Button(filter_frame, text="Agregar", style='button.TButton', command=addfilter)
            addfilter_btn.place(x=540, y=38)

            acceptfilter_btn = ttk.Button(filter_frame, text="Aceptar", style='button.TButton', command=acceptFilter)
            acceptfilter_btn.place(x=220, y=250)

            delfilter_btn = ttk.Button(filter_frame, text="Eliminar", style='button.TButton', command=delFilter)
            delfilter_btn.place(x=380, y=250)

            cancelfilter_btn = ttk.Button(filter_frame, text="Cancelar", style='button.TButton', command=cancelFilter)
            cancelfilter_btn.place(x=540, y=250)


        def onClosingFilters():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("DELETE FROM Filters")

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                mayorConceptos_frame.destroy()

        mayorConceptos_frame.protocol("WM_DELETE_WINDOW", onClosingFilters)

        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Mayor por Concepto?", parent=mayorConceptos_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 10)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,5)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(70, 10, 'Mayor por Conceptos', 0, 2, 'L')
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(70, 5, company_name,0, 2, 'L')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                concepto = 0
                contador = 0
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 10)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(40)
                        pdf.set_auto_page_break(True, 30)
                    if record[1] != concepto:
                        if contador != 0:
                            # Create a database or connect to one that exists
                            conn = sqlite3.connect(db_name)
                            # Create a cursor instance
                            c = conn.cursor()
                            
                            c.execute("""SELECT IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO = :concepto_name""", {'concepto_name': concepto})
                            records = c.fetchone()
                            totalCuenta = round(records[0] - records[1], 2)
                            trans = str.maketrans('.,', ',.')
                            total = str(format(totalCuenta, ',.2f').translate(trans)) 
                            # Commit changes
                            conn.commit()
                            # Close our connection
                            conn.close()
                            pdf.multi_cell(190,8," ", 0, 1)  
                            pdf.set_font("Arial", "B", 12)
                            pdf.set_text_color(255,255,255)
                            pdf.set_fill_color(0,0,0)
                            pdf.cell(30, 0, '', 0, 0, 'C')
                            pdf.cell(97, 5, ' ', 0, 0, 'C')
                            pdf.cell(30, 5, 'Total Cuenta', 1, 0, 'C', fill=True)
                            pdf.set_text_color(0)
                            pdf.cell(38, 5, "$" + total, 1, 0, 'C')
                        if pdf.get_y() > 180:
                            pdf.set_auto_page_break(True, 80)
                        pdf.multi_cell(100,8," ", 0, 1) 
                        pdf.set_font('arial', 'B', 14)
                        pdf.set_text_color(95, 0, 0)
                        pdf.multi_cell(100,5," ", 0, 1) 
                        pdf.cell(210, 15, record[1], 0, 0, 'L')
                        pdf.multi_cell(100,5," ", 1, 1)
                        pdf.cell(65, 7, "", "", 0, 'C')
                        pdf.multi_cell(130,7," ", 'B', 0)
                        pdf.cell(35, 5, "", "", 0, 'C')
                        pdf.cell(40, 5, 'Fecha', 1, 0, 'C')
                        pdf.cell(40, 5, 'Debe', 1, 0, 'C')
                        pdf.cell(40, 5, 'Haber', 1, 0, 'C')
                        pdf.cell(40, 5, 'Saldo', 1, 0, 'C')
                        contador = 1
                        concepto = record[1]
                    pdf.set_font('arial', '', 12)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(100,7," ", 0, 1)
                    pdf.cell(35, 5, "", 'B', 0, 'C')
                    pdf.cell(40, 5, record[0], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 12)
                    pdf.cell(40, 5, record[2], 'B', 0, 'C')
                    pdf.cell(40, 5, record[3], 'B', 0, 'C')
                    pdf.set_text_color(255, 0, 0)
                    pdf.cell(40, 5, record[4], 'B', 0, 'C')
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()
                c.execute("""SELECT IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CONCEPTO = :concepto_name""", {'concepto_name': concepto})
                records = c.fetchone()
                totalCuenta = round(records[0] - records[1], 2)
                trans = str.maketrans('.,', ',.')
                total = str(format(totalCuenta, ',.2f').translate(trans)) 
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 12)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(97, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total Cuenta', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(38, 5, "$" + total, 1, 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 12)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(82, 82, 122)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(97, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(38, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Conceptos"):
                    os.makedirs(path + "/Reportes Conceptos")
                pdf.output(path + '/Reportes Conceptos/Mayor por Concepto - Concepto.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Mayor por Concepto - Concepto.pdf] se exportó correctamente en el Escritorio.", parent= mayorConceptos_frame)


        title_name_label.config(text=company_name)
        address_label.config(text=address)

        idFilter_entry = Entry(mayorConceptos_frame, font=("Arial", 14, BOLD), width=30, foreground="grey")
        
        search_btn = ttk.Button(mayorConceptos_frame, text="Filtros", style='button.TButton', command=filters)
        search_btn.place(x=8, y= 103)
        clean_search_btn = ttk.Button(mayorConceptos_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=188, y= 103)

        export_btn = ttk.Button(mayorConceptos_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=103)

        def exitMovPerConcept():
            mayorConceptos_frame.destroy()

        exit_btn = ttk.Button(mayorConceptos_frame, text="Salir", style='button.TButton', command=exitMovPerConcept)
        exit_btn.place(x=1180, y=690)

        debe_total_entry = Entry(mayorConceptos_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=795, y=630)

        haber_total_entry = Entry(mayorConceptos_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=975, y=630)

        total_entry = Entry(mayorConceptos_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1165, y=630)

        update_data()
        clean_search()
    except:
        mayorConceptos_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def movimientosCuenta():
    try:
        cuenta_mov_frame = Toplevel()
        cuenta_mov_frame.grab_set()
        cuenta_mov_frame.resizable(0,0)
        cuenta_mov_frame.iconbitmap('img\codemy.ico')
        cuenta_mov_frame.title("Todos los Movimientos de Caja por Cuentas")

        ws = cuenta_mov_frame.winfo_screenwidth()
        hs = cuenta_mov_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            cuenta_mov_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            cuenta_mov_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#B25068")])

        # Create a Treeview Frame
        tree_frame = Frame(cuenta_mov_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=16)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CUENTA", "DEBE", "HABER")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=140)
        my_tree.column("CUENTA", anchor=W, width=793)
        my_tree.column("DEBE", anchor=W, width=200)
        my_tree.column("HABER", anchor=W, width=200)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CUENTA", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#e0b8c2")

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            c.execute("SELECT MAX(FECHA), MIN(FECHA) FROM Movimientos")
            dates_sql = c.fetchone()
            max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
            min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

            search_end_date.config(state="normal")
            search_start_date.config(state="normal")

            search_end_date.delete(0, END)
            search_start_date.delete(0, END)

            search_end_date.insert(0, max_date)
            search_start_date.insert(0, min_date)

            search_end_date.config(state="readonly")
            search_start_date.config(state="readonly")
            
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos ORDER BY FECHA ASC")

            records = c.fetchall()

            clean_table()
            
            # Add our data to the screen
            global count
            count = 0
            

            for record in records:       
                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])
                trans = str.maketrans('.,', ',.')
                debe = str(format(debe, ',.2f').translate(trans))            

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])
                haber = str(format(haber, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('oddrow',))

                # increment counter
                count += 1

                    

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(cuenta_mov_frame, foreground="#774360", style="mov_cajat.TLabel", text="Todos los Movimientos de Caja por Cuentas")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(cuenta_mov_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(cuenta_mov_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos de Caja por Cuenta?", parent=cuenta_mov_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 10)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,5)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(70, 10, 'Todos los Movimientos de Caja por Cuentas', 0, 2, 'L')
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(70, 5, company_name,0, 2, 'L')
                pdf.set_font("Arial", "B", 9)
                pdf.set_text_color(128,128,128)
                pdf.cell(70, 5, address,0, 2, 'L')
                pdf.set_text_color(128,0,0)
                pdf.set_font("Arial", "B", 12)
                pdf.cell(30, 5, 'Fecha', 1, 0, 'C')
                pdf.cell(90, 5, 'Cuenta', 1, 0, 'C')
                pdf.cell(35, 5, 'Debe', 1, 0, 'C')
                pdf.cell(35, 5, 'Haber', 1, 0, 'C')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                first_date = 0
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 10)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(20)
                        pdf.set_auto_page_break(True, 30)
                    if record[1] != first_date:
                        pdf.multi_cell(100,8," ", 0, 1) 
                        pdf.set_font('arial', 'B', 12)
                        pdf.set_text_color(95, 0, 0)
                        pdf.multi_cell(100,5," ", 0, 1) 
                        pdf.cell(30, 10, record[1], 0, 0, 'C')
                        pdf.cell(0, 5, " ", 'B', 0, 'C')
                        first_date = record[1]              
                    pdf.set_font('arial', '', 10)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(100,5," ", 0, 1)
                    pdf.cell(30, 5, "", 'B', 0, 'C')
                    if len(record[2]) > 30:
                        pdf.set_font('arial', '', 8)
                    pdf.cell(90, 5, record[2], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 10)
                    pdf.cell(35, 5, record[3], 'B', 0, 'C')
                    pdf.set_text_color(255, 0, 0)
                    pdf.cell(35, 5, record[4], 'B', 0, 'C')           
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 10)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(99, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Cuentas"):
                    os.makedirs(path + "/Reportes Cuentas")
                pdf.output(path + '/Reportes Cuentas/Todos Los Movimientos - Cuenta.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Todos Los Movimientos - Cuenta.pdf] se exportó correctamente.", parent= cuenta_mov_frame)


        def exitAllMov():
            cuenta_mov_frame.destroy()

        def clean_search():
            add_conceptos()
            update_data()


        def search_cuenta():
            try:
                start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')  
                end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d') 

                if start_date > end_date:
                    messagebox.showerror(title="Ups..Ups..", message="¡Error! La fecha DESDE no puede ser mayor a la fecha HASTA, intenta nuevamente.", parent=cuenta_mov_frame)
                else:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)

                    # Create a cursor instance
                    c = conn.cursor()

                    clean_table()
                    

                    c.execute("""SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER FROM Movimientos WHERE FECHA BETWEEN :start_date AND :end_date ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})

                    records = c.fetchall()
                    
                    # Add our data to the screen
                    global count
                    count = 0
                    

                    for record in records:       
                        if record[3] == "":
                            debe = float(0)
                        else:
                            debe = float(record[3])
                        trans = str.maketrans('.,', ',.')
                        debe = str(format(debe, ',.2f').translate(trans))            

                        if record[4] == "":
                            haber = float(0)
                        else:
                            haber = float(record[4])
                        haber = str(format(haber, ',.2f').translate(trans))

                        if debe == "0,00":
                            debe = ""

                        if haber == "0,00":
                            haber = ""

                        date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                        if count % 2 == 0:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('evenrow',))
                        else:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber), tags=('oddrow',))

                        # increment counter
                        count += 1

                    c.execute("""SELECT IFNULL(SUM(DEBE),0.0) AS DEBE, IFNULL(SUM(HABER),0.0) AS HABER FROM Movimientos WHERE FECHA BETWEEN :start_date AND :end_date ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})
                    totalMov = c.fetchone()
                    totalDebe = totalMov[0]
                    totalHaber = totalMov[1]
                    totalMov = totalMov[0] - totalMov[1]

                    trans = str.maketrans('.,', ',.')
                    totalDebe_format = str(format(totalDebe, ',.2f').translate(trans))
                    totalHaber_format = str(format(totalHaber, ',.2f').translate(trans))
                    totalMov_format = str(format(round(totalMov,2), ',.2f').translate(trans))

                    debe_total_entry.config(state="normal")
                    haber_total_entry.config(state="normal")
                    total_entry.config(state="normal")

                    debe_total_entry.delete(0, END)
                    haber_total_entry.delete(0, END)
                    total_entry.delete(0, END)

                    debe_total_entry.insert(0, "$ " + totalDebe_format)
                    haber_total_entry.insert(0, "$ " + totalHaber_format)
                    total_entry.insert(0, "$ " + totalMov_format)

                    debe_total_entry.config(state="readonly")
                    haber_total_entry.config(state="readonly")
                    total_entry.config(state="readonly")

                    my_tree.yview_moveto('1.0')
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
            except:
                messagebox.showerror(title="Ups..Ups..", message="¡Error en la búsqueda! Intente nuevamente con distintos parámetros.", parent=cuenta_mov_frame)

        search_start_date_l = ttk.Label(cuenta_mov_frame, text="Desde", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_start_date_l.place(x=10, y=90)
        search_start_date = DateEntry(cuenta_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_start_date.config(state="readonly")
        search_start_date.place(x=10, y=115, height=35)

        search_end_date_l = ttk.Label(cuenta_mov_frame, text="Hasta", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_end_date_l.place(x=180, y=90)
        search_end_date = DateEntry(cuenta_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_end_date.config(state="readonly")
        search_end_date.place(x=180, y=115, height=35)

        search_btn = ttk.Button(cuenta_mov_frame, text="Buscar", style='button.TButton', command=search_cuenta)
        search_btn.place(x=350, y= 113)
        clean_search_btn = ttk.Button(cuenta_mov_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=520, y= 113)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        export_btn = ttk.Button(cuenta_mov_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)
        
        exit_btn = ttk.Button(cuenta_mov_frame, text="Salir", style='button.TButton', command=exitAllMov)
        exit_btn.place(x=1180, y=690)

        debe_total_entry = Entry(cuenta_mov_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=942, y=600)

        haber_total_entry = Entry(cuenta_mov_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=1145, y=600)

        total_entry = Entry(cuenta_mov_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1045, y=640)

        update_data()
    except:
        cuenta_mov_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def movimientosCuentaObs():
    try:
        cuentaObs_mov_frame = Toplevel()
        cuentaObs_mov_frame.grab_set()
        cuentaObs_mov_frame.resizable(0,0)
        cuentaObs_mov_frame.iconbitmap('img\codemy.ico')
        cuentaObs_mov_frame.title("Todos los Movimientos de Caja por Cuenta/Obs")

        ws = cuentaObs_mov_frame.winfo_screenwidth()
        hs = cuentaObs_mov_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            cuentaObs_mov_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            cuentaObs_mov_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#B25068")])

        # Create a Treeview Frame
        tree_frame = Frame(cuentaObs_mov_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CUENTA", "DEBE", "HABER", "DESCRIPCION")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=120)
        my_tree.column("CUENTA", anchor=W, width=510)
        my_tree.column("DEBE", anchor=W, width=150)
        my_tree.column("HABER", anchor=W, width=150)
        my_tree.column("DESCRIPCION", anchor=W, width=405)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CUENTA", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("DESCRIPCION", text="Descripción", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#e0b8c2")

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            c.execute("SELECT MAX(FECHA), MIN(FECHA) FROM Movimientos")
            dates_sql = c.fetchone()
            max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
            min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

            search_end_date.config(state="normal")
            search_start_date.config(state="normal")

            search_end_date.delete(0, END)
            search_start_date.delete(0, END)

            search_end_date.insert(0, max_date)
            search_start_date.insert(0, min_date)

            search_end_date.config(state="readonly")
            search_start_date.config(state="readonly")
            
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            clean_table()

            c.execute("SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER, IFNULL(DESCRIPCION, '') FROM Movimientos ORDER BY FECHA ASC")

            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0
            

            for record in records:       
                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])
                trans = str.maketrans('.,', ',.')
                debe = str(format(debe, ',.2f').translate(trans))            

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])
                haber = str(format(haber, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, record[5]), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, record[5]), tags=('oddrow',))

                # increment counter
                count += 1

                    

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(cuentaObs_mov_frame, foreground="#774360", style="mov_cajat.TLabel", text="Todos los Movimientos de Caja por Cuenta/Obs")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(cuentaObs_mov_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(cuentaObs_mov_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos de Caja por Cuenta/Obs?", parent=cuentaObs_mov_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 8)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,5)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(70, 10, 'Todos los Movimientos de Caja por Cuenta/Obs', 0, 2, 'L')
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(70, 5, company_name,0, 2, 'L')
                pdf.set_font("Arial", "B", 9)
                pdf.set_text_color(128,128,128)
                pdf.cell(70, 5, address,0, 2, 'L')
                pdf.set_text_color(128,0,0)
                pdf.set_font("Arial", "B", 8)
                pdf.cell(20, 5, 'Fecha', 1, 0, 'C')
                pdf.cell(60, 5, 'Cuenta', 1, 0, 'C')
                pdf.cell(25, 5, 'Debe', 1, 0, 'C')
                pdf.cell(25, 5, 'Haber', 1, 0, 'C')
                pdf.cell(60, 5, 'Obs.', 1, 0, 'C')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                first_date = 0
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 8)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(20)
                        pdf.set_auto_page_break(True, 30)
                    if record[1] != first_date:
                        pdf.multi_cell(100,8," ", 0, 1) 
                        pdf.set_font('arial', 'B', 10)
                        pdf.set_text_color(95, 0, 0)
                        pdf.multi_cell(100,5," ", 0, 1) 
                        pdf.cell(20, 10, record[1], 0, 0, 'C')
                        pdf.cell(0, 5, " ", 'B', 0, 'C')
                        first_date = record[1]              
                    pdf.set_font('arial', '', 8)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(100,5," ", 0, 1)
                    pdf.cell(20, 5, "", 'B', 0, 'C')
                    if len(record[2]) > 30:
                        pdf.set_font('arial', '', 6)
                    pdf.cell(60, 5, record[2], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 8)
                    pdf.cell(25, 5, record[3], 'B', 0, 'C')
                    pdf.set_text_color(255, 0, 0)
                    pdf.cell(25, 5, record[4], 'B', 0, 'C')
                    pdf.set_font('arial', '', 8)
                    pdf.set_text_color(0,0,0)
                    obs = record[5]
                    if len(obs) > 30:
                        pdf.set_font('arial', '', 6)
                    pdf.cell(60, 5, obs[:40], 'B', 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 10)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(99, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Cuentas"):
                    os.makedirs(path + "/Reportes Cuentas")
                pdf.output(path + '/Reportes Cuentas/Todos Los Movimientos por Obs - Cuenta.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Todos Los Movimientos por Obs - Cuenta.pdf] se exportó correctamente en el Escritorio.", parent= cuentaObs_mov_frame)


        def exitAllMov():
            cuentaObs_mov_frame.destroy()

        def clean_search():
            add_conceptos()
            update_data()


        def search_cuenta():
            try:
                start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')  
                end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d') 

                if start_date > end_date:
                    messagebox.showerror(title="Ups..Ups..", message="¡Error! La fecha DESDE no puede ser mayor a la fecha HASTA, intenta nuevamente.", parent=cuentaObs_mov_frame)
                else:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)

                    # Create a cursor instance
                    c = conn.cursor()

                    clean_table()
                    

                    c.execute("""SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(DEBE,'') AS DEBE, IFNULL(HABER,'') AS HABER, IFNULL(DESCRIPCION, '') FROM Movimientos WHERE FECHA BETWEEN :start_date AND :end_date ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})

                    records = c.fetchall()
                    
                    # Add our data to the screen
                    global count
                    count = 0
                    

                    for record in records:       
                        if record[3] == "":
                            debe = float(0)
                        else:
                            debe = float(record[3])
                        trans = str.maketrans('.,', ',.')
                        debe = str(format(debe, ',.2f').translate(trans))            

                        if record[4] == "":
                            haber = float(0)
                        else:
                            haber = float(record[4])
                        haber = str(format(haber, ',.2f').translate(trans))

                        if debe == "0,00":
                            debe = ""

                        if haber == "0,00":
                            haber = ""

                        date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')

                        if count % 2 == 0:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, record[5]), tags=('evenrow',))
                        else:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe, haber, record[5]), tags=('oddrow',))

                        # increment counter
                        count += 1

                    c.execute("""SELECT IFNULL(SUM(DEBE),0.0) AS DEBE, IFNULL(SUM(HABER),0.0) AS HABER FROM Movimientos WHERE FECHA BETWEEN :start_date AND :end_date ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})
                    totalMov = c.fetchone()
                    totalDebe = totalMov[0]
                    totalHaber = totalMov[1]
                    totalMov = totalMov[0] - totalMov[1]

                    trans = str.maketrans('.,', ',.')
                    totalDebe_format = str(format(totalDebe, ',.2f').translate(trans))
                    totalHaber_format = str(format(totalHaber, ',.2f').translate(trans))
                    totalMov_format = str(format(round(totalMov,2), ',.2f').translate(trans))

                    debe_total_entry.config(state="normal")
                    haber_total_entry.config(state="normal")
                    total_entry.config(state="normal")

                    debe_total_entry.delete(0, END)
                    haber_total_entry.delete(0, END)
                    total_entry.delete(0, END)

                    debe_total_entry.insert(0, "$ " + totalDebe_format)
                    haber_total_entry.insert(0, "$ " + totalHaber_format)
                    total_entry.insert(0, "$ " + totalMov_format)

                    debe_total_entry.config(state="readonly")
                    haber_total_entry.config(state="readonly")
                    total_entry.config(state="readonly")

                    my_tree.yview_moveto('1.0')
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
            except:
                messagebox.showerror(title="Ups..Ups..", message="¡Error en la búsqueda! Intente nuevamente con distintos parámetros.", parent=cuentaObs_mov_frame)

        search_start_date_l = ttk.Label(cuentaObs_mov_frame, text="Desde", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_start_date_l.place(x=10, y=90)
        search_start_date = DateEntry(cuentaObs_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_start_date.config(state="readonly")
        search_start_date.place(x=10, y=115, height=35)

        search_end_date_l = ttk.Label(cuentaObs_mov_frame, text="Hasta", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_end_date_l.place(x=180, y=90)
        search_end_date = DateEntry(cuentaObs_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_end_date.config(state="readonly")
        search_end_date.place(x=180, y=115, height=35)

        search_btn = ttk.Button(cuentaObs_mov_frame, text="Buscar", style='button.TButton', command=search_cuenta)
        search_btn.place(x=350, y= 113)
        clean_search_btn = ttk.Button(cuentaObs_mov_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=520, y= 113)


        title_name_label.config(text=company_name)
        address_label.config(text=address)

        export_btn = ttk.Button(cuentaObs_mov_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)
        
        exit_btn = ttk.Button(cuentaObs_mov_frame, text="Salir", style='button.TButton', command=exitAllMov)
        exit_btn.place(x=1180, y=690)

        debe_total_entry = Entry(cuentaObs_mov_frame, font=("Arial", 14, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=622, y=630)

        haber_total_entry = Entry(cuentaObs_mov_frame, font=("Arial", 14, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=800, y=630)

        total_entry = Entry(cuentaObs_mov_frame, font=("Arial", 14, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=715, y=670)

        update_data()
    except:
        cuentaObs_mov_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def movimientosCuentaDiferencia():
    try:
        cuentaDiferencia_mov_frame = Toplevel()
        cuentaDiferencia_mov_frame.grab_set()
        cuentaDiferencia_mov_frame.resizable(0,0)
        cuentaDiferencia_mov_frame.iconbitmap('img\codemy.ico')
        cuentaDiferencia_mov_frame.title("Movimientos por Cuenta agrupados por Fecha")

        ws = cuentaDiferencia_mov_frame.winfo_screenwidth()
        hs = cuentaDiferencia_mov_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            cuentaDiferencia_mov_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            cuentaDiferencia_mov_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#B25068")])

        # Create a Treeview Frame
        tree_frame = Frame(cuentaDiferencia_mov_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=160)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("ID_MOVIMIENTO", "FECHA", "CUENTA", "DEBE", "HABER", "DIFERENCIA")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("ID_MOVIMIENTO", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=130)
        my_tree.column("CUENTA", anchor=W, width=665)
        my_tree.column("DEBE", anchor=W, width=180)
        my_tree.column("HABER", anchor=W, width=180)
        my_tree.column("DIFERENCIA", anchor=W, width=180)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("ID_MOVIMIENTO", text="N°", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CUENTA", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("DIFERENCIA", text="Total", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#e0b8c2")

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)

            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            c.execute("SELECT MAX(FECHA), MIN(FECHA) FROM Movimientos")
            dates_sql = c.fetchone()
            max_date = datetime.strptime(dates_sql[0], '%Y/%m/%d').strftime('%d/%m/%Y')
            min_date = datetime.strptime(dates_sql[1], '%Y/%m/%d').strftime('%d/%m/%Y')

            search_end_date.config(state="normal")
            search_start_date.config(state="normal")

            search_end_date.delete(0, END)
            search_start_date.delete(0, END)

            search_end_date.insert(0, max_date)
            search_start_date.insert(0, min_date)

            search_end_date.config(state="readonly")
            search_start_date.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)


        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()
            clean_table()

            c.execute("SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(SUM(DEBE),'') AS DEBE, IFNULL(SUM(HABER),'') AS HABER FROM Movimientos GROUP BY FECHA, CUENTA ORDER BY FECHA ASC")

            records = c.fetchall()
            
            # Add our data to the screen
            global count
            count = 0
            

            for record in records:       
                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])
                
                trans = str.maketrans('.,', ',.')
                debe_format = str(format(debe, ',.2f').translate(trans))            

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])
                haber_format = str(format(haber, ',.2f').translate(trans))

                if debe_format == "0,00":
                    debe_format = ""

                if haber_format == "0,00":
                    haber_format = ""

                totalDif = round(debe - haber, 2)
                totalDif = str(format(totalDif, ',.2f').translate(trans))

                if totalDif == "0,00":
                    totalDif = ""

                date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')


                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe_format, haber_format, totalDif), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe_format, haber_format, totalDif), tags=('oddrow',))

                # increment counter
                count += 1

                    

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(cuentaDiferencia_mov_frame, foreground="#774360", style="mov_cajat.TLabel", text="Movimientos por Cuenta agrupados por Fecha")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(cuentaDiferencia_mov_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(cuentaDiferencia_mov_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar todos los Movimientos de Caja agrupados por Cuenta/Fecha?", parent=cuentaDiferencia_mov_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 8)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,5)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(70, 10, 'Movimientos por Cuenta agrupados por Fecha', 0, 2, 'L')
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(70, 5, company_name,0, 2, 'L')
                pdf.set_font("Arial", "B", 9)
                pdf.set_text_color(128,128,128)
                pdf.cell(70, 5, address,0, 2, 'L')
                pdf.set_text_color(128,0,0)
                pdf.set_font("Arial", "B", 8)
                pdf.cell(20, 5, 'Fecha', 1, 0, 'C')
                pdf.cell(80, 5, 'Cuenta', 1, 0, 'C')
                pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                pdf.cell(30, 5, 'Total', 1, 0, 'C')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                first_date = 0
                trans = str.maketrans('.,', ',.')
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 8)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(20)
                        pdf.set_auto_page_break(True, 30)
                    if record[1] != first_date:
                        pdf.multi_cell(100,8," ", 0, 1) 
                        pdf.set_font('arial', 'B', 10)
                        pdf.set_text_color(95, 0, 0)
                        pdf.multi_cell(100,5," ", 0, 1) 
                        pdf.cell(20, 10, record[1], 0, 0, 'C')
                        pdf.cell(0, 5, " ", 'B', 0, 'C')
                        first_date = record[1]              
                    pdf.set_font('arial', '', 8)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(100,5," ", 0, 1)
                    pdf.cell(20, 5, "", 'B', 0, 'C')
                    if len(record[2]) > 30:
                        pdf.set_font('arial', '', 6)
                    pdf.cell(80, 5, record[2], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 8)
                    pdf.cell(30, 5, record[3], 'B', 0, 'C')
                    pdf.set_text_color(255, 0, 0)
                    pdf.cell(30, 5, record[4], 'B', 0, 'C')
                    pdf.set_font('arial', '', 8)
                    pdf.set_text_color(0,0,0)
                    if float(str(format(record[5]).translate(trans)).replace(',', '')) < 0.00:
                        pdf.set_text_color(255, 0, 0)
                    pdf.set_font('arial', 'B', 8) 
                    pdf.cell(30, 5, record[5], 'B', 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 10)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(99, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Cuentas"):
                    os.makedirs(path + "/Reportes Cuentas")
                pdf.output(path + '/Reportes Cuentas/Agrupados por Fecha - Cuenta.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Agrupados por Fecha - Cuenta.pdf] se exportó correctamente en el Escritorio.", parent= cuentaDiferencia_mov_frame)



        def clean_search():
            add_conceptos()
            update_data()


        def search_cuenta():
            try:
                start_date = datetime.strptime(search_start_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d')  
                end_date = datetime.strptime(search_end_date.get(), '%d/%m/%Y').strftime('%Y/%m/%d') 

                if start_date > end_date:
                    messagebox.showerror(title="Ups..Ups..", message="¡Error! La fecha DESDE no puede ser mayor a la fecha HASTA, intenta nuevamente.", parent=cuentaDiferencia_mov_frame)
                else:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)

                    # Create a cursor instance
                    c = conn.cursor()

                    clean_table()
                    

                    c.execute("""SELECT ID_MOVIMIENTO, FECHA, CUENTA, IFNULL(SUM(DEBE),'') AS DEBE, IFNULL(SUM(HABER),'') AS HABER FROM Movimientos  WHERE FECHA BETWEEN :start_date AND :end_date GROUP BY FECHA, CUENTA ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})

                    records = c.fetchall()
                    
                    # Add our data to the screen
                    global count
                    count = 0
                    

                    for record in records:       
                        if record[3] == "":
                            debe = float(0)
                        else:
                            debe = float(record[3])
                        
                        trans = str.maketrans('.,', ',.')
                        debe_format = str(format(debe, ',.2f').translate(trans))            

                        if record[4] == "":
                            haber = float(0)
                        else:
                            haber = float(record[4])
                        haber_format = str(format(haber, ',.2f').translate(trans))

                        if debe_format == "0,00":
                            debe_format = ""

                        if haber_format == "0,00":
                            haber_format = ""

                        totalDif = round(debe - haber, 2)
                        totalDif = str(format(totalDif, ',.2f').translate(trans))

                        if totalDif == "0,00":
                            totalDif = ""

                        date = datetime.strptime(record[1], '%Y/%m/%d').strftime('%d/%m/%Y')


                        if count % 2 == 0:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe_format, haber_format, totalDif), tags=('evenrow',))
                        else:
                            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], date, record[2], debe_format, haber_format, totalDif), tags=('oddrow',))

                        # increment counter
                        count += 1

                    c.execute("""SELECT IFNULL(SUM(DEBE),0.0) AS DEBE, IFNULL(SUM(HABER),0.0) AS HABER FROM Movimientos WHERE FECHA BETWEEN :start_date AND :end_date ORDER BY FECHA ASC""",{'start_date':start_date, 'end_date': end_date})
                    totalMov = c.fetchone()
                    totalDebe = totalMov[0]
                    totalHaber = totalMov[1]
                    totalMov = totalMov[0] - totalMov[1]

                    trans = str.maketrans('.,', ',.')
                    totalDebe_format = str(format(totalDebe, ',.2f').translate(trans))
                    totalHaber_format = str(format(totalHaber, ',.2f').translate(trans))
                    totalMov_format = str(format(round(totalMov,2), ',.2f').translate(trans))

                    debe_total_entry.config(state="normal")
                    haber_total_entry.config(state="normal")
                    total_entry.config(state="normal")

                    debe_total_entry.delete(0, END)
                    haber_total_entry.delete(0, END)
                    total_entry.delete(0, END)

                    debe_total_entry.insert(0, "$ " + totalDebe_format)
                    haber_total_entry.insert(0, "$ " + totalHaber_format)
                    total_entry.insert(0, "$ " + totalMov_format)

                    debe_total_entry.config(state="readonly")
                    haber_total_entry.config(state="readonly")
                    total_entry.config(state="readonly")

                    my_tree.yview_moveto('1.0')
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close()
            except:
                messagebox.showerror(title="Ups..Ups..", message="¡Error en la búsqueda! Intente nuevamente con distintos parámetros.", parent=cuentaDiferencia_mov_frame)


        search_start_date_l = ttk.Label(cuentaDiferencia_mov_frame, text="Desde", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_start_date_l.place(x=10, y=90)
        search_start_date = DateEntry(cuentaDiferencia_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_start_date.config(state="readonly")
        search_start_date.place(x=10, y=115, height=35)

        search_end_date_l = ttk.Label(cuentaDiferencia_mov_frame, text="Hasta", style='style_tdata.TLabel', width=10, borderwidth=2, relief="solid", anchor="center")
        search_end_date_l.place(x=180, y=90)
        search_end_date = DateEntry(cuentaDiferencia_mov_frame, font=("Arial", 16), width=10, locale='es_AR', date_pattern='dd/mm/yyyy')
        search_end_date.config(state="readonly")
        search_end_date.place(x=180, y=115, height=35)

        search_btn = ttk.Button(cuentaDiferencia_mov_frame, text="Buscar", style='button.TButton', command=search_cuenta)
        search_btn.place(x=350, y= 113)
        clean_search_btn = ttk.Button(cuentaDiferencia_mov_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=520, y= 113)


        def exitAllMov():
            cuentaDiferencia_mov_frame.destroy()


        title_name_label.config(text=company_name)
        address_label.config(text=address)

        export_btn = ttk.Button(cuentaDiferencia_mov_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=113)
        
        exit_btn = ttk.Button(cuentaDiferencia_mov_frame, text="Salir", style='button.TButton', command=exitAllMov)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(cuentaDiferencia_mov_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=805, y=620)

        haber_total_entry = Entry(cuentaDiferencia_mov_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=975, y=620)

        total_entry = Entry(cuentaDiferencia_mov_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1165, y=620)

        update_data()
    except:
        cuentaDiferencia_mov_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def balanceSumasYSaldos():
    try:
        balance_frame = Toplevel()
        balance_frame.grab_set()
        balance_frame.resizable(0,0)
        balance_frame.iconbitmap('img\codemy.ico')
        balance_frame.title("Balance de Sumas y Saldos")

        ws = balance_frame.winfo_screenwidth()
        hs = balance_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            balance_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            balance_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#B25068")])

        # Create a Treeview Frame
        tree_frame = Frame(balance_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=150)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("CODIGO", "CUENTA", "DEBE", "HABER", "SALDO")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("CODIGO", anchor=W, width=130)
        my_tree.column("CUENTA", anchor=W, width=660)
        my_tree.column("DEBE", anchor=W, width=180)
        my_tree.column("HABER", anchor=W, width=180)
        my_tree.column("SALDO", anchor=W, width=180)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("CODIGO", text="Código", anchor=W)
        my_tree.heading("CUENTA", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("SALDO", text="Saldo", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#e0b8c2")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos GROUP BY ID_CUENTA ORDER BY CUENTA ASC")

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0

            for record in records:
                c.execute("""SELECT COD_CUENTA FROM Cuentas WHERE ID_CUENTA = :id_cuenta""", {'id_cuenta': record[0]})
                codCuenta = c.fetchone()
                codCuenta = codCuenta[0]

                if record[2] == "":
                    debe = float(0)
                else:
                    debe = float(record[2])

                if record[3] == "":
                    haber = float(0)
                else:
                    haber = float(record[3])

                saldoTotal = round(debe - haber, 2)

                trans = str.maketrans('.,', ',.')
                haber = str(format(haber, ',.2f').translate(trans))    
                debe = str(format(debe, ',.2f').translate(trans))
                saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                if saldoTotal == "0,00":
                    saldoTotal = ""

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(codCuenta, record[1], debe, haber, saldoTotal), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(codCuenta, record[1], debe, haber, saldoTotal), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(balance_frame, foreground="#774360", style="mov_cajat.TLabel", text="Balance de Sumas y Saldos")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(balance_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(balance_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT SUM(DEBE), SUM(HABER) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            
            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search(): 
            cuenta_bal_entry.delete(0, END)
            cuenta_bal_entry.focus()
            add_conceptos()
            update_data()

        def search_mov():
            if cuenta_bal_entry.get() == "Buscar Cuenta...":
                messagebox.showerror(title="Ups.. Ups..", message="El campo [Buscar Cuenta...] se encuentra vacío", parent=balance_frame)
            elif cuenta_bal_entry.get() == "":
                add_conceptos()
            else:
                nameCuenta = "%" + cuenta_bal_entry.get() + "%"
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("""SELECT ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE Cuenta LIKE :cuenta_name GROUP BY ID_CUENTA ORDER BY CUENTA ASC""", {'cuenta_name': nameCuenta})

                records = c.fetchall()

                clean_table()


                # Add our data to the screen
                global count
                count = 0


                for record in records:
                    c.execute("""SELECT COD_CUENTA FROM Cuentas WHERE ID_CUENTA = :id_cuenta""", {'id_cuenta': record[0]})
                    codCuenta = c.fetchone()
                    codCuenta = codCuenta[0]

                    if record[2] == "":
                        debe = float(0)
                    else:
                        debe = float(record[2])

                    if record[3] == "":
                        haber = float(0)
                    else:
                        haber = float(record[3])

                    saldoTotal = round(debe - haber, 2)

                    trans = str.maketrans('.,', ',.')
                    haber = str(format(haber, ',.2f').translate(trans))    
                    debe = str(format(debe, ',.2f').translate(trans))
                    saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                    if debe == "0,00":
                        debe = ""

                    if haber == "0,00":
                        haber = ""

                    if saldoTotal == "0,00":
                        saldoTotal = ""

                    if count % 2 == 0:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(codCuenta, record[1], debe, haber, saldoTotal), tags=('evenrow',))
                    else:
                        my_tree.insert(parent='', index='end', iid=count, text='', values=(codCuenta, record[1], debe, haber, saldoTotal), tags=('oddrow',))
                    # increment counter
                    count += 1


                c.execute("""SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CUENTA like :cuenta_name""", {'cuenta_name': nameCuenta})
                totals_concept = c.fetchone()

                trans = str.maketrans('.,', ',.')
                debe_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))
                haber_total = str(format(round(totals_concept[1],2), ',.2f').translate(trans))
                total = str(format(round(totals_concept[0] - totals_concept[1],2), ',.2f').translate(trans))

                debe_total_entry.config(state="normal")
                haber_total_entry.config(state="normal")
                total_entry.config(state="normal")
                

                debe_total_entry.delete(0, END)
                haber_total_entry.delete(0, END)
                total_entry.delete(0, END)
                

                debe_total_entry.insert(0, "$ " + debe_total)
                haber_total_entry.insert(0, "$ " + haber_total)
                total_entry.insert(0, "$ " + total)

                debe_total_entry.config(state="readonly")
                haber_total_entry.config(state="readonly")
                total_entry.config(state="readonly")

                my_tree.yview_moveto('1.0')
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()


        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Balance de Sumas y Saldos?", parent=balance_frame)
            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                if mov_lst == []:
                    messagebox.showerror(title="Ups..Ups..", message="¡No es posible exportar registro vacío! Intente con otro Concepto.", parent=balance_frame)
                    clean_search()
                else:
                    pdf = FPDF('P', 'mm', 'A4')
                    pdf.add_page()
                    pdf.set_font("Arial", "BI", 8)
                    pdf.set_text_color(0,0,0)
                    pdf.set_y(-25)
                    today_date = datetime.today().strftime('%d-%m-%Y')
                    pdf.cell(0, 0, today_date, 0, 0, 'L')
                    pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                    pdf.set_xy(0,5)
                    pdf.set_font("Times", "B", 20)
                    pdf.set_text_color(128,0,0)
                    pdf.cell(10)
                    pdf.cell(130, 10, 'Balance de Sumas y Saldos', 0, 0, 'L')
                    pdf.multi_cell(190,10," ", 0, 1)
                    pdf.set_text_color(0,0,0)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(148, 3, company_name,0, 0, 'L')
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 9)
                    pdf.set_text_color(128,128,128)
                    pdf.cell(70, 3, address,0, 0, 'L')
                    pdf.set_text_color(128,0,0)
                    pdf.multi_cell(190,4," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.cell(20, 5, 'Código', 1, 0, 'C')
                    pdf.cell(81, 5, 'Cuenta', 1, 0, 'C')
                    pdf.cell(30, 5, 'Debe', 1, 0, 'C')
                    pdf.cell(30, 5, 'Haber', 1, 0, 'C')
                    pdf.cell(30, 5, 'Saldo', 1, 0, 'C')
                    pdf.set_auto_page_break(True, 30)
                    trans = str.maketrans('.,', ',.')
                    page_num = pdf.page_no()
                    for record in mov_lst:
                        if page_num != pdf.page_no():
                            page_num = pdf.page_no()
                            pdf.set_auto_page_break(False, 0)
                            pdf.set_font("Arial", "BI", 8)
                            pdf.set_text_color(0,0,0)
                            pdf.set_y(-25)
                            today_date = datetime.today().strftime('%d-%m-%Y')
                            pdf.cell(0, 0, today_date, 0, 0, 'L')
                            pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                            pdf.set_y(20)
                            pdf.set_auto_page_break(True, 30)
                        pdf.set_font('arial', '', 10)
                        pdf.set_text_color(0,0,0)
                        pdf.multi_cell(190,5," ", 0, 1)
                        pdf.cell(20, 5, record[0], 'B', 0, 'C')
                        if len(record[1]) > 30:
                            pdf.set_font('arial', '', 8)
                        pdf.cell(81, 5, record[1], 'B', 0, 'C')
                        pdf.set_font('arial', '', 10)
                        pdf.cell(30, 5, record[2], 'B', 0, 'C')
                        pdf.cell(30, 5, record[3], 'B', 0, 'C')
                        if float(str(format(record[4]).translate(trans)).replace(',', '')) < 0.00:
                            pdf.set_font('arial', 'B', 10)
                            pdf.set_text_color(255, 0, 0)
                        else:
                            pdf.set_font('arial', 'B', 10)
                            pdf.set_text_color(0)
                        pdf.cell(30, 5, record[4], 'B', 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)  
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(71, 5, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, debe_total_entry.get(), 1, 0, 'C')
                    pdf.cell(30, 5, haber_total_entry.get(), 1, 0, 'C')
                    pdf.multi_cell(190,8," ", 0, 1)
                    pdf.set_font("Arial", "B", 10)
                    pdf.set_text_color(255,255,255)
                    pdf.set_fill_color(0,0,0)
                    pdf.cell(131, 3, ' ', 0, 0, 'C')
                    pdf.cell(30, 5, 'Saldo Final', 1, 0, 'C', fill=True)
                    pdf.set_text_color(0)
                    pdf.cell(30, 5, total_entry.get(), 1, 0, 'C')
                    path = os.path.expanduser("~/Desktop")
                    if not os.path.exists(path + "/Reportes Cuentas"):
                        os.makedirs(path + "/Reportes Cuentas")
                    pdf.output(path + '/Reportes Cuentas/Balance Sumas y Saldos - Cuenta.pdf', 'F')
                    messagebox.showinfo(title="Listado Exportado", message="El listado [Balance Sumas y Saldos - Cuenta.pdf] se exportó correctamente en el Escritorio.", parent= balance_frame)

        title_name_label.config(text=company_name)
        address_label.config(text=address)

        #Funciones de Texto temporal Entry Search
        def temp_text_search(e):
            cuenta_bal_entry.delete(0, END)
            cuenta_bal_entry.config(font=("Arial", 16), foreground="black")


        def temp_text_add_search(e):
            if cuenta_bal_entry.get() == "":
                cuenta_bal_entry.delete(0, END)
                cuenta_bal_entry.insert(0, "Buscar Cuenta...")
                cuenta_bal_entry.config(foreground="grey")

        cuenta_bal_entry = Entry(balance_frame, font=("Arial", 16, BOLD), width=30, foreground="grey")
        cuenta_bal_entry.insert(0, "Buscar Código...")
        cuenta_bal_entry.place(x=11, y=102, height=35)

        def searchBind(e):
            search_mov()

        def cleanSearchBind(e):
            clean_search()

        cuenta_bal_entry.bind("<FocusIn>", temp_text_search)
        cuenta_bal_entry.bind("<FocusOut>", temp_text_add_search)
        cuenta_bal_entry.bind("<Escape>", cleanSearchBind)
        cuenta_bal_entry.bind("<Return>", searchBind)
        
        search_btn = ttk.Button(balance_frame, text="Buscar", style='button.TButton', command=search_mov)
        search_btn.place(x=410, y= 100)
        clean_search_btn = ttk.Button(balance_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=570, y= 100)

        export_btn = ttk.Button(balance_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=100)

        def exitMovPerConcept():
            balance_frame.destroy()

        exit_btn = ttk.Button(balance_frame, text="Salir", style='button.TButton', command=exitMovPerConcept)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(balance_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=795, y=620)

        haber_total_entry = Entry(balance_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=985, y=620)

        total_entry = Entry(balance_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1165, y=620)

        update_data()
        clean_search()
    except:
        balance_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

def mayor():
    try:
        mayor_frame = Toplevel()
        mayor_frame.grab_set()
        mayor_frame.resizable(0,0)
        mayor_frame.iconbitmap('img\codemy.ico')
        mayor_frame.title("Mayor por Cuenta")

        ws = mayor_frame.winfo_screenwidth()
        hs = mayor_frame.winfo_screenheight()

        if ws == 1366 and hs == 768:
            mayor_frame.state('zoomed')
        else:
            w = 1366
            h = 768

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            mayor_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

        # Configure the Treeview Colors
        style.configure("Treeview",
        background="#D3D3D3",
        foreground="black",
        rowheight=25,
        fieldbackground="#D3D3D3", font=("Arial", 14))

        style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#774360")

        # Change Selected Color
        style.map('Treeview',
            background=[('selected', "#B25068")])

        # Create a Treeview Frame
        tree_frame = Frame(mayor_frame)
        #tree_frame.pack(pady=10)
        tree_frame.place(x=8, y=150)

        # Create a Treeview Scrollbar
        tree_scroll = Scrollbar(tree_frame, width=20)
        tree_scroll.pack(side=RIGHT, fill=Y)

        # Create The Treeview
        my_tree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set, selectmode="extended", height=17)
        my_tree.pack()

        # Configure the Scrollbar
        tree_scroll.config(command=my_tree.yview)

        # Define Our Columns
        my_tree['columns'] = ("FECHA", "CODIGO", "CUENTA", "DEBE", "HABER", "SALDO")

        # Format Our Columns
        my_tree.column("#0", width=0, stretch=NO)
        my_tree.column("FECHA", anchor=W, width=130)
        my_tree.column("CODIGO", anchor=W, width=110)
        my_tree.column("CUENTA", anchor=W, width=555)
        my_tree.column("DEBE", anchor=W, width=180)
        my_tree.column("HABER", anchor=W, width=180)
        my_tree.column("SALDO", anchor=W, width=180)

        # Create Headings
        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("FECHA", text="Fecha", anchor=W)
        my_tree.heading("CODIGO", text="Código", anchor=W)
        my_tree.heading("CUENTA", text="Cuenta", anchor=W)
        my_tree.heading("DEBE", text="Debe", anchor=W)
        my_tree.heading("HABER", text="Haber", anchor=W)
        my_tree.heading("SALDO", text="Saldo", anchor=W)

        # Create Striped Row Tags
        my_tree.tag_configure('oddrow', background="white")
        my_tree.tag_configure('evenrow', background="#e0b8c2")

        def clean_table():
            for item in my_tree.get_children():
                my_tree.delete(item)

        def add_conceptos():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT FECHA, ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos GROUP BY FECHA, CUENTA ORDER BY CUENTA ASC")

            records = c.fetchall()

            clean_table()


            # Add our data to the screen
            global count
            count = 0
            cuentaActual = 0

            for record in records:
                if record[1] != cuentaActual:
                    c.execute("""SELECT COD_CUENTA FROM Cuentas WHERE ID_CUENTA = :id_cuenta""", {'id_cuenta': record[1]})
                    codCuenta = c.fetchone()
                    cuentaActual = record[1]
                    codCuenta = codCuenta[0]

                if record[3] == "":
                    debe = float(0)
                else:
                    debe = float(record[3])

                if record[4] == "":
                    haber = float(0)
                else:
                    haber = float(record[4])

                saldoTotal = round(debe - haber, 2)

                trans = str.maketrans('.,', ',.')
                haber = str(format(haber, ',.2f').translate(trans))    
                debe = str(format(debe, ',.2f').translate(trans))
                saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                if debe == "0,00":
                    debe = ""

                if haber == "0,00":
                    haber = ""

                if saldoTotal == "0,00":
                    saldoTotal = ""

                if count % 2 == 0:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, codCuenta, record[2], debe, haber, saldoTotal), tags=('evenrow',))
                else:
                    my_tree.insert(parent='', index='end', iid=count, text='', values=(date, codCuenta, record[2], debe, haber, saldoTotal), tags=('oddrow',))
                # increment counter
                count += 1

            my_tree.yview_moveto('1.0')
            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

        add_conceptos()

        window_label = ttk.Label(mayor_frame, foreground="#774360", style="mov_cajat.TLabel", text="Mayor por Cuenta")
        window_label.place(x=10, y=5)
        title_name_label = ttk.Label(mayor_frame, foreground="#000000", style="mov_cajat.TLabel")
        title_name_label.place(x=10, y=35)
        address_label = ttk.Label(mayor_frame, foreground="#808080", style="mov_caja.TLabel")
        address_label.place(x=10, y=65)

        # Create a database or connect to one that exists
        conn = sqlite3.connect(db_name)

        # Create a cursor instance
        c = conn.cursor()

        c.execute("SELECT NOMBRE_EMPRESA, DOMICILIO FROM Datos_Empresa")
        records = c.fetchone()

        company_name = records[0]
        address = records[1]

        # Commit changes
        conn.commit()
        # Close our connection
        conn.close()

        def update_data():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos")
            records = c.fetchone()

            total_debe_haber = (records[0] - records[1])
            trans = str.maketrans('.,', ',.')
            total_debe_haber = format(total_debe_haber, ',.2f').translate(trans)

            debe_total = records[0]
            debe_total = format(debe_total, ',.2f').translate(trans)

            haber_total = records[1]
            haber_total = format(haber_total, ',.2f').translate(trans)
            
            debe_total_entry.config(state="normal")
            haber_total_entry.config(state="normal")
            total_entry.config(state="normal")
            

            debe_total_entry.delete(0, END)
            haber_total_entry.delete(0, END)
            total_entry.delete(0, END)
            
            debe_total_entry.insert(0, "$ " + debe_total)
            haber_total_entry.insert(0, "$ " + haber_total)
            total_entry.insert(0, "$ " + total_debe_haber)

            debe_total_entry.config(state="readonly")
            haber_total_entry.config(state="readonly")
            total_entry.config(state="readonly")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()


        def clean_search():
            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)
            # Create a cursor instance
            c = conn.cursor()

            c.execute("DELETE FROM Filters")

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            add_conceptos()
            update_data()

        def filters():
            filter_frame = Toplevel()
            filter_frame.grab_set()
            filter_frame.iconbitmap('img\codemy.ico')
            filter_frame.title("Filtrar Cuenta")
            w = 700
            h = 300

            ws = filter_frame.winfo_screenwidth()
            hs = filter_frame.winfo_screenheight()

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)

            filter_frame.geometry('%dx%d+%d+%d' % (w, h, x, y))

            # Configure the Treeview Colors
            style.configure("Treeview",
            background="#D3D3D3",
            foreground="black",
            rowheight=25,
            fieldbackground="#D3D3D3", font=("Arial", 14))

            style.configure("Treeview.Heading", font=("Comics Sans", 15, BOLD), foreground="#800000")

            # Change Selected Color
            style.map('Treeview',
                background=[('selected', "#d1d1e0")])

            # Create a Treeview Frame
            tree_frame_filter = Frame(filter_frame)
            tree_frame_filter.place(x=8, y=90)

            # Create a Treeview Scrollbar
            tree_scroll = Scrollbar(tree_frame_filter, width=20)
            tree_scroll.pack(side=RIGHT, fill=Y)

            # Create The Treeview
            my_tree_filter = ttk.Treeview(tree_frame_filter, yscrollcommand=tree_scroll.set, selectmode="extended", height=5)
            my_tree_filter.pack()

            # Configure the Scrollbar
            tree_scroll.config(command=my_tree_filter.yview)

            # Define Our Columns
            my_tree_filter['columns'] = ("ID", "FILTRO", "CUENTA")

            # Format Our Columns
            my_tree_filter.column("#0", width=0, stretch=NO)
            my_tree_filter.column("ID", width=0, stretch=NO)
            my_tree_filter.column("FILTRO", anchor=W, width=250)
            my_tree_filter.column("CUENTA", anchor=W, width=420)

            # Create Headings
            my_tree_filter.heading("#0", text="", anchor=W)
            my_tree_filter.heading("ID", text="", anchor=W)
            my_tree_filter.heading("FILTRO", text="Filtro", anchor=W)
            my_tree_filter.heading("CUENTA", text="Cuenta", anchor=W)
            
            # Create Striped Row Tags
            my_tree_filter.tag_configure('oddrow', background="white")
            my_tree_filter.tag_configure('evenrow', background="grey")

            titleLabel = ttk.Label(filter_frame, style='mov_cajat.TLabel', text="Filtros", foreground="#800000")
            titleLabel.place(x=8, y=5)

            filter_frame.var_filter_cbox = StringVar()
            filterOpt = []
            filterOpt.append("Igual a")
            filterOpt.append("Distinto de")
        
            filtro_cmbox = ttk.Combobox(filter_frame, font=("Arial", 14), textvariable=filter_frame.var_filter_cbox, state="readonly", width=15, height=15)
            filtro_cmbox['values'] = filterOpt
            filtro_cmbox.set("[Filtro...]")
            filtro_cmbox.place(x=8, y=40)

            # Create a database or connect to one that exists
            conn = sqlite3.connect(db_name)

            # Create a cursor instance
            c = conn.cursor()

            c.execute("SELECT NOMBRE_CUENTA, COD_CUENTA FROM Cuentas")
            cuentas_list = []
            for records in c.fetchall():
                cuentas_list.append(records[0] + " (" + records[1] + ")") 

            # Commit changes
            conn.commit()
            # Close our connection
            conn.close()

            filter_frame.var_cuenta_cbox = StringVar()

            cuenta_cmbox = ttk.Combobox(filter_frame, font=("Arial", 14), textvariable=filter_frame.var_cuenta_cbox, state="readonly", width=25, height=15)
            cuenta_cmbox['values'] = cuentas_list
            cuenta_cmbox.set("[Cuenta...]")
            cuenta_cmbox.place(x=220, y=40)

            def cleanFilter_table():
                for item in my_tree_filter.get_children():
                    my_tree_filter.delete(item)

            def add_actualFilter():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)

                # Create a cursor instance
                c = conn.cursor()

                c.execute("SELECT ID, Tipo, Cuenta FROM Filters")

                actualFilters = c.fetchall()

                if actualFilters != None:         
                    cleanFilter_table()


                    # Add our data to the screen
                    global count
                    count = 0

                    for record in actualFilters:
                        if count % 2 == 0:
                            my_tree_filter.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('evenrow',))
                        else:
                            my_tree_filter.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2]), tags=('oddrow',))
                        # increment counter
                        count += 1

                    idFilter_entry.delete(0, END)
                    my_tree_filter.yview_moveto('1.0')
                    # Commit changes
                    conn.commit()
                    # Close our connection
                    conn.close() 
                    

            add_actualFilter() 


            def selectedFilter(e):
                selected_filter = my_tree_filter.focus()
                if selected_filter != "":
                    # Grab record Number
                    selected = my_tree_filter.focus()
                    # Grab record values
                    values = my_tree_filter.item(selected, 'values')
                    idFilter_entry.delete(0, END)
                    idFilter_entry.insert(0, values[0])


            #Bind the treeview
            my_tree_filter.bind("<ButtonRelease-1>", selectedFilter)

            def addfilter():
                try:
                    idFilter_entry.delete(0, END)
                    if filter_frame.var_cuenta_cbox.get() == "[Cuenta...]" or filter_frame.var_filter_cbox.get() == "[Filtro...]":
                        messagebox.showerror(title="Ups.. Ups..", message="El campo [Filtro..] y [Cuenta...] se encuentran vacíos. Son obligatorios.", parent=filter_frame)
                    elif len(my_tree_filter.get_children()) > 5:
                        messagebox.showerror(title="Ups.. Ups..", message="Se alcanzó el límite de condiciones [5]. Elimine alguna si desea filtrar.", parent=filter_frame)
                    else:
                        filterCuenta = filter_frame.var_cuenta_cbox.get()
                        filterSelect = filter_frame.var_filter_cbox.get()

                        # Create a database or connect to one that exists
                        conn = sqlite3.connect(db_name)

                        # Create a cursor instance
                        c = conn.cursor()

                        sql_addFilter = "INSERT INTO Filters (Tipo, Cuenta) VALUES (?,?)"
                        sql_argsFilter = (filterSelect, filterCuenta)
                        c.execute(sql_addFilter, sql_argsFilter)

                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close() 

                        add_actualFilter()
                except:
                    messagebox.showerror(title="Ups.. Ups..", message="¡No es posible aplicar dos veces un filtro a la misma [Cuenta]! Intente con otro registro.", parent=filter_frame)
                        

            def delFilter():
                try:
                    if idFilter_entry.get() == "":
                        messagebox.showerror(title="Ups.. Ups..", message="¡Debe seleccionar el filtro a eliminar primero!", parent=filter_frame)
                    else:
                        # Create a database or connect to one that exists
                        conn = sqlite3.connect(db_name)

                        # Create a cursor instance
                        c = conn.cursor()

                        query_del = "DELETE FROM Filters WHERE ID = ?"
                        args_del = (idFilter_entry.get())
                        c.execute(query_del, [args_del])

                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close() 

                        add_actualFilter()
                except:
                    messagebox.showerror(title="Ups.. Ups..", message="Error al eliminar! Intente nuevamente.", parent=filter_frame)



                    
                    
            def acceptFilter():
                try:
                    # Create a database or connect to one that exists
                    conn = sqlite3.connect(db_name)
                    # Create a cursor instance
                    c = conn.cursor()

                    def convertTuple(tup):
                        str = ','.join(tup)
                        return str

                    c.execute("SELECT CUENTA FROM FILTERS WHERE Tipo = 'Distinto de'")

                    distrecords = c.fetchall()
                    
                    distList = ""

                    if distrecords == []:
                        distList = "-"
                    else:
                        for record in distrecords:
                            if distList != "":
                                distList = distList + "', "    
                            distList = distList + "'" + str(convertTuple(record)).rpartition(" (")[0]
                        distList = distList + "'"
                    

                    c.execute("SELECT CUENTA FROM FILTERS WHERE Tipo = 'Igual a'")

                    eqList = ""
                    eqrecords = c.fetchall()

                    if eqrecords == []:
                        eqList = "-"
                    else:
                        for record in eqrecords:
                            if eqList != "":
                                eqList = eqList + "', "    
                            eqList = eqList + "'" + str(convertTuple(record)).rpartition(" (")[0]
                        eqList = eqList + "'"

                    if distList == "-":
                        query = "SELECT FECHA, ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CUENTA IN " + "(" + eqList + ")" +  " GROUP BY FECHA, CUENTA ORDER BY CUENTA ASC"
                        c.execute(query)
                    elif eqList == "-":
                        query = "SELECT FECHA, ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CUENTA NOT IN " + "(" + distList + ")" + " GROUP BY FECHA, CUENTA ORDER BY CUENTA ASC"
                        c.execute(query)
                    else:
                        query = "SELECT FECHA, ID_CUENTA, CUENTA, IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE CUENTA IN " + "(" + eqList + ")" + " AND Cuenta NOT IN " + "(" + distList + ")" + " GROUP BY FECHA, CUENTA ORDER BY CUENTA ASC"
                        c.execute(query)

                    records = c.fetchall()
                    
                    if records != []:
                    
                        clean_table()

                        # Add our data to the screen
                        global count
                        count = 0


                        for record in records:
                            c.execute("""SELECT COD_CUENTA FROM Cuentas WHERE ID_CUENTA = :id_cuenta""", {'id_cuenta': record[1]})
                            codCuenta = c.fetchone()
                            codCuenta = codCuenta[0]

                            if record[3] == "":
                                debe = float(0)
                            else:
                                debe = float(record[3])

                            if record[4] == "":
                                haber = float(0)
                            else:
                                haber = float(record[4])

                            saldoTotal = round(debe - haber, 2)

                            trans = str.maketrans('.,', ',.')
                            haber = str(format(haber, ',.2f').translate(trans))    
                            debe = str(format(debe, ',.2f').translate(trans))
                            saldoTotal = str(format(saldoTotal, ',.2f').translate(trans))

                            if debe == "0,00":
                                debe = ""

                            if haber == "0,00":
                                haber = ""

                            if saldoTotal == "0,00":
                                saldoTotal = ""

                            date = datetime.strptime(record[0], '%Y/%m/%d').strftime('%d/%m/%Y')

                            if count % 2 == 0:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(date, codCuenta, record[2], debe, haber, saldoTotal), tags=('evenrow',))
                            else:
                                my_tree.insert(parent='', index='end', iid=count, text='', values=(date, codCuenta, record[2], debe, haber, saldoTotal), tags=('oddrow',))
                            # increment counter
                            count += 1

                        if distList == "-":
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CUENTA IN " + "(" + eqList + ")"
                            c.execute(query)
                        elif eqList == "-":
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CUENTA NOT IN " + "(" + distList + ")"
                            c.execute(query)
                        else:
                            query = "SELECT IFNULL(SUM(DEBE),0.00), IFNULL(SUM(HABER),0.00) FROM Movimientos WHERE CUENTA IN " + "(" + eqList + ")" + " AND Cuenta NOT IN " + "(" + distList + ")"
                            c.execute(query)

                        totals_concept = c.fetchone()

                        trans = str.maketrans('.,', ',.')
                        debe_total = str(format(round(totals_concept[0],2), ',.2f').translate(trans))
                        haber_total = str(format(round(totals_concept[1],2), ',.2f').translate(trans))
                        total = str(format(round(totals_concept[0] - totals_concept[1],2), ',.2f').translate(trans))

                        debe_total_entry.config(state="normal")
                        haber_total_entry.config(state="normal")
                        total_entry.config(state="normal")
                        

                        debe_total_entry.delete(0, END)
                        haber_total_entry.delete(0, END)
                        total_entry.delete(0, END)
                        

                        debe_total_entry.insert(0, "$ " + debe_total)
                        haber_total_entry.insert(0, "$ " + haber_total)
                        total_entry.insert(0, "$ " + total)

                        debe_total_entry.config(state="readonly")
                        haber_total_entry.config(state="readonly")
                        total_entry.config(state="readonly")
                        filter_frame.destroy()
                        

                        my_tree.yview_moveto('1.0')
                        # Commit changes
                        conn.commit()
                        # Close our connection
                        conn.close()
                    else:
                        messagebox.showerror(title="Ups.. Ups..", message="No se encontraron resultados! Intente con otra [Cuenta].", parent=filter_frame)

                except:
                    messagebox.showerror(title="Ups.. Ups..", message="Error en la búsqueda! Intente nuevamente.", parent=filter_frame)
                

            def cancelFilter():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("DELETE FROM Filters")

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                add_conceptos()
                filter_frame.destroy()          

            

            addfilter_btn = ttk.Button(filter_frame, text="Agregar", style='button.TButton', command=addfilter)
            addfilter_btn.place(x=540, y=38)

            acceptfilter_btn = ttk.Button(filter_frame, text="Aceptar", style='button.TButton', command=acceptFilter)
            acceptfilter_btn.place(x=220, y=250)

            delfilter_btn = ttk.Button(filter_frame, text="Eliminar", style='button.TButton', command=delFilter)
            delfilter_btn.place(x=380, y=250)

            cancelfilter_btn = ttk.Button(filter_frame, text="Cancelar", style='button.TButton', command=cancelFilter)
            cancelfilter_btn.place(x=540, y=250)


        def onClosingFilters():
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()

                c.execute("DELETE FROM Filters")

                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                mayor_frame.destroy()

        mayor_frame.protocol("WM_DELETE_WINDOW", onClosingFilters)

        def exportData():
            confirmation = messagebox.askquestion(title="Exportar Listado", message="¿Exportar Mayor por Cuenta?", parent=mayor_frame)

            if confirmation == 'yes':
                mov_lst = []
                count = 0
                for row_id in my_tree.get_children():
                    count += 1
                    row = my_tree.item(row_id, 'values')
                    mov_lst.append(row)
                mov_lst = list(map(list, mov_lst))
                pdf = FPDF('P', 'mm', 'A4')
                pdf.add_page()
                pdf.set_font("Arial", "BI", 10)
                pdf.set_text_color(0,0,0)
                pdf.set_y(-25)
                today_date = datetime.today().strftime('%d-%m-%Y')
                pdf.cell(0, 0, today_date, 0, 0, 'L')
                pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                pdf.set_xy(0,5)
                pdf.set_font("Times", "B", 20)
                pdf.set_text_color(128,0,0)
                pdf.cell(10)
                pdf.cell(70, 10, 'Mayor por Cuenta', 0, 2, 'L')
                pdf.set_text_color(0,0,0)
                pdf.set_font("Arial", "B", 10)
                pdf.cell(70, 5, company_name,0, 2, 'L')
                pdf.set_auto_page_break(True, 30)
                page_num = pdf.page_no()
                cuenta = 0
                contador = 0
                for record in mov_lst:
                    if page_num != pdf.page_no():
                        page_num = pdf.page_no()
                        pdf.set_auto_page_break(False, 0)
                        pdf.set_font("Arial", "BI", 10)
                        pdf.set_text_color(0,0,0)
                        pdf.set_y(-25)
                        today_date = datetime.today().strftime('%d-%m-%Y')
                        pdf.cell(0, 0, today_date, 0, 0, 'L')
                        pdf.cell(0, 0, "Página N°" + str(pdf.page_no()), 0, 0, 'R')
                        pdf.set_y(40)
                        pdf.set_auto_page_break(True, 30)
                    if record[2] != cuenta:
                        if contador != 0:
                            # Create a database or connect to one that exists
                            conn = sqlite3.connect(db_name)
                            # Create a cursor instance
                            c = conn.cursor()
                            
                            c.execute("""SELECT IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE Cuenta = :cuenta_name""", {'cuenta_name': cuenta})
                            records = c.fetchone()
                            totalCuenta = round(records[0] - records[1], 2)
                            trans = str.maketrans('.,', ',.')
                            total = str(format(totalCuenta, ',.2f').translate(trans)) 
                            # Commit changes
                            conn.commit()
                            # Close our connection
                            conn.close()
                            pdf.multi_cell(190,8," ", 0, 1)  
                            pdf.set_font("Arial", "B", 12)
                            pdf.set_text_color(255,255,255)
                            pdf.set_fill_color(0,0,0)
                            pdf.cell(30, 0, '', 0, 0, 'C')
                            pdf.cell(97, 5, ' ', 0, 0, 'C')
                            pdf.cell(30, 5, 'Total Cuenta', 1, 0, 'C', fill=True)
                            pdf.set_text_color(0)
                            pdf.cell(38, 5, "$" + total, 1, 0, 'C')
                        if pdf.get_y() > 180:
                            pdf.set_auto_page_break(True, 80)
                        pdf.multi_cell(100,8," ", 0, 1) 
                        pdf.set_font('arial', 'B', 14)
                        pdf.set_text_color(95, 0, 0)
                        pdf.multi_cell(100,5," ", 0, 1) 
                        pdf.cell(210, 15, record[2] + " (" + record[1] + ")", 0, 0, 'L')
                        pdf.multi_cell(100,5," ", 1, 1)
                        pdf.cell(65, 7, "", "", 0, 'C')
                        pdf.multi_cell(130,7," ", 'B', 0)
                        pdf.cell(35, 5, "", "", 0, 'C')
                        pdf.cell(40, 5, 'Fecha', 1, 0, 'C')
                        pdf.cell(40, 5, 'Debe', 1, 0, 'C')
                        pdf.cell(40, 5, 'Haber', 1, 0, 'C')
                        pdf.cell(40, 5, 'Saldo', 1, 0, 'C')
                        contador = 1
                        cuenta = record[2]
                    pdf.set_font('arial', '', 12)
                    pdf.set_text_color(0,0,0)
                    pdf.multi_cell(100,7," ", 0, 1)
                    pdf.cell(35, 5, "", 'B', 0, 'C')
                    pdf.cell(40, 5, record[0], 'B', 0, 'C')
                    pdf.cell(40, 5, record[3], 'B', 0, 'C')
                    pdf.set_font('arial', 'B', 12)
                    pdf.cell(40, 5, record[4], 'B', 0, 'C')
                    pdf.set_text_color(255, 0, 0)
                    pdf.cell(40, 5, record[5], 'B', 0, 'C')
                # Create a database or connect to one that exists
                conn = sqlite3.connect(db_name)
                # Create a cursor instance
                c = conn.cursor()
                c.execute("""SELECT IFNULL(SUM(DEBE),0.00) AS DEBE, IFNULL(SUM(HABER),0.00) AS HABER FROM Movimientos WHERE Cuenta = :cuenta_name""", {'cuenta_name': cuenta})
                records = c.fetchone()
                totalCuenta = round(records[0] - records[1], 2)
                trans = str.maketrans('.,', ',.')
                total = str(format(totalCuenta, ',.2f').translate(trans)) 
                # Commit changes
                conn.commit()
                # Close our connection
                conn.close()
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 12)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(0,0,0)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(97, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total Cuenta', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(38, 5, "$" + total, 1, 0, 'C')
                pdf.multi_cell(190,8," ", 0, 1)  
                pdf.set_font("Arial", "B", 12)
                pdf.set_text_color(255,255,255)
                pdf.set_fill_color(82, 82, 122)
                pdf.cell(30, 0, '', 0, 0, 'C')
                pdf.cell(97, 5, ' ', 0, 0, 'C')
                pdf.cell(30, 5, 'Total General', 1, 0, 'C', fill=True)
                pdf.set_text_color(0)
                pdf.cell(38, 5, total_entry.get(), 1, 0, 'C')
                path = os.path.expanduser("~/Desktop")
                if not os.path.exists(path + "/Reportes Cuentas"):
                    os.makedirs(path + "/Reportes Cuentas")
                pdf.output(path + '/Reportes Cuentas/Mayor por Cuenta - Cuenta.pdf', 'F')
                messagebox.showinfo(title="Listado Exportado", message="El listado [Mayor por Cuenta - Cuenta.pdf] se exportó correctamente en el Escritorio.", parent= mayor_frame)


        title_name_label.config(text=company_name)
        address_label.config(text=address)

        idFilter_entry = Entry(mayor_frame, font=("Arial", 14, BOLD), width=30, foreground="grey")
        
        search_btn = ttk.Button(mayor_frame, text="Filtros", style='button.TButton', command=filters)
        search_btn.place(x=8, y= 100)
        clean_search_btn = ttk.Button(mayor_frame, text="X", style='button.TButton', width=3, command=clean_search)
        clean_search_btn.place(x=168, y= 100)

        export_btn = ttk.Button(mayor_frame, text="Exportar", style='button.TButton', command=exportData)
        export_btn.place(x=1180, y=100)

        def exitMovPerConcept():
            mayor_frame.destroy()

        exit_btn = ttk.Button(mayor_frame, text="Salir", style='button.TButton', command=exitMovPerConcept)
        exit_btn.place(x=1180, y=670)

        debe_total_entry = Entry(mayor_frame, font=("Arial", 15, BOLD), width=14)
        debe_total_entry.config(state="readonly")
        debe_total_entry.place(x=795, y=630)

        haber_total_entry = Entry(mayor_frame, font=("Arial", 15, BOLD), width=14)
        haber_total_entry.config(state="readonly")
        haber_total_entry.place(x=975, y=630)

        total_entry = Entry(mayor_frame, font=("Arial", 15, BOLD), width=14)
        total_entry.config(state="readonly")
        total_entry.place(x=1165, y=630)

        update_data()
        clean_search()
    except:
        mayor_frame.destroy()
        messagebox.showerror(title="Ups..Ups..", message="¡Error al generar el reporte! No existen datos!")

#Create btn and entry for data_entry_frame
background_label_def = Label(data_entry_frame, background="#d1d1e0", height=23, width=140)
background_label_def.place(x=0, y=0)

photo_companyData = PhotoImage(file= r"img\companyData.png", width=30)
company_data_btn_def = ttk.Button(data_entry_frame, text=" Datos de la Empresa", image=photo_companyData, compound="left", style="mainPage.TButton", command=company_data)
company_data_btn_def.place(x=20, y=70)

photo_conceptos = PhotoImage(file= r"img\conceptosAdm.png", width=30)
concepts_btn_def = ttk.Button(data_entry_frame, text=" Carga de Conceptos", image=photo_conceptos, compound="left", style="mainPage.TButton", command=concepts)
concepts_btn_def.place(x=20, y=140)

photo_cuentas = PhotoImage(file= r"img\cuentasAdm.png", width=30)
cuentas_btn_def = ttk.Button(data_entry_frame, text=" Carga de Cuentas", image=photo_cuentas, compound="left", style="mainPage.TButton", command=cuentas_adm)
cuentas_btn_def.place(x=20, y=210)

photo_movimientos = PhotoImage(file= r"img\movimientosAdm.png", width=30)
caja_movement_btn_def = ttk.Button(data_entry_frame, text=" Carga de Movimientos de Caja", image=photo_movimientos, compound="left", style="mainPage.TButton", command=mov_caja_adm)
caja_movement_btn_def.place(x=480, y=140)

#Create btn and entry for concepto_report_frame
background_label_drf = Label(concepto_report_frame, background="#c2d6d6", height=23, width=140)
background_label_drf.place(x=0, y=0)

photo_todoslosmovimientos = PhotoImage(file= r"img\todoslosmovimientosReporte.png", width=30)
all_movement_btn_drf = ttk.Button(concepto_report_frame, text=" Movimientos de Caja por Conceptos", image=photo_todoslosmovimientos, compound="left", style="conceptosPage.TButton", command=all_movements)
all_movement_btn_drf.place(x=20, y=30)

photo_todoslosmovimientosporConcepto = PhotoImage(file= r"img\movimientosporconceptoReporte.png", width=30)
all_mov_concept_btn_drf = ttk.Button(concepto_report_frame, text=" Movimientos de un Concepto", image=photo_todoslosmovimientosporConcepto, compound="left", style="conceptosPage.TButton", command=allmovementsPerConcept)
all_mov_concept_btn_drf.place(x=20, y=85)

photo_totalesConcepto = PhotoImage(file= r"img\totalesReporte.png", width=30)
all_for_concept_btn_drf = ttk.Button(concepto_report_frame, text=" Totales por Concepto", image=photo_totalesConcepto, compound="left", style="conceptosPage.TButton", command=totalmovementsPerConcept)
all_for_concept_btn_drf.place(x=20, y=140)

photo_movimientosEntreFechas2 = PhotoImage(file= r"img\movimientosFechasReporte2.png", width=30)
between_dates_btn_drf = ttk.Button(concepto_report_frame, text=" Impresión de Caja entre Fechas", image=photo_movimientosEntreFechas2, compound="left", style="conceptosPage.TButton", command=movementsBetweenDates)
between_dates_btn_drf.place(x=20, y=205)

photo_movimientosEntreFechas = PhotoImage(file= r"img\movimientosFechasReporte.png", width=30)
concept_mov_dates_btn_drf = ttk.Button(concepto_report_frame, text=" Movimientos de un Concepto entre Fechas", image=photo_movimientosEntreFechas, compound="left", style="conceptosPage.TButton", command=movementsPerConceptBetweenDates)
concept_mov_dates_btn_drf.place(x=20, y=260)

photo_debe = PhotoImage(file= r"img\debeReporte.png", width=30)
debe_mov_btn_drf = ttk.Button(concepto_report_frame, text=" Movimientos del Debe", image=photo_debe, compound="left", style="conceptosPage.TButton", command=mov_debe)
debe_mov_btn_drf.place(x=610, y=70)

photo_haber = PhotoImage(file= r"img\haberReporte.png", width=30)
haber_mov_btn_drf = ttk.Button(concepto_report_frame, text=" Movimientos del Haber", image=photo_haber, compound="left", style="conceptosPage.TButton", command=mov_haber)
haber_mov_btn_drf.place(x=610, y=140)

photo_mayor = PhotoImage(file= r"img\mayorReporte.png", width=30)
mayorConceptos_btn_drf = ttk.Button(concepto_report_frame, text="Mayor por Conceptos", image=photo_mayor, compound="left", style="conceptosPage.TButton", command=mayorConceptos)
mayorConceptos_btn_drf.place(x=610, y=210)

#Create btn and entry for cuenta_report_frame
background_label_crf = Label(cuenta_report_frame, background="#F8E0E0", height=23, width=140)
background_label_crf.place(x=0, y=0)

photo_movCuenta = PhotoImage(file= r"img\movimientoscuentaReporte.png", width=30)
cuenta_mov_btn_crf = ttk.Button(cuenta_report_frame, text=" Movimientos de Caja por Cuentas", image=photo_movCuenta, compound="left", style="cuentasPage.TButton", command=movimientosCuenta)
cuenta_mov_btn_crf.place(x=20, y=70)

photo_movObsCuenta = PhotoImage(file= r"img\movimientosObsReporte.png", width=30)
all_mov_concept_btn_crf = ttk.Button(cuenta_report_frame, text=" Movimientos de Caja por Cuenta/Obs", image=photo_movObsCuenta, compound="left", style="cuentasPage.TButton", command=movimientosCuentaObs)
all_mov_concept_btn_crf.place(x=20, y=145)

photo_movCuentaFecha = PhotoImage(file= r"img\movimentosCuentaFechaReport.png", width=30)
all_for_concept_btn_crf = ttk.Button(cuenta_report_frame, text=" Movimientos de Caja agrupados por Fecha", image=photo_movCuentaFecha, compound="left", style="cuentasPage.TButton", command=movimientosCuentaDiferencia)
all_for_concept_btn_crf.place(x=20, y=220)

photo_SumasySaldo = PhotoImage(file= r"img\balanceSumasSaldoReporte.png", width=30)
balance_btn_crf = ttk.Button(cuenta_report_frame, text=" Balance de Sumas y Saldos", image=photo_SumasySaldo, compound="left", style="cuentasPage.TButton", command=balanceSumasYSaldos)
balance_btn_crf.place(x=560, y=103)

mayor_btn_crf = ttk.Button(cuenta_report_frame, text=" Mayor por Cuentas",  image=photo_mayor, compound="left", style="cuentasPage.TButton", command=mayor)
mayor_btn_crf.place(x=560, y=187)

#Exit Function
def exit():
    root.destroy()

#Create Exit Button
photo_exit = PhotoImage(file= r"img\logout.png", width=30)
exit_btn = ttk.Button(root, text="Salir", image=photo_exit, compound="left", command=exit, style='ttk.TButton')
exit_btn.place(x=660, y=470)

data_entry_frame.pack(fill='both', expand=True)
concepto_report_frame.pack(fill='both', expand=True)
cuenta_report_frame.pack(fill='both', expand=True)

notebook_main.add(data_entry_frame, text="Ingreso de Datos")
notebook_main.add(concepto_report_frame, text="Informes por Concepto")
notebook_main.add(cuenta_report_frame, text="Informes por Cuenta")

if not os.path.isfile('db/Contabilidad_db.db'):
    messagebox.showerror(title="Ups..Ups..", message="¡Error! No se encuentra el archivo de Base de Datos (Contabilidad_db) dentro de la carpeta db en el directorio del programa.")
    root.destroy()

root.mainloop()