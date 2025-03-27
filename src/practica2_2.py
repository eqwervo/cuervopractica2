titles = [
"Speedrun de Super Mario en tiempo récord",
"Charla sobre desarrollo de videojuegos",
"Jugando al nuevo FPS del momento con amigos",
"Música en vivo: improvisaciones al piano"
]
def solution():
    long_sentence = str
    count_max = 0
    for sentence in titles:
        count = 0
        for words in sentence.split():
            count += 1
        if count > count_max:
            count_max = count
            long_sentence = sentence
    print(f'El título mas largo es: {long_sentence}')