Chat TCP Multihilo en Python

  Servidor de chat concurrente en tiempo real construido con sockets en Python.
  Soporta hasta 5 usuarios en simultáneo mediante hilos (multithreading) y retransmite mensajes de manera bidireccional (broadcast).

Características:

  Multihilo (Multithreading): Manejo de clientes concurrentes sin bloquear el servidor.
  Límite de capacidad: Permite un máximo de 5 clientes activos simultáneamente.
  Mensajes Broadcast: Todo mensaje enviado por un usuario se retransmite automáticamente al otro cliente.
  Notificaciones de estado: Informa cuando un usuario entra o sale de la sala.

Requisitos Previos

  Python 3.x instalado en el sistema.

Uso e Instalación
  1. Iniciar el Servidor

      Abre una terminal y ejecuta el script del servidor: python servidor.py
      El servidor quedará en escucha en localhost:5000.
  
  2. Conectar Clientes

      Abre una nueva terminal por cada cliente que desees conectar: python cliente.py
