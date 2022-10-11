# importamos tkinter 
from tkinter import *
 
#Validamos los datos ingresados al formulario
def ingresar():

    if name.get() == "Rodolfo" and nip.get()=="1235":
        mywindow.title("Bienvenido")
    
    elif name.get() == "" and nip.get()=="":
        mywindow.title("Error al iniciar sesion")
    
    elif name.get() == "" or nip.get()=="":
        mywindow.title("Error al iniciar sesion")

   
# Obtenemos el valor de las variables
def send_data():
  name_info = name.get()
  nip_info = nip.get()
  print(name_info,"\t", nip_info)
  ingresar()

  # Creamos la instacia de la clase Tk() y el cuerpo del formulario
mywindow = Tk()
mywindow.geometry("300x300")
mywindow.title("Formulario de ingreso")
mywindow.resizable(False,False)
mywindow.config(background = "#EEE7E5")
main_title = Label(text = "Acceda a su cuenta", font = ("Cambria", 14), width = "250", height = "2")
main_title.pack()

# Definimos la posicion de las etiquetas dentro del formulario
name_label = Label(text = "name")
name_label.place(x = 22, y = 70)
nip_label = Label(text = "nip")
nip_label.place(x = 22, y = 130)

# Obtenemos y almacenamos los datos del usuario
name = StringVar()
nip = StringVar()

# Definimos la posicion de los cuadros de texto
name_entry = Entry(textvariable = name, width = "40")
nip_entry = Entry(textvariable = nip, width = "40",  show = "*")

name_entry.place(x = 22, y = 100)
nip_entry.place(x = 22, y = 160)

# Definimos la funcion y caracteristicas del boton Login
submit_btn = Button(mywindow,text = "Login", width = "30", height = "1", command = send_data)
submit_btn.place(x = 22, y = 230)

mywindow.mainloop()