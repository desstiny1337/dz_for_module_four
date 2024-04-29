path = 'salary.txt'


with open('salary.txt', "w") as file:
    file.write("Alex Korp,3000\n"
        'Nikita Borisenko, 2000\n'
        'Sitarama Raju, 1000\n'
    )

def total_salary(path):
    total = 0
    count = 0

    with open(path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 2:
                name, salary_string = parts
                try:
                    salary = int(salary_string.strip())
                    total += salary
                    count += 1
                except ValueError:
                    print(f'Invalid salary value: {salary_string}')

    if count > 0:
        avg_salary = int(total/count)
    else:
        avg_salary = 0

    return (total, avg_salary)

result = total_salary(path)
print(f"Загальна сума заробітної плати: {result[0]}, Середня заробітна плата: {result[1]}")

if __name__ == '__main__':
    print('completed with main')