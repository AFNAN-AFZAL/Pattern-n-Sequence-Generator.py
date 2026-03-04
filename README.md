# Pattern-n-Sequence-Generator.py

Developing a command-line Python program that generates different number and star patterns using loops and iteration techniques. This task strengthens understanding of loops, nested loops, logical thinking, and pattern generation — essential skills for programming problem-solving.
Simple README: How it Works

Logic Behind the 4 Patterns

1. Star Triangle:
2.  Uses simple string multiplication ("*" * i). As i grows, the line gets longer.
3. 
4. Reverse Star:
5.  Uses a range that counts backwards (range(n, 0, -1)). It starts big and shrinks.
6. 
7. Number Triangle
8. : Uses a Nested Loop. The inner loop handles the horizontal counting (1, 2, 3...) while the outer loop handles the vertical rows.
9. 
10. Number Pyramid
11. 
•	Spaces:
 We calculate spaces as (Total Size - Current Row). If size is 5 and we are on row 1, we print 4 spaces.
•	Odd Numbers: To make a pyramid look balanced, we usually use an odd number of characters per line (1, 3, 5, 7...). That is why we use (2 * i).
