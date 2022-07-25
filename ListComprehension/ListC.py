# Очень быстро создает списки
# [exp for item in iterable]
# [exp for item in iterable (if conditional)]
# [exp <if conditional> for item in iterable (if conditional)]

#list = []

#for i in range(1,101):
    #if(i%2 ==0):
        #list.append(i)

#print(list)

# list = [i for i in range(1,21) if i%2 == 0] - красивее и быстрее без структуры
# print(list)

#list = [(i,i) for i in range(1,21) if i%2 == 0] # кортежи
#print(list)

# def f(x):
   # return x**3

#list = [(i,f(i)) for i in range(1,21) if i%2 == 0] # числа и их кубы в кортежах с вызовом функции
#print(list) 

#path = 'C:\\Users\\mob19\\OneDrive\\Рабочий стол\\Python_Lec_3\\List Comprehension\\text.txt'
#f = open(path, 'r')
#data = f.read() + ' ' # считывает и добавляет пробел
#f.close()

#numbers = []

#while data != '':
    #space_pos = data.index(' ') # найти первую позицию пробела
    #numbers.append(int(data[:space_pos])) # взять то, что находится до первой позиции пробела, превратить в число и добавить в список
    #data = data[space_pos+1:] # обновить строку

#out = []

#for e in numbers:
    #if not e % 2:
        #out.append((e,e**2))
#print(out)

# def f(x):
    # return x**2

# list = [(i,f(i)) for i in list1 if i%2 == 0]
# print(list)

def select(f, col):
    return [f(x) for x in col]

def where(f,col):
    return [x for x in col if f(x)]

data = '1 2 3 5 8 15 23 38'.split()

res = select(int, data) # передает список в функцию и преобразует их в список
res = where(lambda x: not x%2, res) # заносит в список только четные числа
res = select(lambda x:(x,x**2),res) # заносит в список кортеж числа и его квадрата
print(res)
