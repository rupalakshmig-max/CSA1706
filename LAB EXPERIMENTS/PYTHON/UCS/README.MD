START

1. Create a PRIORITY QUEUE.
2. Insert the starting node with cost 0.

3. WHILE PRIORITY QUEUE is not empty:

      a. Remove the node with the lowest cost.

      b. IF the node is the goal:
             Return the path and total cost.

      c. FOR each neighbouring node:

             Calculate the new path cost.

             IF the new cost is lower:
                 Update the cost.
                 Insert the neighbour into
                 PRIORITY QUEUE.

4. Return failure if no solution exists.

STOP
