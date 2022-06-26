from collections import Counter
from itertools import permutations
from collections import namedtuple

import unittest
from xmlrpc.client import Marshaller

def box_ids():
    with open("input/day02.txt", 'r') as f:
        print (f.readlines())
        return [line.rstrip() for line in f.readlines()]
    
def has_n(string, n):
    return n in Counter(string).values()

def checksum(ids):
    twos = 0
    threes = 0
    
    for string in ids:
        twos += has_n(string, 2)
        threes += has_n(string, 3)
        
    return twos * threes 

def char_difference(a, b):
#Number of differing chars in equal lenght strings
    if len(a) != len(b):
        return ValueError("Expecting equal lenght strings")
    
    return sum(x != y for x, y in zip(a,b)) #elaborate

class Match(namedtuple('Match', ['a', 'b', 'diff'])):
    @property
    def overlap(self):
        overlap_len = len(self.a) - self.diff
        for i in range(self.diff + 1 ):
            substr = self.a[i: overlap_len + 1]
            if substr in self.b:
                return substr
            
            
def closest_match(words):
    closest = Match(None, None, 100)
    # permutations
    for a, b in permutations(words, 2):
        match = Match(
            a=a,
            b=b,
            diff=char_difference(a,b)
        )
        if match.diff < closest.diff:
            closest = match
    return closest


class TextBoxScan(unittest.TestCase):

    def test_has_n(self):
        print(box_ids())
        # print("not bar, 2", not has_n("bar", 2))
        # print("bababac, 3", has_n("bababac", 3))
        
    def test_char_difference(self):
        assert char_difference("foo", "bar") == 3
        assert char_difference("foo", "for") == 1
        
    def test_part_1(self):
        print("Part 1", checksum(box_ids()))

        assert checksum(box_ids()) == 7904

    # def test_part_2(self):
    #     match = closest_match(box_ids())

    #     print("Part 2:", match.overlap)

    #     assert match.overlap == "wugbihckpoymcpaxefotvdzns"


if __name__ == '__main__':
    unittest.main()