import random

# Список популярных матерных слов (можно расширить)
obscene_words = [
    "блять", "пизда", "хуй", "ебать", "нахуй", "пиздец", "еблан", "сука",
    "хуесос", "заебал", "охуел", "пидор", "ебаный", "блядь", "отъебись",
    "заебись", "пиздеть", "охуеть", "впизду"
]

# Шаблоны фраз
phrases = [
    "Да {word}!",
    "{word} твою мать!",
    "Пошёл {word}!",
    "Это полный {word}",
    "{word}, как так-то?",
    "Ну ты и {word}",
    "Что за {word}?",
    "Иди {word}",
    "Это {word} круто!",
    "{word} в рот"
]

def generate_mat():
    phrase = random.choice(phrases)
    word = random.choice(obscene_words)
    return phrase.format(word=word)

print(generate_mat())
