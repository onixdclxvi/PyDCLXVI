import re
import csv
import requests
from multiprocessing.dummy import Pool as ThreadPool


def get_links(file):
    lists = []
    data = open(file, 'r').read()
    pattern = '(?:[\w\.]+)\.(?:[a-z]{2,6}\.?)'
    result = re.findall(pattern, data)
    for url in list(set(result)):
        lists.append("https://" + url)
        lists.append("http://" + url)
    print(f'Всего {len(lists)} элементов')
    return lists


def write_in_file(data):
    with open('result.csv', "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def main(file):
    urls = get_links(file)
    with ThreadPool(30) as p:
        p.map(core_check, urls)
    p.close()
    p.join()


def core_check(page_url):

        internet = requests.get('http://data.alexa.com/data?cli=10&dat=s&url=google.com')
        if internet.status_code == 200:
            try:
                open_url = requests.get(page_url + '/.git/HEAD', timeout=(4, 4))

                def validate(data, content):
                    if data == 200:
                        match = re.search('([a-z][a-z][a-z][:]\s[r][e][f][s]/)', content)
                        if match is None:
                            pass
                            #print(page_url + ' Не уязвимый')
                            #write_in_file([page_url, 'Не уязвимый'])
                        else:
                            print(page_url + '/.git/HEAD' + ' Уязвимый')
                            write_in_file([page_url, 'Уязвимый'])
                    else:
                        pass

                validate(open_url.status_code, str(open_url.content))

            except requests.exceptions.ReadTimeout:
                pass
                #print(f'{page_url} Таймаут чтения сайта')
                #write_in_file([page_url, 'Таймаут чтения сайта'])
            except requests.exceptions.ConnectTimeout:
                pass
                #print(f'{page_url} Таймаут коннекта к сайту')
                #write_in_file([page_url, 'Таймаут коннекта к сайту'])
            except requests.exceptions.ConnectionError:
                pass
                #print(f'{page_url} Ошибка коннекта к сайту')
                #write_in_file([page_url, 'Ошибка коннекта к сайту'])
            except:
                pass
        else:
            pass
            #print(f'{page_url} Нет подключения к интернету')
            #write_in_file([page_url, 'Нет подключения к интернету'])

main('top-1m.csv')

