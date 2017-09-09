import os
import argparse
import sys
import fnmatch

def banner():
    print('''
----------------------------------
# Coded By @O*nix v1.3
----------------------------------''')
banner()

info = ('''
Usage: ./base_searche.py [options]
Options: -f,    --filename   <targetfile> указать -f allfile для поиска по всем файлам директории  |   Имя файла без расширения
         -r,    --fileresult <result_filename>                                                     |   Имя файла для записи результатов
         -t,    --filetype   <type_file>                                                           |   Тип файл например .txt
         -s,    --searchinfo <search_info>                                                         |   Какую информацию искать в строках
         -h,    --help       <help>                                                                |   Справка\n
Example: ./base_searche.py -f base -r resultfile -s manager <- Поиск по конкретному файлу
Example: ./base_searche.py -а allfile -r resultfile -s manager <- Поиск по всем файлам в директории
''')

def help():
    print (info)
    sys.exit(0)

parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filename")
parser.add_argument("-r", "--fileresult")
parser.add_argument("-s", "--searchinfo")
parser.add_argument("-t", "--filetype")

args = parser.parse_args()

if not args.filename or not args.fileresult or not args.searchinfo:
    help()
    sys.exit(0)

filename = args.filename
fileresult = args.fileresult
filetype = args.filetype
searchinfo = args.searchinfo

message_pars = ('''Парсинг файлов закончен\nУдаляем дубликаты''')
message_duble = ('''Дубликаты удалены\nРабота завершена''')

if filename == ("allfile"):

    print ('Ищем по всем' + " " + filetype + " " + 'файлам...')

    def searchdata(f):
        result = open((fileresult + filetype), 'a')
        files = open(f, 'r').readlines()
        for i in files:
            if i.count(searchinfo):
                result.write(i)

    for d, dirs, files in os.walk('.'):
        for f in files:
            if f.endswith(filetype):
                searchdata(f)

    closefile = open(fileresult + filetype)
    closefile.close()

    print (message_pars)

    input = open((fileresult + filetype), 'r')
    output = open((fileresult + "_nodubles" + filetype), 'w')
    lines = input.readlines()
    input.close()
    seen = []
    for line in lines:
        if line not in seen:
            seen.append(line)
    output.writelines(seen)

    print (message_duble)
    sys.exit(0)

else:
    try:
        file = open(filename + filetype)
    except IOError as e:
        print("Файла не существует!")
        sys.exit(0)
    else:
        with file:

            print ("Ищем по файлу" + " " + filename + filetype)

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

    print (message_pars)

    input = open((fileresult + filetype), 'r')
    output = open((fileresult + "_nodubles" + filetype), 'w')
    linesarraу = input.readlines()
    input.close()
    seen = []
    for line in linesarraу:
        if line not in seen:
            seen.append(line)
    output.writelines(seen)

    print (message_duble)
    sys.exit(0)
