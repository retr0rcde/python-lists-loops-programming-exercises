import random

def generate_random_list():
    aux_list = []
    randomlength = random.randint(1, 100)  # Tamaño aleatorio para la lista

    for i in range(randomlength):
        aux_list.append(random.randint(1, 100))  # Agregar un número aleatorio entre 1 y 100
    return aux_list

my_stupid_list = generate_random_list()

# Obtener el último elemento de la lista
the_last_one = my_stupid_list[-1]
print(the_last_one)

