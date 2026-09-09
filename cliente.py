import socket, sys, threading

def escuchar(cliente):
    while True:
        try:
            respuesta = cliente.recv(1024).decode()
            if not respuesta:
                break

            print(f"{respuesta}")
        except Exception:
            break

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(("localhost", 5000))
hilo_escuchar = threading.Thread(
    target=escuchar, args=(cliente,)
)
hilo_escuchar.start()

if len(sys.argv) > 1:
    cliente.send(sys.argv[1].encode())

try:
    while True:
        nuevo_mensaje = input()
        cliente.send(nuevo_mensaje.encode())
except KeyboardInterrupt:
    cliente.close()