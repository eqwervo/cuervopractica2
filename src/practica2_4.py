user_name = input('Ingrese un nombre de usuario: ')


mayus = any(letter.isupper() for letter in user_name)


number = any(letter.isnumeric() for letter in user_name)

    
    
if len(user_name) > 5:
    if user_name.isalnum():
        if mayus:
            if number:
                print('La contraseña es segura')
            else:
                print('La contraseña debe contener al menos un número')
        else:
            print('La contraseña debe contener al menos una mayúscula')
    else:
        print('La contraseña debe contener solo letras y números')
else:
    print('La contraseña debe tener al menos 5 digitos')    