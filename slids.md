## 5-Intermediate-file-handling
### 19
What is the minimum number of bits to represent the state of a tic-tac-toe board? two bits per cell, times the amount of cells(nine*three = twenty-seven)
What is the minimum number of bytes? byte is eight bits need at least 27 bits. Three bytes is twenty-four bits so need four bytes equaling thirty-two bits
How does this compare to the minimum number of bytes for a text representation?
>>> print(int.bit_count(ord("x")))
4
>>> print(int.bit_count(ord("o")))
6
>>> print(int.bit_count(ord(" ")))
1
eleven bits for each cell * nine = ninety-nine for the board
### 22-23
Scenario (from KBA)
Consider the following fictional image file format:
File Structure: A binary file containing image data.
First 9 bytes: Text encoded with the dimensions of the image (e.g., "1920x1080").
Following bytes: Series of 3 bytes representing RGB values of each of the pixels.
E,g. 1920x1080 200244002
E,g. 1920x1080 200 244 002

Questions
Given the specification, outline how you would use seek, read, write, and tell (as appropriate) to:
(a) Retrieve the RGB Value of the Center Pixel?
1920x1080 = 2,073,600 / 2 = 1,036,800 * 3 bits 3,110,400 seek to.
( b) Retrieve all pixel values as integers from a random 100x100 grid within the image? 
Each line is 1920 * 3 = 5760 bits long
Each line in the 100x100 100 * 3 = 300 bits long
From the starting point of the 100x100 read the next 100 pixels (300 bits)
then find the start of the next line of the 100x100 seek(5760-300) loop for another 99 times.

(b) Reduce the resolution by half?
read every second pixel