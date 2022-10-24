
import os
import sys

with open(os.path.join(sys.path[0], "triangle.txt"), "r") as TextFile:
    triangle = [[int(i) for i in line.split()] for line in TextFile]

previous_sums = []
for row in triangle:
    current_sums = []
    for position, cell_value in enumerate(row):
        sum_from_right = 0 if position >= len(previous_sums) else previous_sums[position]
        sum_from_left = (previous_sums[position - 1]
                         if 0 < position <= len(previous_sums)
                         else 0)
        current_sums.append(max(sum_from_right, sum_from_left) + cell_value)

    previous_sums = current_sums

print('The Maximum Number of Second Triangle ist:', max(previous_sums))