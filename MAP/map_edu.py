# функция мап применяет указанную ф-ю к каждому элементу итерируемого объекта(к набору данных)
#  и возвращает итератор с новыми объектами(данными)

#li = [x for x in range(1,5)]
#print(li)

#li=list(map(lambda x:x+10, li))
#print(li)

#data = list(map(int, input().split())) #выдаст списком
#print(data)

#data = map(int, input().split())

#for e in data: #будет много строк
    #print(e)

#data = map(int, '1 2 3 55 6'.split())
#for e in data: #будет много строк
 #   print(e)

#data = list(map(int, '1 2 3'.split())) # если работать без списка, то пробегать будет 1 раз
#for e in data: #если использовать список - то данные сохранятся и по списку пробегутся еще
#    print(e)

#print('--')

#for e in data: 
#    print(e)


def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data) # передает список в функцию и преобразует их в список
res = where(lambda x: not x%2, res) # заносит в список только четные числа
res = list(map(lambda x:(x,x**2),res)) # заносит в список кортеж числа и его квадрата
print(res)