from name_generator import generateName


def shouldReturnZero():
    assert generateName(order=[1]) == 0


def shouldNotReturnName():
    assert generateName(order=[1,2]) == 0


def shouldReturnName():
    assert isinstance(generateName(order=[0,2]), str)


shouldReturnZero()
shouldNotReturnName()
shouldReturnName()
