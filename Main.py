print("Алгорит Эратосфена\n")
count = int(input("Введите натуральное число: "))
array = []
array.append(2)
for i in range(3, count):
    simple = True
    for j in range(len(array)):
        if (i % array[j] == 0):
            simple = False
            break
    if (simple):
        array.append(i)
print(array)