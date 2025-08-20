#!/usr/bin/env python3

def return_evens(num_list):
    # list = range(0,8)
    return  [n for n in num_list if n % 2 == 0]
    
    pass

def make_exclamation(sentence_list):
    return [sentence_list + "!" for sentence_list in sentence_list]
    pass