"""
 There are n buildings in a line. You are given an integer array heights 
 of size n that represents the heights of the buildings in the line.

 The ocean is to the right of the buildings. A building has an ocean view if the building
 can see the ocean withought obstructions. Formally, a building has an ocean view if all
 the buildings to it's righat have a smaller height.
 
 Return a list of indices(0-indexed) of buildings that have an ocean view, sorted in increasing order.

 Example 1:
 Input: heights = [4,2,3,1]
 Output: [0,2,3]

 Explanation: Buildin 1 (0-indexed) does not have an ocean view because building 2 is taller.


 Example 2:
 Input: heights = [4,3,2,1]
 Output: [0,1,2,3]
"""


def findBuildings(lst):
    buildings_view = []
    current_max = lst[-1]
    for i in range(len(lst)-1,-1,-1):
        if current_max<lst[i] or i == len(lst)-1:
            buildings_view.append(i)
            current_max = lst[i]
     
    buildings_view.reverse()

    # Manually reversing the list
    
    # for i in range(len(buildings_view)//2,-1,-1):
    #     index = len(buildings_view) - (i+1)
    #     temp = buildings_view[i] 
    #     buildings_view[i] = buildings_view[index]
    #     buildings_view[index] = temp

    return buildings_view


print(findBuildings([4,3,2,1]))
print(findBuildings([4,2,3,1]))

 

 
