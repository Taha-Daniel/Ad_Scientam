import sys
from atom_counter.counter import AtomsCounter

if __name__ == '__main__':
    print("La molecule à déveloper:", sys.argv[1])
    formula = sys.argv[1]
    counter = AtomsCounter()
    print(counter.counter(formula)[1])