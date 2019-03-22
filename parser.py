fp = open('names.csv', 'r')
result = []
dic = {}
headers = input("Файл содержит заголовки? (д/н)")
delim = input("Используемый разделитель: ")



names = fp.readlines()

def no_title():
    for i in names:
        #i = i[:(len(i)-1)]
        
        line = i.split(delim)
        result.append(line)
    
    n = 0
    while n < len(result):

        dic[result[n][0]] = result[n][1:]
        n += 1
    print(dic)


def with_title():
    for i in names:
        #i = i[:(len(i)-1)]
        
        line = i.split(delim)
        result.append(line)
    n = 0
    lst = []
    while n < len(result[0]):
        for i in result[1:]:
            lst.append(i[n])
        
        dic[result[0][n]] = lst
        n += 1
        lst = []
    print(dic)

if headers == 'д':
    with_title()
elif headers == 'н':
    no_title()



fp.close()

