import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="пкшырфыйд007",
    database = "passport"
)
mycursor = mydb.cursor()


import image_processing
import tesseract

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('192.168.1.186', 3000))
server.listen()
print('Server is working...')




client_socket, address = server.accept()
while True:

    with open('passport.jpg', "wb") as file:
        data = client_socket.recv(4096)
        print(len(data))
        file.write(data)
        while data:
            data = client_socket.recv(4096)
            #if not data: break
            print(len(data))
            file.write(data)

            if (len(data) < 4096): break

        passport = image_processing.Passport("passport.jpg")
        isProcessSuccess = passport.processFullName()

        if (isProcessSuccess == False):
            print('error')
            client_socket.send("Плохое качество фото".encode())

        else:
            res = ""
            surnameFilePaths = passport.getProcessedSurnameFilePaths()
            nameFilePaths = passport.getProcessedNameFilePaths()
            patronymicFilePaths = passport.getProcessedPatronymicFilePaths()
            name = tesseract.ocr_core('img/name.jpg')
            surname = tesseract.ocr_core('img/surname.jpg')
            patronymic = tesseract.ocr_core('img/patronymic.jpg')
            print(name)
            print(surname)
            print(patronymic)

            query = 'INSERT INTO people (name,surname,patronymic) VALUES (%s, %s, %s)'
            val = (name,surname,patronymic)
            mycursor.execute(query, val)
            mydb.commit()

            res = surname + name + patronymic
            if (res==""):
                client_socket.send("Плохое качество фото".encode())
            else:
                res_str = res.encode()
                client_socket.send(res_str)

