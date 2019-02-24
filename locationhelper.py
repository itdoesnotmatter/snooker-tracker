def near(p1, p2):
    return in_threshold( p1[0], p2[0] ) \
        and in_threshold( p1[1], p2[1] )


def in_threshold(n1, n2, threshold=5):
    return abs(n1 - n2) < threshold


def avg(nums):
    return int( sum(nums) / len(nums) )


def points_avg(points):
    p0s = list(p[0] for p in points)
    p1s = list(p[1] for p in points)

    return ( avg(p0s), avg(p1s) )
