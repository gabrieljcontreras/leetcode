"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals]) #declare start array with every start interval sorted
        end = sorted([i.end for i in intervals])#declare end array with every end interval sorted

        res, count = 0,0 #set result and count to 0
        s, e = 0,0 #pointers to help us iterate and compare

        while s < len(intervals):  #iterate the start time through intervals
            if start[s] < end[e]: #start time < end time means meeting is running, increase count move s 
                s += 1
                count +=1
            else: #end time < start time means meating ended, decrease count move e
                e += 1
                count -=1
            res = max(res, count) # get the max count as the result
        return res 