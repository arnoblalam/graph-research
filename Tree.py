from itertools import permutations

def perms(iterable):
    """documentatioin"""
    return [list(x) for x in permutations(iterable)]


def apply(f, x):
    """Apply a function to all elemens of a tree"""
    acc = []
    def worker(f, y, a):
        if not y["children"]:
            a.append(f(y))
            return a
        else:
            a.append(f(y))
            [worker(f, y, a) for y in y["children"]]
    acc.append(f(x))
    [worker(f, y, acc) for y in x["children"]]
    return acc

tirtho = {

    "name": "Tirtho",
    "weight": 7,
    "history": [],
    "children": []}

fake = {
    "name": "Fake",
    "weight": 1,
    "history": [],
    "children": []}

fake2 = {
    "name": "Fake Too",
    "weight": 2,
    "history": [],
    "children": []}


tonmoy = {
    "name": "Farid",
    "weight": 32,
    "children": [tirtho, fake, fake2]}

shonchoy = {
    "name": "Fahmid",
    "weight": 26,
    "children": []}


reza = {
    "name": "Reza",
    "weight": 64,
    "children": [tonmoy, shonchoy]}

tree = [reza]