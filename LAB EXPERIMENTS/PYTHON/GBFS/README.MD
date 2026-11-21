
START

1. Create a PRIORITY QUEUE.
2. Insert the starting node using its
   heuristic value h(n).

3. WHILE PRIORITY QUEUE is not empty:

      a. Remove the node with the
         lowest heuristic value.

      b. IF the node is the goal:
             Return the solution path.

      c. Mark the node as VISITED.

      d. FOR each unvisited neighbour:

             Calculate its heuristic value.
             Insert it into PRIORITY QUEUE.

4. Return failure if no solution exists.

STOP
