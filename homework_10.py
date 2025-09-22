"""
Шаблони класів об'єктів природи та побуту (ЗАГОТОВКИ)
Template classes for nature and household objects (TEMPLATES)

ІНСТРУКЦІЯ / INSTRUCTION:
Реалізуйте всі методи та властивості згідно з вимогами в коментарях
Implement all methods and properties according to requirements in comments
"""

import math


class Tree:
    """
    Клас природного об'єкта "Дерево"
    Class for natural object "Tree"
    
    Атрибути / Attributes:
    - height: висота дерева (0 < height < 150 метрів)
    - trunk_diameter: діаметр стовбура (0 < diameter < 1000 см)
    - leaf_count: кількість листя (обчислюється автоматично)
    """
    
    def __init__(self, height, trunk_diameter):
        """
        Ініціалізація дерева / Initialize tree
        
        Args:
            height (float): Висота дерева в метрах / Tree height in meters
            trunk_diameter (float): Діаметр стовбура в см / Trunk diameter in cm
        
        TODO: 
        - Встановити атрибути через властивості для валідації
        - Обчислити початкову кількість листя
        """
        self.__height = height
        self.__trunk_diameter = trunk_diameter
    @property
    def height(self):
        """
        Властивість: висота дерева / Property: tree height
        
        TODO: Повернути значення приватного атрибута _height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Сетер для висоти дерева / Setter for tree height
        
        TODO: 
        - Перевірити що 0 < value < 150
        - Встановити _height = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or 150< value <0:
            raise ValueError("Висота дерева має бути між 1 і 150 метрів")
        else:
            self.__height = value    
            self.__leaf_count = self.__height * self.__trunk_diameter * 100
      
    
    @property
    def trunk_diameter(self):
        """
        Властивість: діаметр стовбура / Property: trunk diameter
        
        TODO: Повернути значення приватного атрибута _trunk_diameter
        """
        return self.__trunk_diameter
    
    @trunk_diameter.setter
    def trunk_diameter(self, value):
        """
        Сетер для діаметра стовбура / Setter for trunk diameter
        
        TODO:
        - Перевірити що 0 < value < 1000
        - Встановити _trunk_diameter = value
        - Перерахувати кількість листя
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value, (int, float)) or not 0 < value < 1000:
            raise ValueError("Невірний діаметр стовбура")
        self.__trunk_diameter = value
        self.__leaf_count = self.__height * self.__trunk_diameter * 100
        print (f"Діаметр стовбура: {self.__trunk_diameter} і листя {self.__leaf_count}") 
       
    @property
    def leaf_count(self):
        """
        Властивість: кількість листя (тільки читання) / Property: leaf count (read-only)
        
        TODO: Повернути значення _leaf_count
        """
        print(f"Це дерево має {self.__leaf_count} листя.")
      
    
    def _calculate_leaf_count(self):
        """
        Приватний метод: обчислення кількості листя / Private method: calculate leaf count
        
        Формула: height * trunk_diameter * 100
        
        TODO: 
        - Обчислити кількість листя за формулою
        - Повернути результат
        """
        self.__leaf_count = self.__height * self.__trunk_diameter * 100
        return self.__leaf_count
    
    def grow(self):
        """
        Метод: ріст дерева / Method: tree growth
        
        TODO:
        - Збільшити висоту на 0.5 м (але не більше 149.9)
        - Збільшити діаметр стовбура на 2 см (але не більше 999.9)
        - Використовувати властивості для автоматичного перерахунку листя
        - Вивести повідомлення про ріст
        """
        new_height = self.__height + 0.5
        if new_height > 149.9:
            return "Дерево зависоке"
        
        new_trunk_diameter = self.__trunk_diameter + 2
        if new_trunk_diameter > 99.9:
            return "Дерево широке"
        new_leaf_calc = new_height * new_trunk_diameter * 100
        print(f"Дерево виросло {new_height} метрів в висоту {new_trunk_diameter} вшир і має {new_leaf_calc} листя")  
        
    def leaf_fall(self):
        """
        Метод: опадання листя / Method: leaf fall
        
        TODO:
        - Зменшити кількість листя на 30% (помножити на 0.7)
        - Вивести повідомлення про опадання
        """
        fall = self._calculate_leaf_count()* 0.7
        print( f"Листя опало і тепер на дереві {fall} листочків")
    
    def get_info(self):
        """
        Метод: отримати інформацію про дерево / Method: get tree information
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити висоту, діаметр стовбура, кількість листя
        """
        return f"Дерево заввишки {self.__height}, {self.__trunk_diameter} см вшир і має листя {self._calculate_leaf_count()}"

class Kettle:
    """
    Клас побутового об'єкта "Чайник"
    Class for household object "Kettle"
    
    Атрибути / Attributes:
    - volume: максимальний об'єм (0.5 <= volume <= 5 літрів)
    - current_volume: поточний об'єм води (0 <= current <= volume)
    - water_temperature: температура води (за замовчуванням 20°C)
    - is_on: чи включений чайник (за замовчуванням False)
    """
    
    def __init__(self, volume):
        """
        Ініціалізація чайника / Initialize kettle
        
        Args:
            volume (float): Максимальний об'єм в літрах / Maximum volume in liters
        
        TODO:
        - Встановити volume через властивість
        - Ініціалізувати current_volume = 0
        - Ініціалізувати water_temperature = 20
        - Ініціалізувати is_on = False
        """
        self.__volume = volume   
        self.__current_volume = 0
        self.__water_temperature = 20
        self.__is_on = False
    @property
    def volume(self):
        """
        Властивість: максимальний об'єм / Property: maximum volume
        
        TODO: Повернути _volume
        """
        return self.__volume
    
    @volume.setter
    def volume(self, value):
        """
        Сетер для максимального об'єму / Setter for maximum volume
        
        TODO:
        - Перевірити що 0.5 <= value <= 5
        - Встановити _volume = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or 0.5 <= value <= 5:
            raise ValueError("Невірний об'єм чайника")
        else:
            self.__volume = value    
    
    @property
    def current_volume(self):
        """
        Властивість: поточний об'єм води / Property: current water volume
        
        TODO: Повернути _current_volume
        """
        return self.__current_volume
    
    @property
    def water_temperature(self):
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _water_temperature
        """
        return self.__water_temperature
    
    @property
    def is_on(self):
        """
        Властивість: стан чайника / Property: kettle state
        
        TODO: Повернути _is_on
        """
        return self.__is_on
    
    def pour_water(self, amount):
        """
        Метод: налити воду / Method: pour water
        
        Args:
            amount (float): Кількість води для додавання / Amount of water to add
        
        TODO:
        - Перевірити що amount >= 0
        - Обчислити скільки води можна додати (не більше ніж volume)
        - Додати воду до current_volume
        - Вивести повідомлення про додавання
        - Повідомити якщо чайник переповнений
        """
        if amount < 0:
            return "Кількість води має бути невід'ємною"
        water_to_add = min(amount, self.__volume - self.__current_volume)
        if water_to_add <= 0:
            return "Чайник вже повний!"
        self.__current_volume += water_to_add
        if water_to_add < amount:
            print(f"Додано лише {water_to_add} л води, чайник переповнений!")
        else:
            print(f"Додано {water_to_add} л води. Поточний об'єм: {self.__current_volume} л")
           
    
    def drain_water(self, amount):
        """
        Метод: злити воду / Method: drain water
        
        Args:
            amount (float): Кількість води для зливання / Amount of water to drain
        
        TODO:
        - Перевірити що amount >= 0
        - Зменшити current_volume (але не менше 0)
        - Вивести повідомлення про зливання
        """
        if amount <0:
            print('неможливо злити відємну кількість води')
            water_left = self.__current_volume - amount
        if water_left <0:
             water_left = 0
        return f"З чайника злили {amount} літрів води і залишилось в ньому {water_left}"
    def turn_on(self):
        """
        Метод: включити чайник / Method: turn on kettle
        
        TODO:
        - Перевірити що в чайнику є вода (current_volume > 0)
        - Встановити is_on = True
        - Встановити water_temperature = 100
        - Вивести повідомлення про включення
        - Якщо води немає - вивести попередження
        """
        if self.__current_volume > 0:
            self.__is_on = True
            self.__water_temperature = 100
            print (f"Чайник нагрівається {self.__is_on}і темпетратура втсановлена {self.__water_temperature}")
        else: 
            print ("Води в чайнику нема")
    def turn_off(self):
        """
        Метод: вимкнути чайник / Method: turn off kettle
        
        TODO:
        - Встановити is_on = False
        - Вивести повідомлення про вимкнення
        """
        self.__is_on = False
        print ("Чайник нагрівся і вимкнувся")
    def get_status(self):
        """
        Метод: отримати статус чайника / Method: get kettle status
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити об'єм, температуру, стан включення
        """
        return f"В чайнику зараз {self.__current_volume}літрів води, температура води: {self.__water_temperature} і він вкл:{self.__is_on}"

class Cloud:
    """
    Клас природного об'єкта "Хмара"
    Class for natural object "Cloud"
    
    Атрибути / Attributes:
    - area: площа хмари (1 <= area <= 10000 км²)
    - altitude: висота над землею (0.5 <= altitude <= 15 км)
    - humidity_density: щільність вологи (0 <= humidity <= 30 г/м³)
    - rain_probability: ймовірність дощу (обчислюється автоматично)
    """
    
    def __init__(self, area, altitude, humidity_density):
        """
        Ініціалізація хмари / Initialize cloud
        
        Args:
            area (float): Площа хмари в км² / Cloud area in km²
            altitude (float): Висота над землею в км / Altitude above ground in km
            humidity_density (float): Щільність вологи в г/м³ / Humidity density in g/m³
        
        TODO:
        - Встановити всі атрибути через властивості
        - Обчислити початкову ймовірність дощу
        """
        self.__area = area
        self.__humidity_density = humidity_density
        self.__altitude = altitude
    
    @property
    def area(self):
        """
        Властивість: площа хмари / Property: cloud area
        
        TODO: Повернути _area
        """
        return self.__area
    
    @area.setter
    def area(self, value):
        """
        Сетер для площі хмари / Setter for cloud area
        
        TODO:
        - Перевірити що 1 <= value <= 10000
        - Встановити _area = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(float)) or 10000 <= value <= 1:
            raise ValueError("Невірне значення площі хмари")
        else:
            self.__area = value    
    
    @property
    def altitude(self):
        """
        Властивість: висота / Property: altitude
        
        TODO: Повернути _altitude
        """
        return self.__altitude
    
    @altitude.setter
    def altitude(self, value):
        """
        Сетер для висоти / Setter for altitude
        
        TODO:
        - Перевірити що 0.5 <= value <= 15
        - Встановити _altitude = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(float)) or 15 <= value <= 0.5:
            raise ValueError("Невірне значення висоти хмари")
        else:
            self.__altitude = value    
    
    @property
    def humidity_density(self):
        """
        Властивість: щільність вологи / Property: humidity density
        
        TODO: Повернути _humidity_density
        """
        return self.__humidity_density
    
    @humidity_density.setter
    def humidity_density(self, value):
        """
        Сетер для щільності вологи / Setter for humidity density
        
        TODO:
        - Перевірити що 0 <= value <= 30
        - Встановити _humidity_density = value
        - Перерахувати ймовірність дощу
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(float)) or 30 <= value <= 0:
            raise ValueError("Неправильне значення ймвірності дощу")
        else:
           self.__humidity_density = value    
    
    @property
    def rain_probability(self):
        """
        Властивість: ймовірність дощу (тільки читання) / Property: rain probability (read-only)
        
        TODO: Повернути _rain_probability
        """
        return self.__rain_probability
    
    
    def _calculate_rain_probability(self):
        """
        Приватний метод: обчислення ймовірності дощу / Private method: calculate rain probability
        
        Формула: min(humidity_density * 3, 100)
        
        TODO:
        - Обчислити ймовірність за формулою
        - Повернути результат
        """
        self.__rain_probability = min(self.__humidity_density * 3, 100)
        return self.__rain_probability
    def accumulate_moisture(self, amount):
        """
        Метод: накопичити вологу / Method: accumulate moisture
        
        Args:
            amount (float): Кількість вологи для додавання / Amount of moisture to add
        
        TODO:
        - Перевірити що amount >= 0
        - Збільшити humidity_density на amount (але не більше 30)
        - Використати властивість для автоматичного перерахунку ймовірності
        - Вивести повідомлення про накопичення
        """
        if not isinstance(amount,(int)) or 0 >= amount >=30:
             raise ValueError ("Невірне значення: занадто волого")
        else:
           new_humidity = self.__humidity_density + amount
        print(f"Вологість збільшилась на {amount} % і тепер складає {new_humidity} %")
        
        
    def rain(self):
        """
        Метод: дощ / Method: rain
        
        TODO:
        - Перевірити чи rain_probability > 70
        - Якщо так: зменшити humidity_density на 50% і вивести повідомлення про дощ
        - Якщо ні: вивести повідомлення що дощу немає з поточною ймовірністю
        - Повернути True якщо йде дощ, False якщо ні
        """
        is_rain = True
        if self._calculate_rain_probability() > 70:
            self.__humidity_density/2
            is_rain = True
            print (f"Ймовірність дощу {self._calculate_rain_probability()} %, дощ йде: {is_rain}")
        else:
            is_rain = False
            print (f"Ймовірність дощу: {self._calculate_rain_probability()} %, дощ йде: {is_rain}")
        
            
    def move(self, new_altitude):
        """
        Метод: рух хмари / Method: cloud movement
        
        Args:
            new_altitude (float): Нова висота / New altitude
        
        TODO:
        - Встановити нову висоту через властивість
        - Вивести повідомлення про переміщення
        """
        self.__altitude = new_altitude
        print(f"Нова висота хмари тепер: {new_altitude}")
    
    def get_forecast(self):
        """
        Метод: отримати прогноз / Method: get forecast
        
        TODO:
        - Повернути форматований рядок з усією інформацією
        - Включити площу, висоту, щільність вологи, ймовірність дощу
        """
        return f"Площа хмари: {self.__area} метрів, висота:{self.__altitude}, вологість: {self.__humidity_density} і ймовірність дощу: {self._calculate_rain_probability()}%"

    
class Aquarium:
    """
    Клас побутового об'єкта "Акваріум"
    Class for household object "Aquarium"
    
    Атрибути / Attributes:
    - length, width, height: розміри (10 < розмір < 200 см)
    - water_level: рівень води (0 <= water_level <= height)
    - fish_count: кількість риб (максимум 1 риба на 5 літрів води)
    - temperature: температура води (18 <= temperature <= 30 °C)
    - water_volume: об'єм води (обчислюється автоматично)
    """
    
    def __init__(self, length, width, height, water_level=0, fish_count=0, temperature=24):
        """
        Ініціалізація акваріума / Initialize aquarium
        
        Args:
            length (float): Довжина в см / Length in cm
            width (float): Ширина в см / Width in cm
            height (float): Висота в см / Height in cm
            water_level (float): Рівень води в см / Water level in cm
            fish_count (int): Кількість риб / Fish count
            temperature (float): Температура води в °C / Water temperature in °C
        
        TODO:
        - Встановити всі атрибути через властивості для валідації
        - Порядок важливий: спочатку розміри, потім water_level, потім fish_count
        """
        self.__length = length
        self.__width = width
        self.__height = height
        self.__water_level = water_level
        self.__fish_count = fish_count
        self.__temperature = temperature
    
    
    @property
    def length(self):
        """
        Властивість: довжина / Property: length
        
        TODO: Повернути _length
        """
        return self.__length
    
    @length.setter
    def length(self, value):
        """
        Сетер для довжини / Setter for length
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _length = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or 200 < value < 10:
            raise ValueError ("Непраивлне значення довжини") 
        else:
            self.__length = value
    
    @property
    def width(self):
        """
        Властивість: ширина / Property: width
        
        TODO: Повернути _width
        """
        return self.__width
    
    @width.setter
    def width(self, value):
        """
        Сетер для ширини / Setter for width
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _width = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or 200 < value < 10:
            raise ValueError ("Непраивлне значення довжини") 
        else:
            self.__width = value
    
    @property
    def height(self):
        """
        Властивість: висота / Property: height
        
        TODO: Повернути _height
        """
        return self.__height
    
    @height.setter
    def height(self, value):
        """
        Сетер для висоти / Setter for height
        
        TODO:
        - Перевірити що 10 < value < 200
        - Встановити _height = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or 200 < value < 10:
            raise ValueError ("Непраивлне значення довжини") 
        else:
            self.__height = value
        #return self._height
    @property
    def water_level(self):
        """
        Властивість: рівень води / Property: water level
        
        TODO: Повернути _water_level
        """
        return self.__water_level
    
    @water_level.setter
    def water_level(self, value):
        """
        Сетер для рівня води / Setter for water level
        
        TODO:
        - Перевірити що 0 <= value <= height
        - Встановити _water_level = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or self.__height() <= value <= 0:
            raise ValueError ("Непраивлне значення для рівня води") 
        else:
            self.__water_level = value
        return f"Рівень води в акваріумі {self.__water_level}"
    @property
    def fish_count(self):
        """
        Властивість: кількість риб / Property: fish count
        
        TODO: Повернути _fish_count
        """
        #fish_count = self._fish_count
        return self.__fish_count
    
    @fish_count.setter
    def fish_count(self, value):
        """
        Сетер для кількості риб / Setter for fish count
        
        TODO:
        - Перевірити що value >= 0
        - Обчислити максимальну кількість риб (water_volume / 5)
        - Перевірити що value не перевищує максимум
        - Встановити _fish_count = value
        - Викинути ValueError при неправильному значенні
        """
        max_number = self.__water_level / 5
        if not isinstance(value,(int)) or  0 >=  value > max_number:
            raise ValueError ("Непраивлне значення кількості риб") 
        else:
            self.__fish_count = value
        return f"В акваріумі зараз {self.__fish_count()} риб"
    
    @property
    def temperature(self):
        """
        Властивість: температура води / Property: water temperature
        
        TODO: Повернути _temperature
        """
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        """
        Сетер для температури / Setter for temperature
        
        TODO:
        - Перевірити що 18 <= value <= 30
        - Встановити _temperature = value
        - Викинути ValueError при неправильному значенні
        """
        if not isinstance(value,(int,float)) or  18 >=  value >= 30:
            raise ValueError ("Неправильне значення температури") 
        else:
            self.__temperature = value
           
    
    @property
    def water_volume(self):
        """
        Властивість: об'єм води в літрах (тільки читання) / Property: water volume in liters (read-only)
        
        Формула: (length * width * water_level) / 1000
        
        TODO: Обчислити та повернути об'єм води
        """
        water_volume = (self.__length * self.__width * self.__water_level) / 1000
        return water_volume
           
    
    def add_water(self, level_increase:float):
        """
        Метод: додати воду / Method: add water
        
        Args:
            level_increase (float): Збільшення рівня в см / Level increase in cm
        
        TODO:
        - Перевірити що level_increase >= 0
        - Обчислити новий рівень (не більше height)
        - Встановити новий рівень через властивість
        - Перевірити чи кількість риб все ще допустима
        - Вивести повідомлення про додавання води
        """
        if 0<= level_increase < self.__height :
            self.__water_level += level_increase
            print(f"Додано води {level_increase} і поточний рівень: {self.__water_level} ")
        elif level_increase < 0:
            print ("Замало води")
        else: 
            print ("Невідома помилка")
        if self.__water_level / 5 < 0:
            print ("Води все ще замало")
        #return f"До акваріума додали води і тепер рівень води: {self._water_level}"        
    
    def add_fish(self):
        """
        Метод: додати рибу / Method: add fish
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Перевірити чи можна додати ще одну рибу
        - Якщо можна: збільшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба додана, False якщо ні
        """
        is_added = True
        max_number = self.__water_level // 5
        if max_number > 0:
            while self.__fish_count < max_number :   
                self.__fish_count += 1 
            print(f"Рибу додано: {is_added},  кількість для додавання {self.__fish_count}")
            return True 
        else:
            print (f"Рибу не додано ")
            return False
            
            
    
    def remove_fish(self):
        """
        Метод: забрати рибу / Method: remove fish
        
        TODO:
        - Перевірити чи є риби в акваріумі
        - Якщо є: зменшити fish_count на 1
        - Вивести повідомлення про результат операції
        - Повернути True якщо риба забрана, False якщо риб немає
        """
        if self.__fish_count >0:
            self.__fish_count -=1 
            print(f"Забрано рибу і залишилось {self.__fish_count}")   
        else:
            print(f"неможливо забрати рибу її там нема")
        
    
    def heat(self, new_temperature: float):
        """
        Метод: нагріти воду / Method: heat water
        
        Args:
            new_temperature (float): Нова температура / New temperature
        
        TODO:
        - Встановити нову температуру через властивість
        - Вивести повідомлення про зміну температури
        """
        self.__temperature = new_temperature
        print (f"Температура води була змінeна. Поточна становить {self.__temperature}")
        return self.__temperature
         
    def inspect(self):
        """
        Метод: огляд акваріума / Method: aquarium inspection
        
        TODO:
        - Обчислити максимальну кількість риб для поточного об'єму
        - Повернути форматований рядок з усією інформацією
        - Включити розміри, рівень води, об'єм, кількість риб, температуру
        """
        max_fish = self.__water_level // 5
        print (f"Акваріум має {self.__water_level} рівень води,висоту {self.__height} см, довжину {self.__width}см, ширину {self.__length}см, максимальну кількість риб: {max_fish}, температуру {self.__temperature}")


    
    
# Область для тестування / Testing area
if __name__ == "__main__":
    print("=== ТЕСТУВАННЯ ШАБЛОНІВ КЛАСІВ / TESTING CLASS TEMPLATES ===\n")
    
    # TODO: Розкоментуйте код нижче після реалізації класів
    # Uncomment code below after implementing classes
    
   
    # Тестування дерева / Testing tree
    print("1. ТЕСТУВАННЯ ДЕРЕВА / TESTING TREE")
    try:
        tree = Tree(10, 50)
        print(tree.get_info())
        tree.grow()
        tree.leaf_fall()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування чайника / Testing kettle
    print("2. ТЕСТУВАННЯ ЧАЙНИКА / TESTING KETTLE")
    try:
        kettle = Kettle(2.0)
        kettle.pour_water(1.5)
        print(kettle.get_status())
        kettle.turn_on()
        kettle.turn_off()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування хмари / Testing cloud
    print("3. ТЕСТУВАННЯ ХМАРИ / TESTING CLOUD")
    try:
        cloud = Cloud(100, 2.5, 15)
        print(cloud.get_forecast())
        cloud.accumulate_moisture(10)
        cloud.rain()
    except Exception as e:
        print(f"Помилка: {e}")
    print()
    
    # Тестування акваріума / Testing aquarium
    print("4. ТЕСТУВАННЯ АКВАРІУМА / TESTING AQUARIUM")
    try:
        aquarium = Aquarium(50, 30, 40)
        aquarium.add_water(35)
        aquarium.add_fish()      #додала максимальну кількість
        aquarium.remove_fish()   # забрала тільки 1 штуку
        aquarium.heat(26)
        print(aquarium.inspect())
    except Exception as e:
        print(f"Помилка: {e}")
   
    
    print("Реалізуйте методи класів та розкоментуйте код для тестування!")
    print("Implement class methods and uncomment code for testing!")