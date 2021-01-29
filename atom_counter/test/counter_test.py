import unittest
from atom_counter.counter import AtomsCounter




class CounterTest(unittest.TestCase):

    def test_counter(self):
        counter = AtomsCounter()
        formula = "O((CN2)3K)4"
        self.assertEqual(counter.counter(formula)[1], {'N': 24, 'C': 12, 'K': 4, 'O': 1})
        formula = "Mg2[CH4{NNi2(Li2O4)5}14]3"
        self.assertEqual(counter.counter(formula)[1], {'Ni': 84, 'Mg': 2, 'Li': 420, 'H': 12, 'N': 42, 'C': 3, 'O': 840})
        formula = "(NH4)2HPO4"
        self.assertEqual(counter.counter(formula)[1], {'H': 9, 'N': 2, 'O': 4, 'P': 1})


if __name__ == '__main__':
    unittest.main()
