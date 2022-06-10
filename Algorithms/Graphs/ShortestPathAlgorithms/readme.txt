Basic Floyd Warshall Implementation
input:
    d is a distance matrix for n nodes.
        e.g. d[i][j] is the distance to move directly from i to j.
        if no direct link from i to j then initialize d[i][j] = Infinity.
        the distance from a node to itself is 0. Initialize d[i][i] = 0 for all i.
    p is a predecessor matrix. it enables you to reconstruct the shortest paths.
        p[i][j] should be initialized to i.
output:
    d[i][j] contains the total cost along the shortest path from i to j.
    p[i][j] contains the predecessor of j on the shortest path from i to j.
for (k=0;k<n;k++)
  for (i=0;i<n;i++)
    for (j=0;j<n;j++)
      if (d[i][k] + d[k][j] < d[i][j]) {
        d[i][j] = d[i][k]+d[k][j];
        p[i][j] = p[k][j];
      }
