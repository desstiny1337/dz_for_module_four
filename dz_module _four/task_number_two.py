with open('cats.txt', 'w') as file:
    file.write('60b90c1c13067a15887e1ae1,Tayson,3\n'
    '60b90c2413067a15887e1ae2,Vika,1\n'
    '60b90c2e13067a15887e1ae3,Barsik,2\n'
    '60b90c3b13067a15887e1ae4,Simon,12\n'
    '60b90c4613067a15887e1ae5,Tessi,5\n') #CREATE A FILE

path = 'cats.txt' #PATH TO OUR CTREATED FILE


def get_cats_info(path): #creating a func
    cats_list = [] #the main list which i am goiong to work up on
    try: #try/except bacause i need to prevent the errors
        with open(path, 'r', encoding='utf-8') as file: #opening this way because i have a b codes
            lines = file.readlines() #reading lines

            for line in lines: #cycle for each line of information
                parts = line.strip().split(',') #strip to delete all of spaces and split to be splitted by comma
                if len(parts) == 3: #after splitiing i have three options which are b-code, name and age(str maaybe or float i dont know but not a int)
                    cat_id, name, age = parts #names of mine parts of info anout cats

                    try: #here i use try except to prevent following errors: Value erroe cause it might be a string or else
                        age = int(age) #tranforming other type to integer
                    except ValueError: #excepting valuseerror
                        print(f'Invalid age: {age}') #consequence of invalid agw

                    cat_info = {       #creating a dictionary with 'key' : value
                        'cat_id': cat_id,
                        'name': name,
                        'age': age
                    }
                    cats_list.append(cat_info) #updating list with cat info i got from the try/except
                else:
                    print(f'Invalid') #obviously
    except FileNotFoundError: #obviously
        print(f'File not found {path}') #obviously
    except Exception as e: #printing other errors
        print(f'Error {e}')
    return cats_list #returning cats updated list

cats_info = get_cats_info(path) #that variable asks func and saves all job which func done in itself

for cat in cats_info: #cycle for each cat
    print(f"Cat ID: {cat['cat_id']}, Name: {cat['name']}, Age: {cat['age']}")

if __name__ == '__main__': #obviously
    print('Meow')


