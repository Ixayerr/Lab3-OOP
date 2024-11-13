from Proc24 import input_and_process
from Matrix2 import matrix_task


def main():
    while True:
        print("Оберіть завдання для виконання:")
        print("1 - Завдання1 (Proc)")
        print("2 - Завдання 2 (Matrix)")
        print("0 - Вихід")
        choice = input("Ваш вибір: ")

        if choice == "1":
            input_and_process()
        elif choice == "2":
            matrix_task()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == "__main__":
    main()
