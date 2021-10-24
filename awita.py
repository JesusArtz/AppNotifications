import threading
import pymysql
import time
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import webbrowser
from sys import platform
#Importa win10toast si el sistema operativo es Windows
if platform == "win32":
    from win10toast import ToastNotifier
    notificacion = ToastNotifier()
#Importa notify2 si el sistema operativo es Linux
elif platform == "linux" or platform == "linux2":
    import notify2

url = "https://www.buymeacoffee.com/jesusartz"

def BuyMeaCoffee():
    webbrowser.open_new(url)

# Coneccion a base de datos
def dataBase():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='dbapp'
    )
    cursor = connection.cursor()

    cons1 = "SELECT titulo FROM motivacion"
    cons2 = "SELECT contenido FROM motivacion"

    cursor.execute(cons1)
    titulo = cursor.fetchall()

    cursor.execute(cons2)
    contenido = cursor.fetchall()
    

def LinuxMessage(title, description):
    notify2.init('Test')
    notify = notify2.Notification(title, description)
    notify
    return

def WindowsMessage(tittle, description):
    notificacion.show_toast(tittle, description, duration=5)
    return

def mainProgram():
    if platform == "linux" or platform == "linux2":
        LinuxMessage("Recuerda beber agua", "Cuida tu cuerpo y mantente centrado <3")
        time.sleep(1000)
            


    elif platform == "win32":
        WindowsMessage("Recuerda beber agua", "Cuida tu cuerpo y mantente centrado <3")
        time.sleep(100)
        
def bucle():
    while True:
        mainProgram()

root = Tk()
estilo = Style(theme='pers')
ventana = estilo.master
root.title("App")
root.geometry("600x450")
imagen = PhotoImage(file= "Assets/CTRL.png")
Label(root, image= imagen).pack(pady=5)

#Variables de Checkbutton

motivacion = IntVar()
salud = IntVar()
datosCuriosos = IntVar()

#Botones y Checkbuttons

botonInicio = Button(text="Start", command=lambda:threading.Thread(target=bucle).start())
botonStop = Button(text="Stop")
botonCoffee = Button(text="Buy Me a Coffee", command=BuyMeaCoffee)
botonCoffee.place(x= 450, y= 400)
botonStop.place(x=300, y=400)
botonInicio.place(x=150, y=400)
check1 = Checkbutton(text="Curiosidades", variable=datosCuriosos, onvalue=1, offvalue=0)
check1.place(x=75, y=250)
check2 = Checkbutton(text="Salud", variable=salud, onvalue=1, offvalue=0)
check2.place(x=75, y=300)
check3 = Checkbutton(text="Motivacion", variable=motivacion, onvalue=1, offvalue=0)
check3.place(x=75, y=350)

#Main Loop

root.mainloop()
