import unittest


def frequencies ():
    with open ("input/day01.txt", 'r') as f:
        return [int(line.rstrip()) for line in f.readlines()]
    
def first_repeated_value(values, passes=200):
    total = 0
    seen = set()
    print(seen)
    i = 0
    
    while i < len(values) * passes:
        if total in seen:
            return total
        else:
            seen.add(total)
            total += values [i % len(values)]
            
            i +=1
    return None

class TestRepeatedValue(unittest.TestCase):
    
    def test_first_repeated(self):
        print(first_repeated_value([+1, -1]) is None) 
        print (first_repeated_value([+1, -1]))
        print (first_repeated_value([+3, +3, +4, -2, -4]))
        print (first_repeated_value([-6, +3, +8, +5, -6]))
        print (first_repeated_value([+7, +7, -2, -7, -4]))
        print (first_repeated_value(frequencies()))
        
    # def test_part_1(self):
    #     print("Part1: ", sum(frequencies()))
        
    #     assert sum(frequencies()) == 513
        
    # def test_part_2(self):
    #     print("Part 2:", first_repeated_value(frequencies()))
    #     assert first_repeated_value(frequencies()) == 287
        
        
if __name__ == '__main__':
    unittest.main()