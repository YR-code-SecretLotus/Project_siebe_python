from Person import Person

def create_person():
    print("******************************")
    print("***** Character Creation *****")
    print("******************************")
    name = input("Enter your character's name: ")
    age = int(input("Enter your character's age: "))
    gender = input("Enter your character's gender (m/f/o): ")
    height = float(input("Enter your character's height (metres): "))
    mass = float(input("Enter your character's mass (kg): "))
    occupation = input("Enter your character's occupation: ")
    favourite_food = input("Enter your character's favourite food: ")

    # Maak een Person-object aan met de opgegeven gegevens
    person = Person(name, age, gender, height, mass, occupation, favourite_food)
    return person

def main():
    while True:
        # Hoofdmenu
        print("\n******************************")
        print("*****      The Simz      *****")
        print("******************************")
        print("******************************")
        print("*1. Create a character       *")
        print("*2. Exit                     *")
        print("******************************")

        option = input("Enter an option (1-2): ")

        if option == '1':
            my_person = create_person()
            print("\nHello, my name is {}. I'm a {}-year-old {} and I'm {}.".format(
                my_person.name, my_person.age, my_person.gender, my_person.bmi()))
            print(f"My favourite food is {my_person.favourite_food}, and I work as a {my_person.occupation}.")
        elif option == '2':
            print("\nExiting the application... Goodbye!")
            break
        else:
            print("\nInvalid option! Please choose 1 or 2.")

if __name__ == "__main__":
    main()

