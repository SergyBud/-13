sum_of_tickets = int(input("Введите количество билетов: "))
summary = 0
for guest in range(1, sum_of_tickets+1):
    age = int(input(f"Ввестите возраст посетителя #{guest}: "))
    if age < 18:
        summary += 0
    elif 18 <= age < 25:
        summary += 9905
    elif 25 <= age:
        summary += 1390
if sum_of_tickets > 3:
    print(float(summary) * 0.9)
else:
    print(summary)