def Odd(K):
    "Перевіряє, чи є ціле число K непарним"
    return K % 2 != 0


def count_odd_numbers(numbers):
    "Підраховує кількість непарних чисел у списку"
    count = 0
    for num in numbers:
        if Odd(num):
            count += 1
    return count


def input_and_process():
    "Вводить п'ять чисел, знаходить кількість непарних чисел"
    numbers = []
    for _ in range(5):
        num = int(input("Введіть число: "))
        numbers.append(num)
    odd_count = count_odd_numbers(numbers)
    print(f"Кількість непарних чисел: {odd_count}")
