START

1. Create OPEN and CLOSED lists.

2. Insert the starting node into OPEN.

3. Calculate:
      f(n) = g(n) + h(n)

4. WHILE OPEN is not empty:

      a. Select the node with the
         lowest f(n) value.

      b. IF the node is the goal:
             Return the solution path.

      c. Move the node from OPEN to CLOSED.

      d. FOR each neighbouring node:

             Calculate the new path cost g(n).

             Calculate heuristic h(n).

             Calculate f(n) = g(n) + h(n).

             Update the node if a better
             path is found.

5. Return failure if no solution exists.

STOP
