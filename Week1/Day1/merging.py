import unittest
from operator import itemgetter

def merge_ranges(meetings):
    if len(meetings) <= 1:
        return meetings

    meetings = sorted(meetings, key=itemgetter(0))
    pre = [meetings[0]]
    for (f, l) in meetings:
        (s, e) = pre[-1]
        if f <= e:
            if e <= l:
                e = l
            pre[-1] = (s, e)
        else:
            pre.append((f, l))
    return pre


