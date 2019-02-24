def distinct_locations(points, recurse=True):
    distinct_points = []

    if recurse:
        points = sorted(points)
    else:
        points = sorted( points, key=lambda el: el[1] )

    near_points = []
    prev_p = points[0]

    for p in points:
        if near(p, prev_p):
            near_points.append(p)
        else:
            if len(near_points) == 1:
                near_points.append(prev_prev_p)
            new_point = points_avg(near_points) if near_points else prev_p
            distinct_points.append( new_point )
            near_points = []
        prev_prev_p = prev_p
        prev_p = p

    if near_points:
        distinct_points.append( points_avg(near_points) )
    else:
        distinct_points.append( prev_p )

    return remove_dupes(distinct_points) if recurse else distinct_points


def remove_dupes(points):
    unduped_points, near_points = [], []
    prev_p = points[0]

    for p in points:

        if in_threshold( p[0], prev_p[0] ):
            near_points.append(p)
        else:
            if len(near_points) > 0:
                if len(near_points) == 1:
                    near_points.append(prev_prev_p)
                near_points = distinct_locations( near_points, False )
            elif len(near_points) == 0:
                near_points.append(prev_p)

            unduped_points.extend( near_points )
            near_points = []

        prev_prev_p = prev_p
        prev_p = p

    if len(near_points) > 0:
        unduped_points.extend( distinct_locations(near_points, False) )
    else:
        unduped_points.append(prev_p)

    return unduped_points


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
