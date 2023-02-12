def get_full_name(first_name: str, last_name: str):
    full_name = first_name.title() + ' ' + last_name.title()
    return full_name


print(get_full_name('Jhon', 'Ortiz'))  #Jhon Ortiz
#print(get_full_name('Jhon', 0))  #Attributeerror (la funcion title() necesita un parametro de tipo str)



