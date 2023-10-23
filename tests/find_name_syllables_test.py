from name_generator import findNameSyllables


def basicModeTest():
    assert findNameSyllables(['test_beggining_syllables.txt', 'test_middle_syllables.txt', 'test_end_syllables.txt'], order=[0,1,2]) \
           == ['Vi', 'ser', 'ys']


def customModeTest():
    assert findNameSyllables(['test_beggining_syllables.txt', 'test_middle_syllables.txt', 'test_end_syllables.txt'], order=[0,1,2],
                             mode='custom') == ['Te', 'pa', 'cur']


def customOrderTest():
    assert findNameSyllables(['test_beggining_syllables.txt', 'test_middle_syllables.txt', 'test_end_syllables.txt'],
                             mode='basic', order=[0, 1]) == ['Vi', 'ser']


def mixedModeTest():
    assert findNameSyllables(['test_beggining_syllables.txt', 'test_middle_syllables.txt', 'test_end_syllables.txt'],
                             mode='mixed', order=[0, 1]) in [['Vi', 'ser'], ['Te', 'pa'], ['Te', 'ser'], ['Vi', 'pa']]


def tooShortOrderTest():
    assert findNameSyllables(['test_beggining_syllables.txt', 'test_middle_syllables.txt', 'test_end_syllables.txt'],
                             mode='mixed', order=[0]) == 0


basicModeTest()
customModeTest()
customOrderTest()
mixedModeTest()
tooShortOrderTest()
