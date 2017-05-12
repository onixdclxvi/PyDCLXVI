import os

def banner():
    print("-----------------------------")
    print("# Coded By @O*nix #DCLXVI.PRO")
    print("-----------------------------")
banner()

filename = input(str('''Введите имя TXT файла, или введите - allfile, для парсинга всех файлов в директории:'''))

if filename == ("allfile"):

    # filetype = input('Введите расширение файла:')
    filetype = (".txt")
    fileresult = input('Введите имя файла с результатом работы:')
    searchinfo = input('Что должно содержаться в строке?:')

    print ('Ищем по всем' + " " + filetype + " " + 'файлам...')

    def searchdata(f):
        result = open((fileresult + filetype), 'a')
        files = open(f, 'r').readlines()
        for i in files:
            if i.count(searchinfo):
                    result.write(i)

    for d, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith('.txt'):
                searchdata(f)

    closefile = open(fileresult + filetype)
    closefile.close()

    print ("Парсинг файлов закончен")

else:

    # filetype = input('Введите расширение файла:')
    filetype = (".txt")
    fileresult = input('Введите имя файла с результатом работы:')
    searchinfo = input('Что должно содержаться в строке?:')


    print ("Ищем по конкретному файлу" + " " + filename + filetype)

    def searchdata(f):
        result = open((fileresult + filetype), 'a')
        files = open(f, 'r').readlines()
        for i in files:
            if i.count(searchinfo):
                    result.write(i)

    for d, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith(filename + '.txt'):
                searchdata(f)

    closefile = open(fileresult + filetype)
    closefile.close()

    print ("Парсинг файла закончен")

