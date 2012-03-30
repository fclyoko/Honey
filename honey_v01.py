#!/usr/bin/python
#Honey v0.1 - Http Server
#Autor: Francisco Hdez (lko)
#Email: fclyoko@gmail.com

import socket, sys, time

def logs(data, addr):
    f=open("honey","a")
    f.write("Conexion recibida: %s:%s - %s\n\n%s" % (addr[0], addr[1], time.ctime(), data))
    f.close()
    
if __name__=='__main__':
  
    if len(sys.argv) != 2:
        print "\n[+] Uso: %s <Puerto>\n" % (sys.argv[0])
        exit()
    else: 
        if (int(sys.argv[1]) < 1) or (int(sys.argv[1]) > 65535):
	    print "\n[+] Error: El puerto tiene que ser un numero entre 1 y 65535\n"
	    exit()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('', int(sys.argv[1])))
    s.listen(1)

    print "\n[+] Escuchando en el puerto %s...\n" % (int(sys.argv[1]))

    while 1:
        conn, addr = s.accept() 
        print "Conexion recibida: %s:%s - %s" % (addr[0], addr[1], time.ctime())
        data = conn.recv(1024)
        conn.send("<html><head><title>System Admin - Database Dump -</title></head><body>MD5 Hash password: 9373393390934b64ebd10852acec7cbc<br /> -- Honey/0.1 Database Dump 29/03/2012 06:37:45 --</body></html>")
        conn.close()
        logs(data, addr)