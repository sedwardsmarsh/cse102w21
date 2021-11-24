#!/usr/local/bin/python3
import argparse
import random
from typing import Optional

def findSet(array, v1, v2):
    '''Returns the set from ARRAY containing V1 and V2 or [] if no set exists'''
    result_set = [s for s in array if (v1 in s and v2 in s)]
    return [] if result_set == [] else result_set

def findNumSets(array, v1):
    '''Returns the number of sets from ARRAY containing V1'''
    result_set = [s for s in array if v1 in s]
    return 0 if result_set == [] else len(result_set)

# choose random number of vertices and edges
num_vertices = random.randint(4, 10)
num_max_edges = num_vertices * (num_vertices - 1) / 2
num_edges = random.randint(1, num_max_edges)

# output filename is required
parser = argparse.ArgumentParser()
parser.add_argument('o', type=str, metavar='OUTPUT FILE')
args = parser.parse_args()

# parse command line arguments
args_dict = vars(args)
output_file = args_dict['o']

# choose a source and destination vertex
unweighted_edges = []
for _ in range(num_edges):
    while True:
        v1 = random.randint(1, num_vertices)
        v2 = random.randint(1, num_vertices)

        # choose v1 and v2 s.t. 
        #   1. v1 and v2 are not equal
        #   2. set containing v1, v2 doesn't already exist
        #   3. # of v1 edges is < num_vertices - 1
        #   4. # of v2 edges is < num_vertices - 1
        if v1 != v2 and findSet(unweighted_edges, v1, v2) == [] and findNumSets(unweighted_edges, v1) < num_vertices - 1 and findNumSets(unweighted_edges, v2) < num_vertices - 1:
            unweighted_edges.append({v1, v2})
            break

# randomly assign a weight between 1 and 10 to each edge 
weighted_edges = [(edge, random.randint(1, 10)) for edge in unweighted_edges]

# print(f'{num_vertices=}')
# print(f'{num_edges=}')
# print(f'{len(weighted_edges)=}')
# for edge in weighted_edges:
#     print(edge)
# print()

# write graph to output file
with open(output_file, 'w') as f:
    f.write(f'{num_vertices}\n')
    f.write(f'{num_edges}\n')
    for (vertex1, vertex2), weight in weighted_edges:
        f.write(f'{vertex1} {vertex2} {weight}\n')