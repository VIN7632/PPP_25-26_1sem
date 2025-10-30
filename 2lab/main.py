text = input("Введите строку: ")

if not text.isalpha():
    print("Ошибка: строка должна содержать только буквы латинского алфавита.")
else:
    lower_count = {}
    upper_count = {}

    for ch in text:
        low = ch.lower()
        if low not in lower_count:
            lower_count[low] = 0
            upper_count[low] = 0
        if ch.islower():
            lower_count[low] += 1
        else:
            upper_count[low] += 1

    result = ""
    for ch in text:
        low = ch.lower()
        if lower_count[low] <= upper_count[low]:
            result += ch

    print("Результат:", result)
