from random import choice
import random
from datetime import date
import os
import json

horoscope = {}
signs = ["Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева","Весы","Скорпион", "Стрелец", "Козерог", "Водолей", "Рыбы"]

# main function: returns todays horoskop for the sign
def get_text_from_horoscope(sign):

    d = date.today()
    if sign not in signs:
        return TypeError;

    if (d, sign) not in horoscope:
        horoscope[(d, sign)] = gen_horoscope()

    data = {}
    data['sign'] = sign
    data['date'] = (d.day, d.year)
    data['text'] = horoscope[(d, sign)]

    json_data = json.dumps(data)

    return json_data

# prapares markov_chain for text.txt in static/text.txt
def prepare_horoscope():

    script_dir = os.path.dirname(__file__)
    rel_path = "static/text.txt"
    abs_file_path = os.path.join(script_dir, rel_path)

    with open(abs_file_path, encoding='utf-8') as f:
        global words
        words = []
        words = f.read().split()
    markov_chain = {}
    for i in range(0, len(words) - 2):
        key = (words[i], words[i+1])
        markov_chain.setdefault(key, [])
        markov_chain[key].append(words[i+2])
    return markov_chain

#gererates random text from markov chain (prepared by prepare_horoscope) of size 25
def gen_horoscope():
    stopsentence = (".", "!", "?",)
    markov_chain = prepare_horoscope()
    size = 25
    gen_words = []
    seed = random.randint(0, len(words) - 3)
    w1 = words[seed]
    while (w1.isupper()  or w1.islower()):
        seed = random.randint(0, len(words) - 3)
        w1 = words[seed]
    w2 = words[seed+1]

    for i in range(0, size-1):
        gen_words.append(w1)
        try:
            w3 = choice(markov_chain[(w1,w2)])
        except KeyError:
            break
        w1, w2 = w2, w3

    while True:
        gen_words.append(w1)
        if w1[-1] in stopsentence:
             break
        try:
            w3 = choice(markov_chain[(w1,w2)])
        except KeyError:
            break
        w1, w2 = w2, w3
    result = ' '.join(gen_words)
    return result


