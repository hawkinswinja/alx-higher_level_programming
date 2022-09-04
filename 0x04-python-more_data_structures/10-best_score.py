#!/usr/bin/python3
def best_score(a_dictionary):
    if len(a_dictionary) < 1 or a_dictionary is None:
        return None
    a = sorted(a_dictionary.items(), key=lambda x: x[1])
    return (a[-1][0])
