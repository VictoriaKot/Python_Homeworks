import pytest
"""
Тести для файлу tasks.py
Запуск: pytest test_tasks.py
"""
from functions_for_test import *

"""
📝 Завдання 1. Перевірка додавання чисел 
Напиши тест на функцію add(a, b), яка повертає суму двох чисел. 
Створи тест, який перевіряє кілька випадків: додавання додатних, від’ємних і нуля.
"""
def test_add_positive():
    assert add(5,6) == 11
    
def test_add_negative():
    assert add (-4,-6) == -10
    assert add (-4, 0) == -4
    assert add (-4, 2) == -2
def test_add_zero():
    assert add(5, 0) == 5
    assert add(0, -5) == -5
    assert add(0, 0) == 0


"""
📝 Завдання 2. Перевірка парності 
Функція is_even(n) повертає True, якщо число парне, інакше False. 
Напиши тести для кількох чисел: парних, непарних, від’ємних.
"""
def test_is_even_pair():
    assert is_even(8) == True
def test_is_even_unpair():
    assert is_even(7) == False
def test_is_even_negative():
    assert is_even(-7) == False

"""
📝 Завдання 3. Розворот рядка 
Функція reverse_string(s) повинна повертати рядок у зворотному порядку. 
Перевір: звичайний рядок, порожній рядок, рядок з одним символом.
"""
def test_reverse_string_common():
   assert reverse_string("string") == "gnirts"
def test_reverse_string_empty():
    assert reverse_string("") == ""
def test_reverse_string_one():
    assert reverse_string("d") == "d"   


"""
📝 Завдання 4. Мінімум у списку 
Функція find_min(nums) повертає найменший елемент списку. 
Протестуй для: звичайного списку, списку з одним елементом, списку з від’ємними числами.
"""
def test_find_min_common():
    nums = [56,67,78,89]
    assert find_min(nums) == 56
def test_find_min_one():
    one_element = [70]
    assert find_min(one_element) == 70
def test_find_min_negative():
    negative_elememts= [-56,-67,-78,-89]
    assert find_min(negative_elememts) == -89
    


"""
📝 Завдання 5. Перевірка підрядка 
Функція contains_substring(s, sub) повертає True, якщо sub є в s. 
Протестуй випадки: підрядок є, підрядка нема, порожній підрядок.
"""
def test_contains_substring():
    s = "elementary"
    sub = "elem"
    assert contains_substring(s, sub) == True
def test_contains_no_sub():
   assert contains_substring("elementary", "eles") == False
def test_contains_substring_empty():
   assert contains_substring("elementary", " ") == False


"""
📝 Завдання 6. Факторіал 
Функція factorial(n) обчислює факторіал числа n. 
Протестуй: factorial(0), factorial(1), factorial(5).
"""
def test_factorial_0():
    assert factorial(0) == 1
def test_factorial_1():
   assert factorial(1) == 1
def test_factorial_5():
   assert factorial(5) == 120


"""
📝 Завдання 7. Ділення з винятком 
Функція divide(a, b) ділить a на b. 
Перевір: звичайне ділення, ділення на від’ємне число, ділення на нуль (очікуваний ZeroDivisionError).
"""
def test_divide_common():
    assert divide(54, 6) == 9
def test_divide_neg():
    assert divide(54, -6) == -9
def test_divide_sero():
    with pytest.raises(ValueError):
        divide (56, 0)    
        
    

"""
📝 Завдання 8. Паліндром 
Функція is_palindrome(s) перевіряє, чи є рядок паліндромом. 
Протестуй: паліндром, непаліндром, порожній рядок.
"""
def test_is_palindrome_positive():
    assert is_palindrome ("наган") == True
def test_is_palindrome_negative():
    assert is_palindrome ("діду") == False
def test_is_palindrome_empty():
    assert is_palindrome (" ") == True


"""
📝 Завдання 9. Сума елементів списку 
Функція sum_list(nums) повертає суму всіх чисел у списку. 
Протестуй: звичайний список, порожній список, список з від’ємними числами.
"""
def test_sum_list_common():
    list1 = [5, 8, 34]
    assert sum_list(list1) == 47
def test_sum_list_empty():
    list_empty = []
    assert sum_list(list_empty) == 0
def test_sum_list_negative():
    list_neg = [-5, -8, -34]
    assert sum_list(list_neg) == -47
   


"""
📝 Завдання 10. Конвертація в верхній регістр 
Функція to_upper(s) повертає рядок у верхньому регістрі. 
Протестуй: звичайний рядок, вже великими літерами, порожній рядок.
"""
def test_to_upper_low():
    assert to_upper("слово") == "СЛОВО"
def test_to_upper_high():
    assert to_upper("ДІД") == "ДІД"
def test_to_upper_empty():
    assert to_upper(" ") == " "    
