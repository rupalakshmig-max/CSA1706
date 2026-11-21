START

1. Create a game tree.
2. Set ALPHA = -INFINITY.
3. Set BETA = +INFINITY.

4. Evaluate the root node.

5. IF the node is MAX:

      Find the maximum value.
      Update ALPHA.

6. IF the node is MIN:

      Find the minimum value.
      Update BETA.

7. IF ALPHA >= BETA:

      Prune the remaining branches.

8. Continue evaluating the remaining
   necessary nodes.

9. Return the best value.

STOP
