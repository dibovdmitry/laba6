#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Ввод списка.
    a = list(map(int, input().split()))
    # Если список окажется пустым программа завершится.
    if not a:
        print("Заданный список пуст", file=sys.stderr)
        exit(1)

    # Определяет индексы минимального и максимального элементов.
    a_min = a_max = a[0]
    i_min = i_max = 0
    for i, item in enumerate(a):
        if item < a_min:
            i_min, a_min = i, item
        if item >= a_max:
            i_max, a_max = i, item

    # Проверяет индексы и меняет их местами.
    if i_min > i_max:
        i_min, i_max = i_max, i_min

    # Считает количество положительных элементов.
    count = 0
    for item in a[i_min+1:i_max]:
        if item > 0:
            count += 1
    print(count)
