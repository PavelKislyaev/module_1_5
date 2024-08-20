immutable_var=10 , 5.5 , 'Camel' , "Верблюд" , False , True , bool #создаём кортеж с разными типами данных
print(immutable_var) #выводим данный кортеж
print(type(immutable_var))
print(immutable_var[0]) #можно обратиться к элементам по их индексу
#immutable_var[0]=25 #элементы внутри кортежа неизменяемы но может хранить внутри себя изменяемые объекты(список)
mutable_list='Элемент' , 'concatenate' , 'Синий' , 'Красный'
print(mutable_list)
mutable_list=(['Элемент' , 'concatenate'] ,['Синий' , 'Красный'] ) #создаём список в нутри кортежа
print(mutable_list)
mutable_list[0][1]='4K Ultra' #для изменения в нём элементов
print(mutable_list)
mutable_list[1][0]='Клетчатый'
print(mutable_list)