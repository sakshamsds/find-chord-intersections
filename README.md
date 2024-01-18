
### Problem Statement
Given a list of chords in a circle, count the number of intersections, if any. For simplicity’s sake, assume all starting and ending points are unique.

### Input
Two lists: one being an identifier of the chord and the other being the radian measure. The values themselves are radians and sorted in ascending order. Look below for more clarity.

#### Test Input 1
```bash
python find_intersections.py --radians 0.78 1.47 1.77 3.92 --identifiers s1 s2 e1 e2  
```
Output
```
Parsed arguments Namespace(identifiers=['s1', 's2', 'e1', 'e2'], radians=[0.78, 1.47, 1.77, 3.92])
Number of intersections found: 1
```

#### Test Input 2
```bash
python find_intersections.py --radians 0.35 0.52 1.04 1.74 2.08 2.15 2.35 3.83 4.05 4.36 5.55 5.94 --identifiers e4 s1 s2 e5 e1 e6 s3 e3 s4 e2 s6 s5 
```
Output
```
Parsed arguments Namespace(identifiers=['e4', 's1', 's2', 'e5', 'e1', 'e6', 's3', 'e3', 's4', 'e2', 's6', 's5'], radians=[0.35, 0.52, 1.04, 1.74, 2.08, 2.15, 2.35, 3.83, 4.05, 4.36, 5.55, 5.94])
Number of intersections found: 7
```

### Complexity
Time Complexity: O(n*n) \
Space Complexity: O(n)

### Test Input 2 Visualization 
![1](https://github.com/sakshamsds/find-chord-intersections/blob/main/find_intersections.png)

