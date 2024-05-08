#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

#num = [element for element in a if element < 5]
#
#print(num)






#numbers = input() 
#for num in numbers:
#    if num % 5 == 0:
#        print(num)



#numbers = input()
#a = numbers[0]

#for num in numbers:
#    if num > a:
#        a = num

#print(a)

#str1 = input()

#j= []
#n = []

#for i in range(len(str1)):
#    if i % 2 == 0:
#        j.append(str1[i])
#    else:
#        n.append(str1[i])

#print(" ".join(j))




#num = input()
#for i in range(7):
#    if i != 3 and i != 6:
#        print(i, end=' ')



#n = []
#for num in range(1, 51):
#    if num % 3 ==0 and num % 5 ==0:
#        print("FizzBuzz")
#    elif num % 3 == 0:
#        print("Fizz")
#    elif num % 5 == 0:
#        print("Buzz")
#    else:
#        print(num)






#age = int(input())

#if 1 <= age <= 5:
#    num = "old"












# Инициализация переменной для суммы
total_sum = 0

# Ввод чисел и суммирование
while True:
    num = int(input("Введите число (для завершения введите 0): "))
    if num == 0:
        break
    total_sum += num

# Вывод результата
print(f"Сумма элементов последовательности: {total_sum}")















