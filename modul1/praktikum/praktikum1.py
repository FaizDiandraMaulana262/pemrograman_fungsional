import json
import ast
import os


def userVerification(username):
    fileUser = open("user.txt", "r")
    for x in fileUser.readlines():
        if (username == json.loads(x)[1]):
            if (json.loads(x)[0] == "user"):
                userFun(json.loads(x)[1])
            elif (json.loads(x)[0] == "admin"):
                adminFun(json.loads(x)[1])


def userBorrow(username):
    count = 0
    arrBorrow = []
    fileUserBorrow = open("borrow.txt", "r")
    fileUserBorrow2 = open("borrow1.txt", "a")
    fileBook2 = open("book1.txt", "a")
    fileBook = open("book.txt", "r")
    inputID = str(input("Input Book ID : "))

    for x in fileBook.readlines():
        if (inputID == ast.literal_eval(x)[0]):
            if (ast.literal_eval(x)[2] < 1):
                print("Stock Buku Habis")
                arrBorrow = [ast.literal_eval(x)[0], ast.literal_eval(x)[
                    1], ast.literal_eval(x)[2]]
                fileUserBorrow2.close()
                os.remove("borrow1.txt")
            else:
                countBorrow = 0
                arrBorrow = [username, inputID]
                if (countBorrow == 0):
                    fileUserBorrow2.write(str(arrBorrow))
                    fileUserBorrow2.write("\n"+fileUserBorrow.read())
                    fileUserBorrow.close()
                    fileUserBorrow2.close()
                    os.remove("borrow.txt")
                    os.renames("borrow1.txt", "borrow.txt")

                arrBorrow = [ast.literal_eval(x)[0], ast.literal_eval(x)[
                    1], ast.literal_eval(x)[2] - 1]

            if (count == 0):
                fileBook2.write(str(arrBorrow))
            else:
                fileBook2.write("\n"+str(arrBorrow))
            count = count + 1
        else:
            arrBorrow = [ast.literal_eval(x)[0], ast.literal_eval(x)[
                1], ast.literal_eval(x)[2]]
            if (count == 0):
                fileBook2.write(str(arrBorrow))
            else:
                fileBook2.write("\n"+str(arrBorrow))

            count = count + 1

    fileBook.close()
    fileBook2.close()
    os.remove("book.txt")
    os.renames("book1.txt", "book.txt")


def userReturnBook(username):
    arrBook = []
    count = 0
    fileBook = open("book.txt", "r")
    fileBook2 = open("book1.txt", "a")
    fileUserBorrow = open("borrow.txt", "r")
    fileUserBorrow2 = open("borrow1.txt", "a")
    inputID = str(input("Input Book ID : "))
    for x in fileUserBorrow.readlines():
        if (ast.literal_eval(x)[0] == username):
            if (ast.literal_eval(x)[1] == inputID):

                for i in fileBook.readlines():
                    if (ast.literal_eval(i)[0] == inputID):
                        arrBook = [ast.literal_eval(i)[0], ast.literal_eval(i)[
                            1], ast.literal_eval(i)[2] + 1]
                        print("Buku Dikembalikan")
                    else:
                        arrBook = [ast.literal_eval(i)[0], ast.literal_eval(i)[
                            1], ast.literal_eval(i)[2]]
                    
                    if(count == 0):
                        fileBook2.write(str(arrBook))
                    else:
                        fileBook2.write("\n"+str(arrBook))

                    count = count + 1
                
            else:
                fileUserBorrow2.write(x)
        else:
            fileUserBorrow2.write(x)


    fileUserBorrow.close()
    fileUserBorrow2.close()
    os.remove("borrow.txt")
    os.renames("borrow1.txt", "borrow.txt")

    fileBook.close()
    fileBook2.close()
    os.remove("book.txt")
    os.renames("book1.txt", "book.txt")


def listBook():
    fileBook = open("book.txt", "r")
    for x in fileBook.readlines():
        print("ID : "+ast.literal_eval(x)[0]+"\nNama Buku : "+ast.literal_eval(
            x)[1]+"\nStock : "+str(ast.literal_eval(x)[2])+"\n")


def addListBook():
    fileBook = open("book.txt", "a")
    bookID = str(input("Book ID : "))
    bookName = str(input("Book Name : "))
    bookStock = int(input("Book Stock : "))

    arrBook = [bookID, bookName, bookStock]
    fileBook.write("\n"+str(arrBook))


def userFun(username):
    loopThisFun = True
    while (loopThisFun):
        print("Welcome "+username +
              "\n\n=== Menu ===\n0. Exit\n1. Pinjam Buku\n2. Lihat List Buku\n3. Kembalikan Buku\n\nInput : ")
        inNumber = int(input())
        if (inNumber == 0):
            loopThisFun = False
            print("Terimakasih :D")
        elif (inNumber == 1):
            userBorrow(username)
        elif (inNumber == 2):
            listBook()
        elif (inNumber == 3):
            userReturnBook(username)


def adminFun(username):
    loopThisFun = True
    while (loopThisFun):
        print("Welcome "+username +
              "\n\n=== Menu ===\n0. Exit\n1. Tambahkan Buku\n2. Lihat List Buku\n\nInput : ")
        inNumber = int(input())
        if (inNumber == 0):
            loopThisFun = False
        elif (inNumber == 1):
            addListBook()


userVerification("test")
