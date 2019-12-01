# Convex Hull algorithm
# Amon , Pragalva
import random

def convexhull_jarvis_algo(points):
    # https://iq.opengenus.org/gift-wrap-jarvis-march-algorithm-convex-hull/
    pass

def convexhull_graham_scan(points):
    pass



def main():
    points = []
    for i in range(20):
        points.append((random.randint(0,20),random.randint(0,20)))
    convexhull_jarvis_algo(points)
    convexhull_graham_scan(points)
if __name__ == '__main__':
    main()