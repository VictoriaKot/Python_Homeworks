adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while 
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

# УВАГА! Перезаписуйте вміст змінної adwentures_of_tom_sawer у завданнях 01-03

# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

new_adwentures = adwentures_of_tom_sawer.replace("\n", " ")
print (f"Task 01:{new_adwentures}")
print()
# task 02 ==
""" Замініть .... на пробіл
"""
new_adwentures_task2= new_adwentures.replace ("....", " ")
print (f"Task 2: {new_adwentures_task2}")
print()

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
new_adwentures_task3 = new_adwentures_task2.replace("  ", " ")
print (f"Task 3: {new_adwentures_task3}")
print()

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
new_adwentures_task4 = new_adwentures_task3.count("h")
print (f"Task 4: {new_adwentures_task4}")

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
підказка - порахувати кожну велику літеру напр, .count("A") і їх сумму
"""

new_adwentures_task5A = new_adwentures_task3.count("A")
new_adwentures_task5B = new_adwentures_task3.count("B")
new_adwentures_task5J = new_adwentures_task3.count("J")
new_adwentures_task5M = new_adwentures_task3.count("M")
new_adwentures_task5F = new_adwentures_task3.count("F")
new_adwentures_task5T = new_adwentures_task3.count ("T")
new_adwentures_task5 = new_adwentures_task5A+new_adwentures_task5B+new_adwentures_task5F+new_adwentures_task5M+new_adwentures_task5J+new_adwentures_task5T
print(f"Task 5: {new_adwentures_task5}")


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
new_adwentures_task6 = new_adwentures_task3.find ("Tom")
new_adwentures_task6 = new_adwentures_task3.find("Tom", new_adwentures_task6 + 1)
print (new_adwentures_task6)

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = new_adwentures_task3.split (". ")
print (f"Task 7: {adwentures_of_tom_sawer_sentences}")
print()

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
new_adwentures_task8 = adwentures_of_tom_sawer_sentences[3]
print (f"Task 8: {new_adwentures_task8.lower()}")
print()


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
new_adwentures_task9 = new_adwentures_task3.find("By the time")
if new_adwentures_task9 == -1:
    print ("В тексті нема речень, які починаються на 'By the time'")
else:
    print ("Task 9.В тексті є речення, які починаються на 'By the time'")           

print()

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
new_adwentures_task10a = adwentures_of_tom_sawer_sentences[-1]
new_adwentures_task10 = new_adwentures_task10a.split(" ")
print (f"Task 10. Кількість слів в останньому реченні: {len(new_adwentures_task10)}")