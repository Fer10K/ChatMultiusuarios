import socket, threading

clientes_conectados = []

def broadcast(mensaje, conexion_res):
    for cliente in clientes_conectados:
                    if cliente != conexion_res:
                        cliente.send(f"{mensaje}".encode())


def atender_cliente(conexion, direccion):
    clientes_conectados.append(conexion)
    broadcast(f"{direccion}: se ha unido al chat", conexion)
    try:
        while True:
            datos=conexion.recv(1024).decode()
            if not datos:
                break
            mensaje = f"{direccion}: {datos}"
            broadcast(mensaje, conexion)
    finally:
        clientes_conectados.remove(conexion)
        broadcast(f"{direccion} ha salido del chat", conexion)
        conexion.close()
        print(f"Cliente desconectado: {direccion}")

servidor=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
servidor.bind(("localhost", 5000))
servidor.listen()
print("Servidor escuchando en el puerto 5000")

while True:
    conexion, direccion = servidor.accept()
    if len(clientes_conectados) < 5:
        print(f"Cliente conectado: {direccion}")
        hilo = threading.Thread(
            target=atender_cliente,
            args=(conexion, direccion)
        )
        hilo.start()
    else:
        print(f"direccion: {direccion}, rechazada")
        conexion.send("Servidor lleno".encode())
        conexion.close()