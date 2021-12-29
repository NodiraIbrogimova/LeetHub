class Solution:
    def checkRecord(self, s: str) -> bool:
        # Warm-up
        print('\nstr: ', s)
        absenceCount, lateCount = 2, 3
        for att in s:
            if att == 'A':
                absenceCount -= 1
                if absenceCount == 0:
                    return False
                lateCount = 3
            elif att == 'L':
                lateCount -= 1
                if lateCount == 0:
                    return False
            else:
                lateCount = 3
        
        return True
        
        
        # Approach 2
        count_absent = 0
        count_late = 0
        for record in s:
            if record == 'A':
                count_absent += 1
                if count_absent > 1:
                    return False
                count_late = 0
            elif record == 'L':
                count_late += 1
                if count_late > 2:
                    return False
            else:
                count_late = 0
        return True
        
        # Approach 1: Using hashmap
        # Time: O(n)
        # Space: O(1)
        records = {'A':0, 'L':0, 'P':0}
        records[s[0]] += 1
        prev = 0
        late_count = 0
        curr = 1
        while curr < len(s) and late_count < 2:
            records[s[curr]] += 1
            if s[curr] == 'L' and s[prev] == 'L':
                late_count += 1
            else:
                prev = curr
                late_count = 0
            curr += 1
        return records['A'] < 2 and late_count < 2