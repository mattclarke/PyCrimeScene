import os


def generate_structure(input):
    structure = []
    for filepath, weight, loc in input:
        _create_children(_break_path(filepath), weight, loc, structure)
    return {'name': 'root', 'children': structure}


def _create_children(parts, weight, loc, structure):
    if len(parts) == 1:
        structure.append({'name': parts[0], 'children': [], 'weight': weight, 'size': loc})
        return

    names = [v['name'] for v in structure]

    if parts[0] not in names:
        structure.append({'name': parts[0], 'children': []})
        _create_children(parts[1:], weight, loc, structure[-1]['children'])
    else:
        _create_children(parts[1:], weight, loc, structure[names.index(parts[0])]['children'])


def _break_path(input):
    parts = []

    while True:
        input, y = os.path.split(input)
        parts.append(y)
        if input == '':
            break
    parts.reverse()
    return parts

