import argparse
from typing import List

class Chord:
    def __init__(self, start=0, end=0) -> None:       
        self.s = start
        self.e = end

    # Checks if chords c1 and c2 intersects inside the circle
    def intersect(self, c1: List[int], c2: List[int]) -> bool:
        if c1.s < c1.e:
            if c2.s < c2.e:
                return c2.s < c1.e and c1.e < c2.e
            else:   # c2.s > c2.e
                return (c2.s < c1.e and c2.e < c1.s) or (c2.s > c1.e and c1.s < c2.e < c1.e)
        else:   # c1.s > c1.e
            if c2.s < c2.e:
                return False
            else:   # c2.s > c2.e
                return c1.e < c2.e < c1.s

    def count_intersections(self, radians: List[int], identifiers: List[str]) -> int:
        num_intersections = 0
        num_chords = len(identifiers) // 2
        
        # Initialize chords
        chords = [Chord() for _ in range(num_chords)]            
        
        # Get the chords start and end points
        for i in range(len(identifiers)):
            chord_idx = int(identifiers[i][1:]) - 1
            if identifiers[i][0] == 's':        # if its the starting point
                chords[chord_idx].s = radians[i]
            else:
                chords[chord_idx].e = radians[i]
                
        # Sort the chords based on the start points
        chords.sort(key=lambda chord: chord.s)         # might not be required, instructions were a bit unclear, O(nlogn)

        # Iterate over every pair
        for i in range(num_chords):             # O(n*n)
            for j in range(i, num_chords):
                num_intersections += int(self.intersect(chords[i], chords[j]))
        
        return num_intersections

if __name__ == '__main__':
    # Parse the CLI arguments
    parser = argparse.ArgumentParser('Chord Intersections')
    parser.add_argument(
        '--radians',
        nargs='*',
        type=float
    )
    parser.add_argument(
        '--identifiers',
        nargs='*',
        type=str
    )
    args = parser.parse_args()
    print('Parsed arguments', args)
    
    chords = Chord()
    count = chords.count_intersections(args.radians, args.identifiers)
    print('Number of intersections found:', count)