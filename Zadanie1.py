#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    A = list(map(int, input("Оценки по алгебре : ").split()))
    G = list(map(int, input("Оценки по геометрии : ").split()))
    F = list(map(int, input("Оценки по физике : ").split()))
    SA = sum(A) / len(A)
    SG = sum(G) / len(G)
    SF = sum(F) / len(F)
    if SA > SG and SF < SA:
        print(f'Самая высокая успеваемость по алгебре')
    elif SG > SA and SF < SG:
        print(f'Самая высокая успеваемость по геометрии')
    elif SF > SA and SG < SF:
        print(f'Самая высокая успеваемость по физике')
