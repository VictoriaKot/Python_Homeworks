# task 1
import math
import numbers
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та виправити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while multiplier >=0:
        result = number * multiplier
        # десь тут помилка, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_of_two_digits(a,b):
    return a+b
sum = sum_of_two_digits(7,9)
print(sum)
    

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def middle_arythmetic (numbers):
    total_numbers = 0
    for number in numbers:
        total_numbers = total_numbers + number
    mid_arytm = total_numbers / len(numbers)
    return mid_arytm
new_list = [1,5,6,9,12]
average_value = middle_arythmetic(new_list)
print(f'Average value for the list: {new_list} is {average_value}')
#task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def zadom_napered (str):
    result = ''
    for char in range (len(str) -1, -1,-1):
        result+=str[char]
    return result
my_text = zadom_napered('Hello World!')
print( my_text)
# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def longest_word(text):
    return max(text, key = len)
my_list = ['banana', 'monkey', 'tree', 'condition']
find_longest_word = longest_word(my_list)
print (f'The longest word in the list {my_list} is {find_longest_word}')
    
    
# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    index = str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
def checkig_leap_year(year):  #функція по перевірці високоснго року
    if (year%4==0 and year%100!=0) or year%400==0:
        return (' Високосний рік')
    else:
        return('Рік не високосний')
my_birth_year = int(input('Рік вашогo народження:'))
check_my_year = checkig_leap_year(my_birth_year)
print(f'Ваш рік народження {my_birth_year}: {check_my_year}')

# task 8 
def cooking_pizza(ingredients): #функція додавання введених через інпут їнгредієнтів до піци
    ingredients = []
    while True:
        pizza_topping = input('Введіть інгредієнт або quit для закінчення готування піци: ')
        if pizza_topping == 'quit':
            break
    ingredients.append(pizza_topping)
    return(f'піца з такими інгредієнтами готова: {ingredients}')
new_ingredients = input('Введіть інгредієнт або quit для закінчення готування піци: ')
pepperoni_pizza = cooking_pizza(new_ingredients)
print(f'Пеппероні піца з такими інгредієнтами {new_ingredients} готова')
# task 9
"""Це провал! Функція не виводить найбільше значення"""
def max_value_finder(): #знайти найбільше число з введених
    while True:
        numbers = input('')
        number_list = list(map(int, numbers.split(" ")))
        max_number = max(number_list)
        if numbers == '0':
            break
    return(max_number)
my_list = input('Введіть декілька чисел через пробіл або 0 для закінчуння: ')
my_max_number = max_value_finder(my_list)
print(f'максимальне число зі списку {my_list}: {my_max_number}')

# task 10
def total_of_sets (set_1,set_2):   # Функція обєднує 2 сети в один
    united_sets = set_1 | set_2
    return united_sets
my_set = {'cheese', 'bread', 'meat', 'fish', 'tomato'}
friends_set = {'cheese', 'tomato', 'cucumbers'} 
our_list_products = total_of_sets(my_set,friends_set) 
print(f'На природу беремо: {our_list_products}')
  
    
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обов'язково документуйте функції та дайте зрозумілі імена змінним.
"""

        