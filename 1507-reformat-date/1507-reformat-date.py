class Solution:
    def reformatDate(self, date: str) -> str:
        month = {"Jan": "1", "Feb": "2", "Mar": "3", "Apr": "4", "May": "5", "Jun": "6", "Jul": "7", "Aug": "8", "Sep": "9", "Oct": "10", "Nov": "11", "Dec": "12"}
        result = [date[-4:], month[date[-8:-5]].zfill(2), date[:-11].zfill(2)]
        return "-".join(result)