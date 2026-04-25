"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key= lambda x: x.start) # sort based on start time

        q = []


        meetingRooms = 0

        for interval in intervals:
            while q and interval.start >= q[0]:
                heapq.heappop(q)

            heapq.heappush(q,interval.end)

            meetingRooms = max(meetingRooms, len(q))
        
        return meetingRooms
            

