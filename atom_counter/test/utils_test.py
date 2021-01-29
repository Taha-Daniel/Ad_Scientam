import unittest
from atom_counter.utils import tuplist_to_dict, dict_fusion


class UtilsTest(unittest.TestCase):
    def test_tuplisttodict(self):
        """test tuplist_to_dict"""
        self.assertEqual(tuplist_to_dict([('x', 3), ('x', 2), ('y', 1)]), {'x': 5, 'y': 1})

    def test_dict_fusion(self):
        """test tuplist_to_dict"""
        self.assertEqual(dict_fusion({'x': 5, 'z': 6}, {'x': 5, 'y': 1}, 3), {'x': 30, 'y': 3, 'z': 18})


if __name__ == '__main__':
    unittest.main()
