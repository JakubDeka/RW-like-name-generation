from name_generator import combineSyllabelsToGetName


def shouldGetCombined():
    assert combineSyllabelsToGetName(['J', 'ak', 'ub']) == 'Jakub', 'Something is wrong'


def shouldNotGetCombined():
    assert combineSyllabelsToGetName(['J', 'ak', 'ub']) != 'Jakubek', 'Something is wrong'


shouldGetCombined()
shouldNotGetCombined()
