import threading
import requests
import random
import time
from tkinter import *
from tkinter import ttk
from ttkbootstrap import Style
import webbrowser
from sys import platform

# Importa win10toast si el sistema operativo es Windows
if platform == "win32":
    from win10toast import ToastNotifier

    notificacion = ToastNotifier()
# Importa notify2 si el sistema operativo es Linux
elif platform == "linux" or platform == "linux2":
    import notify2

stop_threads = False

# Carga la ventana de Tkinter

root = Tk()
estilo = Style(theme='alt')
ventana = estilo.master
root.title("App")
root.geometry("600x450")
imagen = PhotoImage(file="Assets/CTRL.png")
Label(root, image=imagen).pack(pady=5)

varDatos = IntVar()
varMotivacion = IntVar()

# Define la listas donde se almacenaran los datos de la API
listaTitulos = []
listaMensajes = []

listaTD = []
listaMD = []

listaTM = []
listaMM = []

headers = headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get("http://137.184.124.114:8080/api/datos", headers=headers)

api = response.json()

for i in api:
    listaTD.append(i['TituloD'])
    listaMD.append(i['MensajeD'])

for i in api:
    listaTM.append(i['TituloS'])
    listaMM.append(i['MensajeS'])

listaTitulos.append(listaTD)
listaTitulos.append(listaTM)

listaMensajes.append(listaMD)
listaMensajes.append(listaMM)

# Detecta el tamaño de las listas


# Hace Funcionar el boton de BuyMeaCoffe (PARTE ESENCIAL NO TOCAR)
url = "https://www.buymeacoffee.com/jesusartz"


def BuyMeaCoffee():
    webbrowser.open_new(url)


# Define los parametros de notificacion para Linux
def LinuxMessage(title, description):
    notify2.init('Test')
    notify = notify2.Notification(title, description)
    notify.show()
    return


# Define los parametros de notificacion para Windows
def WindowsMessage(tittle, description):
    notificacion.show_toast(tittle, description, duration=5)
    return


# Correr programa principal
def mainProgram():
    if (varDatos.get() == 1) & (varMotivacion.get() == 1):
        if platform == "linux" or platform == "linux2":
            randomNum = random.randint(0, 76)
            choiseL = [0, 1]
            choise = random.choice(choiseL)

            LinuxMessage(listaTitulos[choise][randomNum], listaMensajes[choise][randomNum])
            time.sleep(15)

        elif platform == "win32":
            randomNum = random.randint(0, 76)
            choiseL = [0, 1]
            choise = random.choice(choiseL)
            WindowsMessage(listaTitulos[choise][randomNum], listaMensajes[choise][randomNum])
            time.sleep(15)



    elif (varDatos.get() == 0) & (varMotivacion.get() == 1):
        if platform == "linux" or platform == "linux2":
            randomNum = random.randint(0, 50)

            LinuxMessage(listaTitulos[0][randomNum], listaMensajes[0][randomNum])
            time.sleep(15)

        elif platform == "win32":
            randomNum = random.randint(0, 50)
            WindowsMessage(listaTitulos[0][randomNum], listaMensajes[0][randomNum])
            time.sleep(15)


    elif (varDatos.get() == 1) & (varMotivacion.get() == 0):

        if platform == "linux" or platform == "linux2":
            randomNum = random.randint(51, 76)
            LinuxMessage(listaTitulos[1][randomNum], listaMensajes[1][randomNum])
            time.sleep(15)

        elif platform == "win32":
            randomNum = random.randint(51, 76)
            WindowsMessage(listaTitulos[1][randomNum], listaMensajes[1][randomNum])
            time.sleep(15)


# Esta funcion crea un hilo en el sistema para poder usar la interfaz a la vez que el bucle se ejecuta
def bucle():
    global stop_threads
    stop_threads = False
    while True:

        mainProgram()

        if stop_threads == True:
            break
        # Vale verga la eficiencia


def Stop():
    global stop_threads
    stop_threads = True


# Botones y Checkbuttons

botonInicio = Button(text="Start", command=lambda: threading.Thread(target=bucle).start())

c2 = Checkbutton(root, text="Motivacion", variable=varDatos, onvalue=1, offvalue=0)
c3 = Checkbutton(root, text="Datos Curioso", variable=varMotivacion, onvalue=1, offvalue=0)

c2.place(x=100, y=300)
c3.place(x=100, y=275)
botonStop = Button(text="Stop", command=Stop)
botonCoffee = Button(text="Buy Me a Coffee", command=BuyMeaCoffee)
botonCoffee.place(x=450, y=400)
botonStop.place(x=300, y=400)
botonInicio.place(x=150, y=400)

# Main Loop

root.mainloop()
