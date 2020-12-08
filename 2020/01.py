from math import prod
from itertools import combinations
def part1(data):
    int_lines = [int(i) for i in data.rstrip().split('\n')]
    for c in combinations(int_lines,2):
        if sum(c)==2020:
            return prod(c)

def part2(data):
    int_lines = [int(i) for i in data.rstrip().split('\n')]
    for c in combinations(int_lines,3):
        if sum(c)==2020:
            return prod(c)