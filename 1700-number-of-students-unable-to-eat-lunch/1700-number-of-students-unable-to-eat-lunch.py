class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = {0:0, 1:0}
        for el in students:
            count[el] += 1
            
        i = 0
        while i < len(students) and count[sandwiches[i]]:
            count[sandwiches[i]] -= 1
            i += 1
        return len(students) - i
        