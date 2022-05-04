import socket


# функция записывает логи в файл
# не очень понял, надо писать просто что получили или надо для всех писать в логи: Спортсмен ...
def writer(mess):
    with open('log.txt', 'a+', encoding='UTF-8') as f:
        f.write(message + '\n')


# создаем сокет
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Порт и адрес хоста
PORT = 8002
HOST = 'localhost'

# бинд сокета
sock.bind((HOST, PORT))
# слушаем сокет
sock.listen(5)
# принимаем соединения
(clientsock, address) = sock.accept()
# Establish and accept connections with client
print(f"Новое соединение от {address}")
try:
    while True:
        # Получаем сообщение от клиента
        message = clientsock.recv(1024)
        # декодируем и отрезаем перенос строки
        message = message.decode('utf-8')[:-1]
        writer(message)
        # удаляем CR и разбиваем все слова по пробелу
        message = message.replace('[CR]', '').split()
        # номер участника
        BBBB = message[0]
        # id канала
        NN = message[1]
        # время. Не понял надо ли его округлять? Тут не округлял, но если надо сделаю
        t = message[2][:-2]
        GG = message[3]
        if GG == "00":
            print(f'Спортсмен, нагрудный номер {BBBB} прошёл отсечку {NN} в "{t}"')
        # если минуту нет сообщений, то закрываем соединение
        if not message:
            clientsock.close()
        # # посылаем ответ, что всё окей
        # reply = 'OK!\n'
        # # отображаем ответ на клиенте
        # clientsock.sendall(str.encode(reply))
except KeyboardInterrupt:
    # Закрываем соединение
    clientsock.close()
    sock.close()
finally:
    # Закрываем соединение
    clientsock.close()
    sock.close()
