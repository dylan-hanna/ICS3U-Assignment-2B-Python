#!usr/bin/env python3

# Created by: Dylan Hanna
# Created on: Sept 2019
# This program calculates the perimeter of a triangle

def main():
    
    side_1 = int(input("Enter side length 1:  "))
    side_2 = int(input("Enter side length 2:  "))
    side_3 = int(input("Enter side length 3:  "))
    
    perimeter = side_1 + side_2 + side_3 
   
    
    print("")
    print("Perimeter is {}".format(perimeter))
    
    
if __name__ == "__main__":
   main()