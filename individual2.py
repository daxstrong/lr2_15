#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open('text_ind2.txt', 'r', encoding='utf-8') as fileptr:
        content = fileptr.read()

    words = content.split()
    max_length = max(len(word) for word in words)
    longest_words = [word for word in words if len(word) == max_length]

    print("Длина самого длинного слова:", max_length)
    print("Самые длинные слова:", longest_words)
