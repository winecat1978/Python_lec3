# ф-я enumerate() применяется к итерируемому объекту
#  и возвращает новый итератор с кортежами из индекса и элементов входных данных

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4,5,9,14,7]
salary = [111,222,333]
data = list(enumerate(users))
print(data)