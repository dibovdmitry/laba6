#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys
if __name__ == '__main__':
    A = list(map(int, input("Список : ").split()))
    s = 0
    d = max(A)
    print(f" Максимальное число из списка: {d}")
    print(f" Его индекс: {A.index(max(A))}")
for i in A:
    if i > 0:
        print(f" Сумма элемнтов массива, расположенных после первого положительного элемента {sum(A[A.index(i):])}")
        break
