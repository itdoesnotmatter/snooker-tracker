from ball import Ball

import locationhelper as loc


class Balls:
    def __init__(self, locations):
        self.locations = self._distinct_locations( locations )
        self.__balls = []


    def _distinct_locations(self, points, recurse=True):
        distinct_points = []

        if recurse:
            points = sorted(points)
        else:
            points = sorted( points, key=lambda el: el[1] )

        near_points = []
        prev_p = points[0]

        for p in points:
            if loc.near(p, prev_p):
                near_points.append(p)
            else:
                if len(near_points) == 1:
                    near_points.append(prev_prev_p)
                new_point = loc.points_avg(near_points) if near_points else prev_p
                distinct_points.append( new_point )
                near_points = []
            prev_prev_p = prev_p
            prev_p = p

        if near_points:
            distinct_points.append( loc.points_avg(near_points) )
        else:
            distinct_points.append( prev_p )

        return self._remove_dupes(distinct_points) if recurse else distinct_points


    def _remove_dupes(self, points):
        unduped_points, near_points = [], []
        prev_p = points[0]

        for p in points:

            if loc.in_threshold( p[0], prev_p[0] ):
                near_points.append(p)
            else:
                if len(near_points) > 0:
                    if len(near_points) == 1:
                        near_points.append(prev_prev_p)
                    near_points = self._distinct_locations( near_points, False )
                elif len(near_points) == 0:
                    near_points.append(prev_p)

                unduped_points.extend( near_points )
                near_points = []

            prev_prev_p = prev_p
            prev_p = p

        if len(near_points) > 0:
            unduped_points.extend( self._distinct_locations(near_points, False) )
        else:
            unduped_points.append(prev_p)

        return unduped_points


    def to_list(self):
        return self.__balls


    def add(self, x, y, color):
        self.__balls.append( Ball(x, y, color) )


    def __str__(self):
        balls = ", ".join( map(str, self.__balls) )
        return "[{}]".format( balls )
