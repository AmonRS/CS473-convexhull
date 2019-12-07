# Convex Hull algorithm
# implement , compare , contrast
# several testcases/examples (10-100 2d points each)
# analysis of computational efficiency   (also generalize to asymptotic run-time as N grows very large

import random

def orientation(cvh_prev, pt, ep):
    # if pt left of line from convexhull[-1]<-->ep
    if counterclockwise:
        return 1
    return 0

def convexhull_jarvis_march(points):
    # https://iq.opengenus.org/gift-wrap-jarvis-march-algorithm-convex-hull/

    convexhull = []

    # find leftmost point
    p = points[0]
    for point in points:
        if point[0] < p[0]: p = point
    convexhull.append(p)

    # go over all the other points
    while True:
        ep = points[0]      # pick any point to start with
        for pt in points:
            if (ep == convexhull[-1]) or (pt left of line from convexhull[-1]<-->ep):   # if any other point left-er than ep, update ep
                ep = pt
    
        convexhull.append(ep)   # add next left-most point

        # end of convex hull. wrapped around to starting point.
        if convexhull[-1] == convexhull[0]:
            convexhull.pop()
            break



def main():
    random.seed(7)
    points = []
    for i in range(20):
        points.append( (random.randint(0,20),random.randint(0,20)) )
    convexhull_jarvis_march(points)
if __name__ == '__main__':
    main()