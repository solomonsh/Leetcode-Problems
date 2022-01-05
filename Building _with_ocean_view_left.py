"""
Given an array representing heights of buildings. 
The array has buildings from left to right as shown in below diagram, count number of buildings facing the sunset.
It is assumed that heights of all buildings are distinct.

Input : arr[] = {7, 4, 8, 2, 9}
Output: 3
Explanation: As 7 is the first element, it can 
see the sunset.
4 can't see the sunset as 7 is hiding it. 
8 can see.
2 can't see the sunset.
9 also can see the sunset.

Input : arr[] = {2, 3, 4, 5}
Output : 4

"""


def findBuildings(lst):
    building_counts = 0
    for i, ls in enumerate(lst):
        if i == 0:
            building_counts += 1
        elif max(lst[:i]) < ls:
            building_counts += 1
    return building_counts


# optimized version
def findBuildingsOptimized(lst):
    building_counts = 0
    current_max = lst[0]
    for i, ls in enumerate(lst):
        if current_max <= ls:
            building_counts += 1
        else:
            current_max = ls
    return building_counts


print(findBuildingsOptimized([7, 4, 8, 2, 9]))
print(findBuildingsOptimized([2, 3, 4, 5]))
