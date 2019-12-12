# jarvis march
#    __
#  /    \
#    <--/

import random
import sys

def print_points(points, cvh, sz):
    '''display the grid of points'''
    # empty grid
    grid = []
    for i in range(sz+1):
        grid.append(['  ']*(sz+1))
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

def convexhull_jarvis_march(points):
    '''jarvis march algorithm'''
    # https://iq.opengenus.org/gift-wrap-jarvis-march-algorithm-convex-hull/

    convexhull = []

    # find left-most point
    p = points[0]
    for point in points:
        if point[0] < p[0]: p = point
    convexhull.append(p)

    # go over all the other points
    while True:
        # pick any point to start with (except most recent point in convexhull)
        ep = points[0]
        while ep == convexhull[-1]:
            ep = points[random.randint(0,len(points)-1)]

        for pt in points:
            # if any other point left-er than ep, update ep
            if orientation(convexhull[-1], pt, ep) == 2:
                ep = pt
    
        convexhull.append(ep)   # add next left-most point to the list of vertices in convexhull

        # end of convex hull. wrapped around to starting point.
        if convexhull[-1] == convexhull[0]:
            convexhull.pop()
            break
    
    return convexhull



def main():
    if len(sys.argv) > 1:
        n = sys.argv[1]     # take seed as cmd arg
        random.seed(n)
    sz = 30
    xmax = sz
    ymax = sz

    # generate random points
    points = []
    for i in range(30):
        point = (random.randint(0,xmax),random.randint(0,ymax))
        if point not in points:
            points.append(point)
    
    cvh = convexhull_jarvis_march(points)

    # results
    print("convexhull:",cvh)
    print_points(points,cvh,sz)

if __name__ == '__main__':
    main()