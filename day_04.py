from curses.textpad import rectangle
import re
from dataclasses import dataclass
from collections import defaultdict
from string import hexdigits
from turtle import width
import unittest

rectangle_parser = re.compile(r"#(\d+)\s@\s(\d+,\d+):\s(\d+x\d+)") #what
with open ("imput/day03.txt", 'r') as input_file:
    lines = [line.rstrip() for line in input_file.readlines()]
    
    
@dataclass
class Rectangle:
    uid: str
    x: int
    y: int
    width: int
    height: int
    
    def __str__(self) :
        return f"Rectangle('#{self.uid} @ {self.x},{self.y}: {self.width}x{self.height}')"
    
    @classmethod
    def rectangle_from_string(cls, string):
        try: 
            result = rectangle_parser.match(string)
            uid = result.group(1) #what
            x, y= [int(i) for i in result.group(2).split(',')]
            w, h= [int(i) for i in result.group(3).split('x')]
        except (AttributeError, TypeError):
            raise ValueError(f"Failed to parse: '{string}'")
        
        return Rectangle (uid, x, y, w, h)
    
    def points(self):
        points = []
        for x in range(self.x, self.x + width):
            for y in range(self.y, self.y + self.height):
                points.append((x,y))
                
        return points
    
def rectangles():
    return [Rectangle.rectangle_from_string(line) for line in lines]

def grid_map():
    grid = defaultdict(int) #read
    
    for rect in rectangles():
        for point in rect.points():
            grid[point] +=1
            
    return grid

def total_overlapped_cells_map(grid):
    return len([x for x in grid.values() if x > 1])

class TestFabricOverlap(unittest.TestCase):

    def setUp(self):
        self.grid = grid_map()

    def test_part_1(self):
        print("Part 1:", total_overlapped_cells_map(self.grid))

    def test_part_2(self):
        for rect in rectangles():
            points = rect.points()
            if sum(self.grid[point] for point in points) == len(points):
                print("Part 2:", rect)


if __name__ == '__main__':
    unittest.main()
