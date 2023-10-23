from name_generator import convertFileToList


def simpleCorrectTest():
    assert convertFileToList('test_syllable_file')\
           == ['basic:\n', 'Ale\n', 'Jak\n', 'To\n', 'custom:\n', 'A\n', 'No\n', 'Tak\n', 'To'], 'It doesn\'t work'


def simpleFalseTest():
    assert convertFileToList('test_syllable_file')\
           != ['basic:\n', 'custom:\n', 'A\n', 'To\n'], 'It doesn\'t work'


simpleCorrectTest()
simpleFalseTest()