# -*- coding: utf-8 -*-
"""
Created on Sun Jul 24 11:24:47 2022

@author: dfu
"""

import sys, random, json

symbol_list = ['~','!','@','#','$','%','^','&','*','.',':',';']
word_list = []
words = []

def setup() :
    global word_list
    with open("words_dictionary.json") as file:
        json_file = json.load(file)
    word_list = json_file.keys()

def generate(w, c, n, s) :
    global words
    words = random.sample(word_list, w)
    words = capitalize(c)
    words = numbers(n)
    words = symbols(s)
    return ''.join(words)

def capitalize(c) :
    cap_index = random.sample(range(len(words)), c)
    for i in cap_index:
        words[i] = words[i].capitalize()
    return words

def numbers(n) :
    spaces = random.sample(range(len(words)),n)
    for space in spaces:
        words.insert(space, str(random.randint(0,9)))
    return words

def symbols(s) :
    spaces = random.sample(range(len(words)),s)
    for space in spaces:
        words.insert(space, random.choice(symbol_list))
    return words

def get_command_line_args(args) :
    h = False
    w = 4
    c = 0
    n = 0
    s = 0
    for i in range(len(args)):
        arg = args[i]
        if (arg == '-h' or arg == '-help'):
            h = True
        elif (arg == '-w' or arg == '-words'):
            w = int(args[i+1])
        elif (arg == '-c' or arg == '-caps'):
            c = int(args[i+1])
        elif (arg == '-n' or arg == '-numbers'):
            n = int(args[i+1])
        elif (arg == '-s' or arg == '-symbols'):
            s = int(args[i+1])
    return h, w, c, n, s

def main() :
    h,w,c,n,s = get_command_line_args(sys.argv)
    if (h):
        print("help menu")
    else:
        try:
            setup()
            print(generate(w, c, n, s))
        except:
            print("An exception occurred")
    
main()