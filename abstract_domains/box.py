from abstract_domains.interval import Interval
from abstract_domains.abstract_domain import AbstractDomain
from typing import List
import numpy as np


def _get_sub_vertices(intervals):
    if len(intervals) == 1:
        return [[intervals[0].lower], [intervals[0].upper]]
    res = []
    sub = _get_sub_vertices(intervals[1:])
    for s in sub:
        res.append([intervals[0].lower] + s)
        res.append([intervals[0].upper] + s)
    return res

class Box(AbstractDomain):
    def __init__(self, intervals: List[Interval]):
        self.intervals = intervals

    def get_affine_transform(self, transformation: np.ndarray, bias: np.ndarray):
        res = []
        for i, interval in enumerate(self.intervals):
            coefs = transformation[i,:].reshape(len(self.intervals))
            lower = bias[i]
            upper = bias[i]
            for j, c in enumerate(coefs):
                if c > 0:
                    upper += c * self.intervals[j].upper
                    lower += c * self.intervals[j].lower
                else:
                    upper += c * self.intervals[j].lower
                    lower += c * self.intervals[j].upper
            res.append(Interval(lower, upper))
        return Box(res)


    def get_relu(self):
        res = []
        for interval in self.intervals:
            res.append(Interval(max([interval.lower, 0]), max([interval.upper, 0])))
        return Box(res)



    def get_vertices(self):
        return _get_sub_vertices(self.intervals)


