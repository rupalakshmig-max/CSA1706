START

1. Create an N × N chessboard.

2. Place queens one by one in each row.

3. Define a function SAFE(row, col):

      Check the same column.
      Check the upper-left diagonal.
      Check the upper-right diagonal.

      IF another queen is found:
          RETURN FALSE.

      ELSE:
          RETURN TRUE.

4. Define a function SOLVE(row):

      IF row = N:
          RETURN TRUE.

      FOR col = 0 to N-1:

          IF SAFE(row, col) is TRUE:

              Place a queen at (row, col).

              IF SOLVE(row + 1) is TRUE:
                  RETURN TRUE.

              Remove the queen (Backtrack).

      RETURN FALSE.

5. Call SOLVE(0).

6. IF solution exists:
      Display the chessboard.

   ELSE:
      Display "No solution exists".

STOP
