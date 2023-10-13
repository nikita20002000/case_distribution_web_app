max_workers = 599
distant_workers = 599 * 15 / 100

places_array = [46, 70, 15, 112, 99, 75, 68, 28, 99, 448, 62, 83, 166, 378]

final_list = []
i = 0

for place in places_array:
    counter = 0
    coef = 0
    i = 0
    while round(i, 1) >= 3.6 or i ==0 and max_workers != 0:
        counter += 1
        max_workers -= 1
        i = place / counter

    print(round(i, 1))
    final_list.append(f'{counter} - {place}')


print(final_list)
print(max_workers)



