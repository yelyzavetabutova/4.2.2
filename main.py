from utils import fibonacci, is_power_of_five

def main():
    number = input("Введіть число:")
    result = fibonacci(number)     
    print(f"{number}-те число Фібоначчі дорівнює {result}")
    if is_power_of_five(number):
        print(f"Число {number} є степенем 5!")
    else:
        print(f"Число {number} НЕ є степенем 5.")

if name == "__main__":
    main()
