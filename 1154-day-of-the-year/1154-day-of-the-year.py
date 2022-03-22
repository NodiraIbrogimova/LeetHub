class Solution:
    def dayOfYear(self, date: str) -> int:
        '''
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        find days until the beginning of each month via prefix sum
        1. Check if this year a leap year
        2. Find the month -> int(date[5:7])
        2. Check how many days are needed to come to this month
        3. Add the days until this day from current month
        '''
        months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
        year, month, day = map(int, date.split('-'))
        first_year = 1900
        year_difference = year - first_year
        if year_difference > 0 and year_difference % 4 == 0: months[2] += 1
        for i in range(1, len(months)): months[i] += months[i-1]
        return months[month-1] + day