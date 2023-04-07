"""
Arrange Buildings
===================

1. You are given a number n, which represents the length of a road. The road
has n plots on it's each side.
2. The road is to be so planned that there should not be consecutive buildings
on either side of the road.
3. You are required to find and print the number of ways in which the buildings
can be built on both side of roads.


sample input
=============
6

sample output
=============
441
"""


def arrange_buildings(n):
    os = 1
    ob = 1

    for i in range(2, n + 1):
        nb = os
        ns = os + ob

        os = ns
        ob = nb

    total = os + ob
    total = total * total
    return total


if __name__ == '__main__':
    n = int(input())
    print(arrange_buildings(n))
