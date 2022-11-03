raw = input('Введите последовательность чисел через пробел: ')
int_array = [int(i) for i in raw.split(' ') if i.isdigit()]
print(max(int_array))
