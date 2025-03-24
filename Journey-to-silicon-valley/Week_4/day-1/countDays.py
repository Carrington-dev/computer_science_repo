# 3169. Count Days Without Meetings
class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        all_days = set()
        all_meeting_days = set()
        for i in range(len(meetings)):
            for j in range(meetings[i][0], meetings[i][1] + 1):
                all_meeting_days.add(j)
        
        for day in range(1, days + 1):
            all_days.add(day)
        
        days_not_used = all_days - all_meeting_days
        return len(list(days_not_used))
