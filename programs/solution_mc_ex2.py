from __future__ import print_function, division  # Omit if using Python 3.x
import numpy as np
import mc_tools
from operator import itemgetter
import re

infile = 'web_graph_data.txt'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

n = 14 # Total number of web pages (nodes)

# First create a matrix Q with Q[i, j] = 1 if there is a link from i to j
# and Q[i, j] = 0 otherwise
Q = np.zeros((n, n), dtype=int)
f = open(infile, 'r')
edges = f.readlines()
f.close()
for edge in edges:
    from_node, to_node = re.findall('\w', edge)
    i, j = alphabet.index(from_node), alphabet.index(to_node)
    Q[i, j] = 1
# Now create the corresponding Markov matrix P
P = np.empty((n, n))
for i in range(n):
    P[i,:] = Q[i,:] / Q[i,:].sum()
# And compute the stationary distribution r
r = mc_tools.compute_stationary(P)
ranked_pages = {alphabet[i] : r[i] for i in range(n)}
# Print solution, sorted from highest to lowest rank
print('Rankings\n ***')
for name, rank in sorted(ranked_pages.iteritems(), key=itemgetter(1), reverse=1):
    print('{0}: {1:.4}'.format(name, rank))

