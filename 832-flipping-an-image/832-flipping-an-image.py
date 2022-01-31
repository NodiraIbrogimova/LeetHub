class Solution:
    def flipAndInvertImage(self, image):
        row, col = 0, 0
        while row < len(image):
            col = 0
            while col < (len(image[row]) + 1)//2:
                image[row][col], image[row][~col] = image[row][~col] ^ 1, image[row][col] ^ 1
                col += 1
            row += 1
        return image
    
        '''
        Time complexity: O(N) - N is total number of elements in image
        Space complexity: O(1)
        '''