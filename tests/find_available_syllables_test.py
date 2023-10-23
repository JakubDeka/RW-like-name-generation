from name_generator import findAvailableSyllables


def basicTest():
    assert findAvailableSyllables('test_syllable_file', 'basic') == ['Ale', 'Jak', 'To'], 'It doesn\'t work'


def customTest():
    assert findAvailableSyllables('test_syllable_file', 'custom') == ['A', 'No', 'Tak', 'To'], 'It doesn\'t work'


def mixedTest():
    assert findAvailableSyllables('test_syllable_file', 'mixed') == ['Ale', 'Jak', 'To', 'A', 'No', 'Tak', 'To'],\
        'It doesn\'t work'


basicTest()
customTest()
mixedTest()