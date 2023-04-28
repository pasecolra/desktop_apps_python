from tkinter import *

ventana_principal=Tk()

ventana_principal.title("bandera")

ventana_principal.resizable(False, False)

ventana_principal.geometry("500x300")

frame_ventana=Frame(ventana_principal)

frame_ventana.config(bg="dark orange", width=200,height=300)

frame_ventana.place(x=0,y=0)

ventana_principal.mainloop()



