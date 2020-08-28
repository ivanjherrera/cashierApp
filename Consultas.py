import sqlite3
from tkinter import messagebox


def CreaTabla():
	
	try:

		miConexion=sqlite3.connect("TablaClientes")
		miCursor=miConexion.cursor()

		miCursor.execute('''
			CREATE TABLE CLIENTES(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE_USUARIO VARCHAR(50),
			PASSWORD VARCHAR(50),
			APELLIDO VARCHAR(50),
			DIRECCION VARCHAR(50),
			COMENTARIOS VARCHAR(50))
			''')

		miConexion.close()

		messagebox.showinfo("Gestor","Tabla creada con exito")
	 	
	except Exception as e:
	 	messagebox.showwarning("Advertencia","La tabla ya existe! Proceda a ingresar registros")
	 #---------------------------------------------------