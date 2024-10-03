datas = []
novaData = ''

for i in range(5):
    novaData = input('Digite uma data DD-MM-YYYY: ')
    datas.append(novaData)
    datas[i].replace('-', '/')

for data in datas:
    print(data)
