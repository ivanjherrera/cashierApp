import sqlite3
from tkinter import messagebox
from tkinter import*


def CreaTabla():
	
	try:

		miConexion=sqlite3.connect("TablaClientes")
		miCursor=miConexion.cursor()

		miCursor.execute('''
			CREATE TABLE CLIENTES(
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			PRIMER_NOMBRE VARCHAR(30),
			SEGUNDO_NOMBRE VARCHAR(30),
			APELLIDO VARCHAR(30),
			SEGUNDO_APELLIDO VARCHAR(20),
			SALDO DOUBLE(20))
			''')

		miConexion.close()

		messagebox.showinfo("Gestor","Tabla creada con exito")
	 	
	except Exception as e:
	 	messagebox.showwarning("Advertencia","La tabla ya existe! Proceda a ingresar registros")
	 #---------------------------------------------------

def InsertaRegistros(Name,Name2,Apellido,Apellido2,Saldo):
	
     
     Nombre1=Name
     Nombre2=Name2
     Apelli=Apellido
     Apelli2=Apellido2
     Sald=Saldo 

     miConexion=sqlite3.connect("TablaClientes")
	 #miCursor=miConexion.cursor()
     miCursor=miConexion.cursor()

     miCursor.execute("INSERT INTO CLIENTES VALUES(NULL, '" + 
		Nombre1.get() + 
		"','" + Nombre2.get() +
		"','" + Apelli.get() +
        "','" + Apelli2.get() +  
		"','" + Sald.get() + "')")
		#"','" + textoComentario.get("1.0","end")+ "')")
     
     miConexion.commit()
     miConexion.close()

     messagebox.showinfo("Gestor", "Registro agregado con exito")
	

def ejecuta_Consultas(Id,Name,Name2,Apellido,Apellido2,Saldo):
	
	if Id.get()!="":
		miConexion=sqlite3.connect("TablaClientes")
		miCursor=miConexion.cursor()

		miCursor.execute("SELECT * FROM CLIENTES WHERE ID="+ Id.get())
		elUsuario=miCursor.fetchall()

		for usuario in elUsuario:

			#Id.set(usuario[0])
			Name.set(usuario[1])
			Name2.set(usuario[2])
			Apellido.set(usuario[3])
			Apellido2.set(usuario[4])
			Saldo.set(usuario[5])
			
		#print(usuario[2])
			

		miConexion.commit()
		miConexion.close()	 
	else:
		messagebox.showerror("ERROR","El Id que ingreso no existe, Verifique y vuelva a intentarlo.")