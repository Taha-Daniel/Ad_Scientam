import re
from atom_counter.utils import tuplist_to_dict, dict_fusion


class AtomsCounter:

    def __init__(self):
        self.decoded_formula = {}

    def _simple_count(self, string):
        """
        Separate a list of atoms in a dict with indexes of each atoms
        :param string:string of a simple molecula without parenthesis
        :return: dict_atom: dictionary with a counter of each atom inside this molecula
        """
        list_atom = re.findall('([A-Z][a-z]?)(\d*)', string)
        dict_atom = tuplist_to_dict(list_atom)
        return dict_atom

    def counter(self, str):
        """
        parser of the molecule with an iterative method reading from the left to the right and starting inside parenthesis
        :param: str: name of the molecule
        :return: (int,dict): iteration when we stop and dictionnary with atom counts of the molecula
        :method: I used a recursion to do it every time i open a parenthesis
        """
        buffer = []
        i = 0
        dict = {}
        while i < len(str):
            iterator = str[i]
            if iterator in '({[':
                '''Open parethesis lead to a recursion with the same function called after the parenthesis and make a 
                fusion between the old dictionnary and the recursed one'''
                par_length, temp_dict = self.counter(str[i + 1:])
                dict = dict_fusion(dict, temp_dict)
                i += par_length + 1
            elif iterator in ')}]':
                '''Closed parenthesis make calculate the number of occurence of each atoms since the start of its 
                associated parenthesis'''
                indice_regex = re.match(r'\d+', str[i + 1:])
                # Calulating the number index after the parenthesis
                if indice_regex:
                    i += len(indice_regex.group(0))
                    indice = int(indice_regex.group(0))
                else:
                    indice = 1
                temp_dict = self._simple_count(''.join(buffer))
                return i, dict_fusion(dict, temp_dict, indice)
            else:
                '''Each char is added inside this buffer until we meet a closed parenthesis'''
                buffer.append(str[i])

            i += 1
        return i, dict_fusion(dict, self._simple_count(''.join(buffer)))


def execute(molecule):
    return AtomsCounter().counter(molecule)[1]
