Assignment 2
Author: Hassan Tariq, 100657119

For the plotting, I included it in the compare.py file and I combined
the two plots, instead of plotting on two different graphs. This was so
I could easily compare the two plots within one program.

I also only ran the loop from 10^2 to 10^4 due to built-in function, not
being able to handle the nxn matrix past 10^4. This is due to memory
limitations of my machine and the flops required to actually compute it
using the 'traditional' (scipy) method.

Note: I ran the built-in function as a scipy.dot(matrix, matrix) instead of matrix.dot(matrix),
      I did this to show the difference in between the traditional and the diagonal method.
      If I ran the matrix.dot(matrix) function, it would consider it sparse and run faster than
      the expected output. I did not include that sparse implementation to keep the output simple
      but I am aware that this is an option to compute and not run out of memory.
