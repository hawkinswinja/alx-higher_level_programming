#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    for index in dir(hidden_4):
        if index[0] == "_":
            continue
        print(index)
