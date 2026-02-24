from utils import fibonacci, is_pow_of_five, is_prime

def main():
    number = input("Введіть число:")
    result = fibonacci(number)
    result1 = is_prime(number)
    print(f"{number}-те число Фібоначчі дорівнює {result}")
    if is_prime(number):
        print(f"{number} є простим")
    else:
        print(f"{number} НЕ є простим.")
    if is_pow_of_five(number):
        print(f"Число {number} є степенем 5!")
    else:
        print(f"Число {number} НЕ є степенем 5.")

if name == "__main__":
    main()

