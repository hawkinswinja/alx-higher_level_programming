#!/usr/bin/python3
""" 101-lazy_matrix_mul module
    multiplies two matrices using numpy module
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """function to multiply two matrices
       @args:
           m_a(list)
           m_b(list)
    """
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    for listi in m_a:
        if type(listi) is not list:
            raise TypeError("m_a must be a list of lists")
        if len(listi) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")
        for i in listi:
            if type(i) not in [int, float]:
                raise TypeError("m_a should contain only integers or floats")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    for listi in m_b:
        if type(listi) is not list:
            raise TypeError("m_b must be a list of lists")
        if len(listi) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")
        for i in listi:
            if type(i) not in [int, float]:
                raise TypeError("m_b should contain only integers or floats")
    m_c = [list(i) for i in zip(*m_b)]
    if len(m_a[0]) != len(m_c[0]):
        raise ValueError("m_a and m_b can't be multiplied")
    m_ab = np.matmul(m_a, m_b)
    return m_ab
