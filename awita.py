import threading
import pymysql
import time
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
from sys import platform
#Importa win10toast si el sistema operativo es Windows
if platform == "win32":
    from win10toast import ToastNotifier
    notificacion = ToastNotifier()
#Importa notify2 si el sistema operativo es Linux
elif platform == "linux" or platform == "linux2":
    import notify2

def dataBase(titulo, contenido):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='dbapp'
    )
    cursor = connection.cursor()

    sql = "SELECT * FROM motivacion"

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
estilo = Style(theme='darkly')
ventana = estilo.master
root.title("App")
root.geometry("600x450")
motivacion = IntVar()
salud = IntVar()
datosCuriosos = IntVar()
botonInicio = Button(text="Start", command=threading.Thread(target=bucle).start())
botonStop = Button(text="Stop")
botonStop.place(x=340, y=400)
botonInicio.place(x=200, y=400)
check1 = Checkbutton(text="Curiosidades", variable=datosCuriosos, onvalue=1, offvalue=0)
check1.place(x=150, y=50)
root.mainloop()