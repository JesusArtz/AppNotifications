import threading
import requests
import random
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



# Carga la ventana de Tkinter

root = Tk()
estilo = Style(theme='pers')
ventana = estilo.master
root.title("App")
root.geometry("600x450")
imagen = PhotoImage(file= "Assets/CTRL.png")
Label(root, image= imagen).pack(pady=5)

varTime = IntVar()

# Define la listas donde se almacenaran los datos de la API
listaTitulos = []
listaMensajes = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("https://jesusartz.net/api/datos", headers=headers)
object = response.json()
for i in object['postData']:
    listaTitulos.append(i['titulo'])
    listaMensajes.append(i['mensaje'])


# Detecta el tamaño de las listas
longitud = len(listaMensajes)



# Hace Funcionar el boton de BuyMeaCoffe (PARTE ESENCIAL NO TOCAR)
url = "https://www.buymeacoffee.com/jesusartz"
def BuyMeaCoffee():
    webbrowser.open_new(url)

# Define los parametros de notificacion para Linux
def LinuxMessage(title, description):
    notify2.init('Test')
    notify = notify2.Notification(title, description)
    notify
    return

# Define los parametros de notificacion para Windows
def WindowsMessage(tittle, description):
    notificacion.show_toast(tittle, description, duration=5)
    return

# Correr programa principal
def mainProgram():
    # Detecta la platarfoma en la que esta corriendo el programa
    if platform == "linux" or platform == "linux2":
        # Genera un numero aleartorio para enviar una notificacion al azar de la api 
        randomNum = random.randint(5, longitud)
        # Envia la notificacion de la Lista [RANDOM]
        LinuxMessage(listaTitulos[randomNum], listaMensajes[randomNum])
        # Tiempo de espera para la siguiente notificacion
        time.sleep(15)

    elif platform == "win32":
        # Genera un numero aleartorio para enviar una notificacion al azar de la api 
        randomNum = random.randint(5, longitud)
        # Envia la notificacion de la Lista [RANDOM]
        WindowsMessage(listaTitulos[randomNum], listaMensajes[randomNum])
        # Tiempo de espera para la siguiente notificacion
        time.sleep(15)
    
#def apiGet():
#    while True:
#        response = requests.get("http://localhost:3001/api/motivacion")
#        object = response.json()
#        for i in object:
#            listaTitulos.append(i['titulo'])
#            listaMensajes.append(i['mensaje'])


# Esta funcion crea un hilo en el sistema para poder usar la interfaz a la vez que el bucle se ejecuta
def bucle():
    stop_threads = False
    while True:
        mainProgram()
        stop_threads
        if stop_threads:
            break

def StopThread():
    stop_threads = True





#Botones y Checkbuttons

botonInicio = Button(text="Start", command=lambda:threading.Thread(target=bucle).start())
tiempoVar = Label(root, textvariable=varTime)
tiempoVar.place(x=300, y=225)
tiempoVar.pack()
botonStop = Button(text="Stop", command=StopThread)
botonCoffee = Button(text="Buy Me a Coffee", command=BuyMeaCoffee)
botonCoffee.place(x= 450, y= 400)
botonStop.place(x=300, y=400)
botonInicio.place(x=150, y=400)

#Main Loop

root.mainloop()


# Coded with love for Emma
