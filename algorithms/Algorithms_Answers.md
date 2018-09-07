Add your answers to the Algorithms exercises here.

Exercise I:
  a) There are at least two reasons that we can see that runtime complexity is
  O(n) first we have a bound of n^3 that we are incrementing to by steps of
  n^2. This is equivalent to divding n^3 by n^2 which is equal to n. Secondly
  an analysis of the outputs of this funciton for several values n shows that
  the function takes n number of operations to complete. For these reasons
  we conclude that our runtime complexity is O(n)

  b) Because we are dealing with one operation inside of nested for loops that whose ranges are bounded
  by n we conclude that the runtime complexity is O(n^3). Looking analyzing the output
  of this function would also help us to conclude that

  c) This is a recursive functions whose depth relies on n for this reason we
  conclude that the runtime complexity is O(c^n), exponential

Exercise II:
I recommend a binary search or similar for this problem. Start by dropping the
egg off of floor n if it breaks then we drop a new egg off of floor n//2 if it breaks
again we repeat this process until we get a level where it doesn't break. From there
we go to a floor that is at the midpoint of this floor and the previous n//2 floor.
We continue this process until we find the precise floor _f_ where the egg does
not break.
