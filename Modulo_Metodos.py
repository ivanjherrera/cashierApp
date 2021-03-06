from tkinter import*
from tkinter import font
from Consultas import*


def LimpiaText(Nombre,Nombre2,Apellido,Apellido2,Saldo):
	try:
		Nombre.delete("0","end")
		Nombre2.delete("0","end")
		Apellido.delete("0","end")
		Apellido2.delete("0","end")
		Saldo.delete("0","end")
		

		
	except Exception as e:

		messagebox.showwarning("Advertencia","Los campos ya estan limpios.")

#-------------METODO PARA LA VENTANA DE CREAR USUARIOS-------------------
def construye_Frame_Crear():
   

    Id=StringVar()
    Name=StringVar()
    Name2=StringVar()
    Apellido=StringVar()
    Apellido2=StringVar()
    Saldo=DoubleVar() 
   #----------------CREACION DE LA OTRA RAIZ-------------------

    #frame.witdraw()
    #raiz_Crear=Tk()
    
    raiz_Crear=Toplevel()
    raiz_Crear.title("Crear")
    raiz_Crear.geometry("285x255+522+230")

    

 #------------------------SEPARACION POR FILAS EN LA INTERFAZ-----------------------------
    
    label_Id=Label(raiz_Crear,text="ID:")
    label_Id.grid(row=1,column=0,padx=5,pady=5)
    
    btn_Salir=Button(raiz_Crear,text="SALIR",command=lambda:raiz_Crear.destroy())
    btn_Salir.grid(row=2,column=1,padx=5,pady=5)
    txt_Id=Entry(raiz_Crear,textvariable=Id)
    txt_Id.grid(row=2,column=0,padx=5,pady=5)
    

    label_Nombre=Label(raiz_Crear,text="NOMBRES:")
    label_Nombre.grid(row=3,column=0,padx=5,pady=5)
    btn_Limpia=Button(raiz_Crear,text="LIMPIA TEXT",command=lambda:LimpiaText(txt_Nombre,txt_Nombre2,txt_Apellido,txt_Apellido2,txt_Saldo))
    btn_Limpia.grid(row=3,column=1,padx=5,pady=5)
    txt_Nombre=Entry(raiz_Crear,textvariable=Name)
    txt_Nombre.grid(row=4,column=0,padx=5,pady=5)
    txt_Nombre2=Entry(raiz_Crear,textvariable=Name2)
    txt_Nombre2.grid(row=4,column=1,padx=5,pady=5)

    label_Apellido=Label(raiz_Crear,text="APELLIDOS:")
    label_Apellido.grid(row=5,column=0,padx=5,pady=5)
    txt_Apellido=Entry(raiz_Crear,textvariable=Apellido)
    txt_Apellido.grid(row=6,column=0,padx=5,pady=5)
    txt_Apellido2=Entry(raiz_Crear,textvariable=Apellido2)
    txt_Apellido2.grid(row=6,column=1,padx=5,pady=5)

    label_Saldo=Label(raiz_Crear,text="SALDO:")
    label_Saldo.grid(row=7,column=0,padx=5,pady=5)
    txt_Saldo=Entry(raiz_Crear,textvariable=Saldo)
    txt_Saldo.grid(row=8,column=0,padx=5,pady=5)
    btn_Agregar=Button(raiz_Crear,text="AGREGAR",command=lambda:InsertaRegistros(Name,Name2,Apellido,Apellido2,Saldo))
    btn_Agregar.grid(row=8,column=1,padx=5,pady=5)

    #raiz_Crear.mainloop()

def construye_Frame_Depositar_Retirar():

    Id=StringVar()
    NewSaldo=StringVar()#100.0#DoubleVar()
    NewSaldo.set("")
    Name1_Label=StringVar()
    Name1_Label.set("...")
    Name2_Label=StringVar()
    Name2_Label.set("...")
    Apelli_Label=StringVar()
    Apelli_Label.set("...")
    Apelli2_Label=StringVar()
    Apelli2_Label.set("...")
    Saldo=StringVar()
    Saldo.set("...")

   #----------------CREACION DE LA OTRA RAIZ-------------------

    #frame.witdraw()
    #raiz_Crear=Tk()
    
    raiz_Crear=Toplevel()
    raiz_Crear.title("Depositar-Retirar")
    raiz_Crear.geometry("295x200+522+230")

    #----------CREACION DE LOS ELEMENTOS DEL FRAME----------

    label_Id=Label(raiz_Crear,text="ID:")
    label_Id.grid(row=1,column=0,padx=5,pady=5)
    txt_Id=Entry(raiz_Crear,textvariable=Id)
    txt_Id.grid(row=1,column=1,padx=5,pady=5)
    btn_Search=Button(raiz_Crear,text="SEARCH",command=lambda:ejecuta_Consultas(txt_Id,Name1_Label,Name2_Label,Apelli_Label,Apelli2_Label,Saldo))
    btn_Search.grid(row=1,column=2,padx=5,pady=5)

    label_Name=Label(raiz_Crear,textvariable=Name1_Label)
    label_Name.grid(row=2,column=0,padx=5,pady=5)
    label_Name2=Label(raiz_Crear,textvariable=Name2_Label)
    label_Name2.grid(row=2,column=1,padx=5,pady=5)

    label_Apelli=Label(raiz_Crear,textvariable=Apelli_Label)
    label_Apelli.grid(row=3,column=0,padx=5,pady=5)
    label_Apelli2=Label(raiz_Crear,textvariable=Apelli2_Label)
    label_Apelli2.grid(row=3,column=1,padx=5,pady=5)

    label_Saldo=Label(raiz_Crear,textvariable=Saldo)
    label_Saldo.grid(row=4,column=0,padx=5,pady=5)

    label_Saldo2=Label(raiz_Crear,text="Ingrese el saldo:")
    label_Saldo2.grid(row=5,column=0,padx=5,pady=5)
    txt_NewSaldo=Entry(raiz_Crear,textvariable=NewSaldo)
    txt_NewSaldo.grid(row=5,column=1,padx=5,pady=5)

    btn_Retirar=Button(raiz_Crear,text="RETIRAR",command=lambda:retira_Dinero(txt_Id,Saldo,NewSaldo,Name1_Label,Name2_Label,Apelli_Label,Apelli2_Label,Saldo))
    btn_Retirar.grid(row=6,column=0,padx=5,pady=5)
    btn_Depositar=Button(raiz_Crear,text="DEPOSITAR",command=lambda:deposita_Dinero(txt_Id,Saldo,NewSaldo,Name1_Label,Name2_Label,Apelli_Label,Apelli2_Label,Saldo))
    btn_Depositar.grid(row=6,column=1,padx=5,pady=5)
    btn_Salir=Button(raiz_Crear,text="SALIR",command=lambda:raiz_Crear.destroy())
    btn_Salir.grid(row=6,column=2,padx=5,pady=5)

def construye_Frame_Pagos():

    Id=StringVar()
    Name1_Label=StringVar()
    Name1_Label.set("...")
    Saldo=StringVar()
    Saldo.set("0")

     #----------------CREACION DE LA OTRA RAIZ-------------------

    #frame.witdraw()
    #raiz_Crear=Tk()
    
    raiz_Crear=Toplevel()
    raiz_Crear.title("Pagos")
    raiz_Crear.geometry("295x200+522+230")

    label_Id=Label(raiz_Crear,text="ID:")
    label_Id.grid(row=1,column=0,padx=5,pady=5)
    txt_Id=Entry(raiz_Crear,textvariable=Id)
    txt_Id.grid(row=1,column=1,padx=5,pady=5)
    btn_Search=Button(raiz_Crear,text="BUSCAR",command=lambda:ejecuta_Consulta(txt_Id,Name1_Label,Saldo))
    btn_Search.grid(row=1,column=2,padx=5,pady=5)

    label_Name=Label(raiz_Crear,textvariable=Name1_Label)
    label_Name.grid(row=2,column=0,padx=5,pady=5)
    btn_Serv1=Button(raiz_Crear,text="Serv1",command=lambda:primer_Servicio(txt_Id,Saldo,Name1_Label,Saldo))
    btn_Serv1.grid(row=2,column=2,padx=5,pady=5)


    label_Saldo=Label(raiz_Crear,textvariable=Saldo)
    label_Saldo.grid(row=3,column=0,padx=5,pady=5)
    btn_Serv2=Button(raiz_Crear,text="Serv2",command=lambda:segundo_Servicio(txt_Id,Saldo,Name1_Label,Saldo))
    btn_Serv2.grid(row=3,column=2,padx=5,pady=5)

    btn_Serv3=Button(raiz_Crear,text="Serv3",command=lambda:tercer_Servicio(txt_Id,Saldo,Name1_Label,Saldo))
    btn_Serv3.grid(row=4,column=2,padx=5,pady=5)

    btn_Salir=Button(raiz_Crear,text="SALIR", command=lambda:raiz_Crear.destroy())
    btn_Salir.grid(row=5,column=2,padx=5,pady=5)

