# Реализуйте программу, которая будет вычислять количество различных объектов в списке.
# Два объекта a и b считаются различными, если a is b равно False.
#
# Вашей программе доступна переменная с названием objects, которая ссылается на список,
# содержащий не более 100 объектов. Выведите количество различных объектов в этом списке.
new = []
for i in objects:
    new.append(id(i))
new = set(new)
print(len(new))