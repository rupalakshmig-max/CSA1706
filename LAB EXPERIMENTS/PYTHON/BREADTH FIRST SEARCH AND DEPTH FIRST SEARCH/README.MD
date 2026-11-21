START

1. Create an empty QUEUE.
2. Insert the starting node into QUEUE.
3. Mark the starting node as VISITED.

4. WHILE QUEUE is not empty:

      a. Remove the front node from QUEUE.
      b. Display the node.

      c. FOR each unvisited neighbour:

             Mark it as VISITED.
             Insert it into QUEUE.

5. Stop when the goal node is found.

STOP
START

1. Create an empty STACK.
2. Push the starting node into STACK.

3. WHILE STACK is not empty:

      a. Pop a node from STACK.

      b. IF the node is not visited:

             Mark it as VISITED.
             Display the node.

      c. IF the node is the goal:
             STOP.

      d. Push all unvisited neighbours
         into STACK.

STOP
