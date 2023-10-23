import random
import os


path = os. getcwd().rstrip('tests')


def convertFileToList(file_name):
    with open(file_name) as opened_file:
        lines = opened_file.readlines()
    return lines


def findAvailableSyllables(file_name, mode):
    modes = ['basic', 'custom', 'mixed']
    modes_ = ['basic:', 'custom:']
    if mode not in modes:
        return
    lines = convertFileToList(file_name)
    syllables = []
    if mode == 'mixed':
        for line in lines:
            syllable = line.rstrip('\n')
            if syllable not in modes_:
                syllables.append(syllable)
    else:
        valid_syllable = False
        for line in lines:
            syllable = line.rstrip('\n')
            if syllable == mode+':':
                valid_syllable = True
                continue
            elif syllable in modes_ and valid_syllable:
                break
            elif valid_syllable:
                syllables.append(syllable)
    return syllables


def findNameSyllables(raw_syllables_file_names=[path+'beggining_syllables.txt', path+'middle_syllables.txt', path+'end_syllables.txt'],
                      mode='basic', order=[]):
    available_syllables = []
    for file in raw_syllables_file_names:
        available_syllables.append(findAvailableSyllables(file, mode))
    # if no order is provided, the order is selected from the available order list
    if not len(order):
        orders = [[0,2], [0,1,2], [0,1,1,2]]
        order = random.choice(orders)
    # correct order for name generation must begin with 0, end with 2 and must have at least length 2
    elif len(order) < 2 or order[0] != 0 or order[-1] != 2:
        return 0
    for number in order:
        if 0 > number or number > 2:
            return
    # choose syllables according to the order
    name_parts = []
    for number in order:
        random_syllable = random.choice(available_syllables[number])
        name_parts.append(random_syllable)
    return name_parts


def combineSyllabelsToGetName(syllables):
    if syllables != 0:
        return ''.join(syllables)


def generateName(mode='basic', order=[]):
    result = combineSyllabelsToGetName(findNameSyllables(mode=mode, order=order))
    if isinstance(result, str):
        return result
    return 0
