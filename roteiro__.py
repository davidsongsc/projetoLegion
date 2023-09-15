import threading
import os

def start_servidor1():
    print('servidor-1: 1.00.10\nservidor de post')
    os.system("python roteiro_01.py")

def start_servidor2():
    print('servidor-2: 1.00.10\nservir do roteiro')
    os.system("python roteiro_02.py")


def IniciarServico():
    print('iniciando Serviço...')
    thread1 = threading.Thread(target=start_servidor1)
    thread2 = threading.Thread(target=start_servidor2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

IniciarServico()