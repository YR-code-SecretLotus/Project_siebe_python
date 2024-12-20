class Person:
    def __init__(self, name, age, gender, height, mass, occupation, favourite_food):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.mass = mass
        self.occupation = occupation
        self.favourite_food = favourite_food

    def bmi(self):
        # Berekening van de BMI (Body Mass Index)
        bmi_value = self.mass / (self.height ** 2)
        if bmi_value < 18.5:
            return "underweight"
        elif 18.5 <= bmi_value < 24.9:
            return "normal weight"
        elif 25 <= bmi_value < 29.9:
            return "overweight"
        else:
            return "obese"

    def walk(self):
        return f"{self.name} is going on a relaxing walk."

    def eat(self, food):
        if food.lower() == self.favourite_food.lower():
            return f"{self.name} is eating {food} and is loving it! Yum yum!"
        else:
            return f"{self.name} is eating {food}."

    def sleep(self):
        return f"{self.name} is sleeping... Zzz..."

    def work(self):
        return f"{self.name} is going to work as a {self.occupation}."

    def introduce(self):
        bmi_category = self.bmi()
        return (f"Hello, my name is {self.name}. I’m a {self.age}-year-old {self.gender} "
                f"and I’m {bmi_category}. My favourite food is {self.favourite_food}, "
                f"and I work as a {self.occupation}.")
