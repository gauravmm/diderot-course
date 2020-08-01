import itertools
import random


def rotate_list_grade(grade, rotate_list):
    grade.equal(rotate_list([1, 2, 3, 4], 1), [2, 3, 4, 1])
    grade.equal(rotate_list([1, 2, 3, 4], 3), [4, 1, 2, 3])
    grade.equal(rotate_list([1, 2, 3, 4, 5], 3), [4, 5, 1, 2, 3])
    grade.equal(rotate_list([1], 1), [1])
    grade.equal(rotate_list([], 0), [], score=2)
