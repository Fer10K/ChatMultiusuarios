import socket
import threading
from colorama import Fore, Style, init

init()

cliente = socket.socket()
cliente.connect(("localhost", 5000))

direccion = str(cliente.getsockname())

respuesta = cliente.recv(1024).decode()

if respuesta == "Servidor lleno":
    print(respuesta)
    cliente.close()
    exit()

isActive = True


def mostrar(mensaje):
    color = Fore.GREEN if direccion in mensaje else Fore.CYAN
    print("\r\033[K" + color + mensaje + Style.RESET_ALL)

    if isActive:
        print(f"{Fore.GREEN}{direccion}: {Style.RESET_ALL}", end="", flush=True)


def escuchar():
    global isActive

    while isActive:
        try:
            mensaje = cliente.recv(1024).decode()

            if not mensaje:
                break

            mostrar(mensaje)

        except:
            break


threading.Thread(target=escuchar, daemon=True).start()

try:
    while isActive:
        mensaje = input(f"{Fore.GREEN}{direccion}: {Style.RESET_ALL}")
        cliente.send(mensaje.encode())

except KeyboardInterrupt:
    pass

finally:
    isActive = False
    cliente.close()