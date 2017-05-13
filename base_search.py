import os
import argparse
import sys

def banner():
    print('''
----------------------------------\n
# Coded By @O*nix #DCLXVI.PRO v1.2\n
----------------------------------''')
banner()

info = ('''
Usage: ./base_searche.py [options]
Options: -f,    --filename   <targetfile> указать -f allfile для поиска по всем файлам директории  |   Имя файла без расширения
         -r,    --fileresult <result_filename>                                                     |   Имя файла для записи результатов
         -s,    --searchinfo <search_info>                                                         |   Какую информацию искать в строках
         -h,    --help       <help>                                                                |   Справка\n
Example: ./base_searche.py -f base -r resultfile -s manager <- Поиск по конкретному файлу
Example: ./base_searche.py -а allfile -r resultfile -s manager <- Поиск по всем файлам в директории
Удаление дубликатов автоматическое.
''')

def help():
    print (info)
    sys.exit(0)

#filename = input(str('''Введите имя TXT файла, или введите - allfile, для парсинга всех файлов в директории:'''))

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename")
parser.add_argument("-r", "--fileresult")
parser.add_argument("-s", "--searchinfo")

args = parser.parse_args()

if not args.filename or not args.fileresult or not args.searchinfo:
    help()
    sys.exit(0)

filename = args.filename
fileresult = args.fileresult
searchinfo = args.searchinfo

if filename == ("allfile"):
    filetype = (".txt")

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
    print ("Удаляем дубликаты...")

    input = open((fileresult + filetype), 'r')
    output = open((fileresult + "_nodubles" + filetype), 'w')
    linesarraу = input.readlines()
    input.close()
    seen = []
    for line in linesarraу:
        if line not in seen:
            seen.append(line)
    output.writelines(seen)

    print ("Дубликаты удалены")
    print ("Работа завершена")

else:
    filetype = (".txt")
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
    print ("Удаляем дубликаты")

    input = open((fileresult + filetype), 'r')
    output = open((fileresult + "_nodubles" + filetype), 'w')
    linesarraу = input.readlines()
    input.close()
    seen = []
    for line in linesarraу:
        if line not in seen:
            seen.append(line)
    output.writelines(seen)

    print ("Дубликаты удалены")
    print ("Работа завершена")
