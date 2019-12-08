# graham scan

import random
import sys
import math

def print_n_points(n_points):
    '''utility function. print grid with order of points.'''
    grid = []
    for i in range(21):
        grid.append(['. ']*21)
    for k in range(len(n_points)):
        p = n_points[k]
        grid[p[0]][p[1]] = str(k)[-1]+' ' if k<10 else str(k)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()

def print_points(points, cvh):
    '''display the grid of points, showing points on the convex hull'''
    # empty grid
    grid = []
    for i in range(21):
        grid.append(['. ']*21)
    # points on grid
    for p in points:
        grid[p[0]][p[1]] = '* '
    # points on convex hull
    for p in cvh:
        grid[p[0]][p[1]] = '@ '
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()

def orientation(cvh_prev, pt, ep):
    '''check if point pt is more left that ep(potential endpoint) from cvh_prev (recent point on convexhull)'''
    # https://math.stackexchange.com/a/274728

    # d=(x−x1)(y2−y1)−(y−y1)(x2−x1)
    d = (ep[0]-cvh_prev[0])*(pt[1]-cvh_prev[1]) - (ep[1]-cvh_prev[1])*(pt[0]-cvh_prev[0])

    # if pt left of line from (cvh_prev)-----(ep)
    if d == 0:  # collinear
        return 0
    elif d>0:     # right side
        return 1
    elif d<0:     # left side
        return 2

def convexhull_graham_scan(points):
    '''graham scan algorithm for convex hull'''
    # https://iq.opengenus.org/graham-scan-convex-hull/
    # https://www.algorithm-archive.org/contents/graham_scan/graham_scan.html (for sorting points)

    # find bottom-most point
    p = 0
    for i in range(len(points)): #point in points:
        if points[i][1] < points[p][1]:
            p = i
        elif points[i][1] == points[p][1] and points[i][0]<points[p][0]:    # if 2 bottom-most points, choose the one with less x
            p = i
    points[0],points[p] = points[p],points[0]       # put target point in first of list

    # sort remaining points by polar angle (using atan())
    rfp = points[0]     # reference point
    d = {}
    for p in points[1:]:
        score = math.atan2(p[1] - rfp[1], p[0] - rfp[0])        # ccw polar angle
        if score in d:
            d[score].append(p)
        else:
            d[score] = [p]
    n_points = [rfp]            # make new list of sorted points
    for score in sorted(d.keys()):
        if len(d[score]) == 1:
            n_points.append(d[score][0])
        elif len(d[score]) > 1:
            tl = sorted(d[score])
            for i in tl:
                n_points.append(i)

    print_n_points(n_points)

    convexhull = []

    # traverse sorted list of points and find the convexhull
    for p in n_points:
        convexhull.append(p)
        if len(convexhull) > 3:
            # check 
            while len(convexhull)>3:
                if orientation(convexhull[-3], convexhull[-2], convexhull[-1]) == 1:
                    convexhull.pop(-2)
                else:
                    break
    
    return convexhull

def main():
    if len(sys.argv) > 1:
        n = sys.argv[1]     # take seed as cmd arg
        random.seed(n)
    xmax = 20
    ymax = 20

    # generate random points
    points = []
    for i in range(20):
        point = (random.randint(0,xmax),random.randint(0,ymax))
        if point not in points:
            points.append(point)
    
    cvh = convexhull_graham_scan(points)

    # results
    print(cvh)
    print_points(points,cvh)

if __name__ == '__main__':
    main()