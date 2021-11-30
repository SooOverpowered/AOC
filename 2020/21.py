import re


def part1(data):
    lines = data.rstrip().split('\n')
    allergens_dict = {}
    food_set = set()
    food_list=[]
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        foods = ingredients.split(' ')
        food_set = food_set.union(set(foods))
        food_list.extend(foods)
        allergens=allergens[:-1].split(', ')
        for allergen in allergens:
            if allergen not in allergens_dict:
                allergens_dict[allergen]=set(foods)
            else:
                allergens_dict[allergen].intersection_update(set(foods))
    while sum([len(c) for c in allergens_dict.values()]) != len(allergens_dict):
        single_val_sets = [s for s in allergens_dict.values() if len(s) == 1]
        for s in single_val_sets:
            val = list(s)[0]
            for candidates in allergens_dict.values():
                if val in candidates and len(candidates) != 1:
                    candidates.remove(val)
    safe_foods = set.union(*allergens_dict.values()) ^ food_set
    count = sum([food_list.count(food) for food in safe_foods])
    return count


def part2(data):
    lines = data.rstrip().split('\n')
    allergens_dict = {}
    food_set = set()
    food_list=[]
    for line in lines:
        ingredients, allergens = line.split(' (contains ')
        foods = ingredients.split(' ')
        food_set = food_set.union(set(foods))
        food_list.extend(foods)
        allergens=allergens[:-1].split(', ')
        for allergen in allergens:
            if allergen not in allergens_dict:
                allergens_dict[allergen]=set(foods)
            else:
                allergens_dict[allergen].intersection_update(set(foods))
    while sum([len(c) for c in allergens_dict.values()]) != len(allergens_dict):
        single_val_sets = [s for s in allergens_dict.values() if len(s) == 1]
        for s in single_val_sets:
            val = list(s)[0]
            for candidates in allergens_dict.values():
                if val in candidates and len(candidates) != 1:
                    candidates.remove(val)
    return ','.join([list(allergens_dict[key])[0] for key in sorted(allergens_dict)])

