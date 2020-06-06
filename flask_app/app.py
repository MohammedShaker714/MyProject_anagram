import csv
from flask import Flask, request, render_template

server = Flask(__name__)


def load_dictionary_words():
    with open('dictionary.txt', newline='\n') as f:
        reader = csv.reader(f)
        dictionary_words = []
        for row in reader:
            dictionary_words.append(row[0])
        return dictionary_words


def get_anagrams_dict(dictionary_words):
    anagrams_dict = {}
    for word in dictionary_words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in anagrams_dict:
            anagrams_dict[sorted_word] = [word]
        else:
            anagrams_dict[sorted_word].append(word)
    return anagrams_dict


def get_anagrams(anagrams_dict, word):
    sorted_word = "".join(sorted(word))
    anagrams = []
    if sorted_word in anagrams_dict:
        anagrams = [element for element in anagrams_dict[sorted_word] if element != word]
    if anagrams == []:
        return 'NOTHING WAS FOUND'
    else:
        return str(anagrams)


@server.route('/')
def anagrams():
    input_word = request.args.get('input_word')
    if input_word != None:
        anagrams = get_anagrams(anagrams_dict, input_word.lower())
        return render_template('anagrams_page.html', anagrams=anagrams, word=input_word)
    else:
        return render_template('anagrams_page.html', anagrams=None, word=None)


dictionary_words = load_dictionary_words()
anagrams_dict = get_anagrams_dict(dictionary_words)
