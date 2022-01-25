import random

print("Input quantity of arrays")
n = int(input())

random_numbers = random.sample(range(1000), n)  #создание списка с рандомными числами и размером n
list_of_arrays = [i for i in range(0,n)]    #создание массива
print(random_numbers)


def sorting(n):
    i = 0
    for i in range(n):  #генерация массивов с рандомной, уникальной длиной, и последующая их сортивка
        list_of_arrays[i] = random.sample(range(1000), random_numbers[i]) #заполнение массива рандомными числами
        if random_numbers[i] % 2 == 0:
            list_of_arrays[i].sort()    #если размер массива четный, то по возрастанию
        else:
            list_of_arrays[i].sort(reverse=True)  #если нечетный, то по убыванию
    return(list_of_arrays)


result = sorting(n)

print("Total list with sortered arrays:\n","------------------------ \n", result)
