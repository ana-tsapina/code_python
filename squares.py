
#import statements: 

from math import sqrt, floor 

tiles = int(input()) 

answer = tiles ** 0.5 
answer = sqrt(tiles)
answer = floor(answer)

print(f"The largest square had a side length of {answer}.")

