from tkinter import*
from tkinter import messagebox
import sqlite3
from Modulo_Metodos import* 

#------------ZONA DE LA RAIZ---------
raiz=Tk()
raiz.title("Sistema de Gestion")
raiz.geometry("310x308+510+230")
#raiz.config(bg="red")
#------------------------------------
#CREACION DEL FRAME LABELS-------------------

miFrame=Frame()
miFrame.config(width=300,height=105)
miFrame.grid()
#---------------------------------


#-----------SECCION DONDE CREO LOS DISTINTOS FORMATOS-----------

Helvfont=font.Font(family="Helvetica", size=12, weight="bold")
#----------------------------------------------------------

#-----------------------SECCION DE METODOS---------------
def cierra_Ventana():
    raiz.destroy()
#--------CREACION DE LA PRIMERA VENTANA----------
Helvfont_Btn =font.Font(family="Helvetica", size=8, weight="normal")
label_Bienvenida=Label(miFrame,text="BIENVENIDOS AL SISTEMA", font=Helvfont)
label_Bienvenida.grid(row=1,column=0,padx=10,pady=10)

label_Realizar=Label(miFrame,text="QUE ACTIVIDAD DESEA REALIZAR?", font=Helvfont)
label_Realizar.grid(row=2,column=0,padx=10,pady=10)

btn_Crear=Button(miFrame,text="CREAR", font=Helvfont_Btn,command=construye_Frame_Crear)
btn_Crear.grid(row=3,column=0,padx=10,pady=10)
btn_Depositar=Button(miFrame,text="DEPOSITAR-RETIRAR", font=Helvfont_Btn,command=construye_Frame_Depositar_Retirar)
btn_Depositar.grid(row=4,column=0,padx=10,pady=10)
#btn_Retirar=Button(miFrame,text="RETIRAR", font=Helvfont_Btn)
#btn_Retirar.grid(row=5,column=0,padx=10,pady=10)
btn_Pagos=Button(miFrame,text="PAGOS", font=Helvfont_Btn)
btn_Pagos.grid(row=5,column=0,padx=10,pady=10)
btn_Salir=Button(miFrame,text="SALIR", font=Helvfont_Btn,command=cierra_Ventana)
btn_Salir.grid(row=6,column=0,padx=10,pady=10)



#NOTA: CREAR LA VENTANA DE PAGOS
#NOTA2: AVERIGUAR SI SE EXISTEN LOS LINK LABELS
#NOTA3: GUARDAR EL PROYECTO EN GIT ANTES DE EMPEZAR CON LO DEMAS







raiz.mainloop()