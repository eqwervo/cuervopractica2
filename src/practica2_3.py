rules = """Respeta a los demás. No se permiten insultos ni lenguaje ofensivo. Evita el spam. No publiques enlaces sospechosos o repetitivos. No compartas información personal. Usa los canales adecuados para cada tema. Sigue las instrucciones de los moderadores."""

def solution():
    rules_list = rules.split('. ')
    print(rules_list)
    word = input('Ingrese una palabra: ')

    for sentence in rules_list:
        if word in sentence:
            print(sentence)
