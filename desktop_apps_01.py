#-----------------------------
#--------desktop NO.1---------
#-----------------------------

# se importa toda la libreria tkinter con todas sus funciones

from tkinter import *

#------------------
# funcion de la app
#------------------

#-----------------------------
# pantalla principal de la app 
#-----------------------------

# se declara una variable llamada ventana_principal que adquiera las caracteristicas de un objeto Tk()

ventana_principal= Tk()

# titulo de la ventana 

ventana_principal.title("especialidad de sistemas")

# tamaño de la ventana

ventana_principal.geometry("500x500")

# deshabilitar boton de maximizar 

ventana_principal.resizable(False,False)

# color del fondo de la ventana

ventana_principal.config(bg=("dark orange"))

# run
# se ejecuta el metodo mainloop de la clase Tk atravez de la instancia ventana_principal, este metodo despliega la ventana en pantalla

ventana_principal.mainloop()

