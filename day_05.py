import string
import unittest

data = open("input/day05.txt").read().strip()

def reduce_polymer(polymer):
    stack = list()
    for c in polymer:
        #breaks here
        if stack and c.swampcase() == stack[-1]:
            stack.pop()
        else:
            stack.append(c)
            print(stack)
    return ''.join(stack)

class TestPolymer(unittest.TestCase):
    
    def test_reduce_polymer(self):
        assert reduce_polymer("hHsSmMHhhHwWfoo") == 'foo'
        assert reduce_polymer("hHsSmMHhhHwWfoohHsSmMHaAhhHwW") == 'foo'
        


if __name__ == "__main__":
    unittest.main()