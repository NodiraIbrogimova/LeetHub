class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Questions to ask: 
        # Should L and W be integer, or can be float numbers?
        # If prime numbers are included, then the area is [area, 1]
        # area = 13
        width = math.ceil(area**0.5)
        while area % width > 0:
            width -= 1
        length = max(width, area//width)
        return [length, area//length]