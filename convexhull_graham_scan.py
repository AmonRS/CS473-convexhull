# Convex Hull algorithm
# implement , compare , contrast
# several testcases/examples (10-100 2d points each)
# analysis of computational efficiency   (also generalize to asymptotic run-time as N grows very large

import random

def convexhull_graham_scan(points):
    pass



def main():
    random.seed(7)
    points = []
    for i in range(20):
        points.append( (random.randint(0,20),random.randint(0,20)) )
    convexhull_graham_scan(points)
if __name__ == '__main__':
    main()