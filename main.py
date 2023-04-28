import threading
import os

def start_servidor():
    print('servidor: 1.00.00')
    os.system("python servidor.py")

def start_manage():
    print('delivery: 1.00.00')
    os.system("python manage.py runserver 192.168.0.50:5000")

def start_impressoras():
    print('impressora: 1.00.00')
    os.system("python impressoras.py")

def start_estoque():
    print('estoque: 1.00.00')
    os.system("python estoque.py")

def start_terminais():
    print('terminais: 1.00.00')
    os.system("python terminais.py")

def start_cozinha():
    print('cozinha: 1.00.00')
    os.system("python cozinha.py")

if __name__ == "__main__":
    print('iniciando Serviço...')
    thread1 = threading.Thread(target=start_servidor)
    thread2 = threading.Thread(target=start_manage)
    thread3 = threading.Thread(target=start_impressoras)
    thread4 = threading.Thread(target=start_estoque)
    thread5 = threading.Thread(target=start_terminais)
    thread6 = threading.Thread(target=start_cozinha)

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()

    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()
