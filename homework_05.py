# task 1. Знайдіть всі унікальні елементи в списку small_list
small_list = [3, 1, 4, 5, 2, 5, 3]
set_small_list=set(small_list)
small_list = list(set_small_list)
print(small_list)


# task 2. Знайдіть середнє арифметичне всіх елементів у списку small_list
sum_of_list = sum(small_list)
lenght_of_list = len(small_list)
middle_arithmetic = sum_of_list / lenght_of_list
print(middle_arithmetic)

# task 3. Перевірте, чи є в списку big_list дублікати
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
set_big_list = set(big_list)
lenght_of_big_list = len(big_list)
lenght_of_unique_list = len(set_big_list)

if lenght_of_unique_list < lenght_of_big_list:
    print('Дублікати в списку big_list є')
else:
    print('Дублікатів нема')

# task 4. Знайдіть ключ з максимальним значенням у словнику add_dict
base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
max_value = max(add_dict.values())
print(f'Найбільше значення в словнику:{max_value}')



# task 5. Створіть новий словник, в якому ключі та значення base_dict будуть
# замінені місцями ({'Ukraine':'contry'...})
base_dict_updated ={} 
for  i , j in base_dict.items():
    base_dict_updated.update({j:i})
print (base_dict_updated)

# task 6. Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
# print(base_dict)
# print(add_dict)

# sum_dict = {**base_dict,**add_dict} 
# print (sum_dict)                    

# task 7.
line = "Створіть множину всіх символів, які входять у заданий рядок"
set_line = set(line)
print(set_line)

# task 8. Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
diff_set = set_1 | set_2
print(diff_set)
sum_value = sum(diff_set)
print(sum_value)

# task 9. Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
list_1 = ['a','b','c','d','e','e']
list_2 = ['t','e','e','d','m']
list_1.extend(list_2)
my_set = set(list_1)
new_list = list(my_set) #якщо повернути сет, то print(my_set)
print(new_list) #якщо створити список з унікальними елементами, то сет в список назад

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]

# task 10. Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}

# sorted_person_list = dict(person_list)
# print (sorted_person_list)