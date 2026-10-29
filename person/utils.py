from person.data import my_dic

def get_full_name(name,surname):
    return f"{name} {surname}"

def print_person():
    name = my_dic['name']
    surname = my_dic['surname']
    
    full_name = get_full_name(name, surname)

    print (full_name)