class Solution:
    def flipAndInvertImage(self, image):
        # Warm-up for ompleting C0
        # Approach 2
        # 1. Flip the image horizontally
        # 2. In step 1, complete inverse as well
        middle = len(image[0]) % 2
        for row in range(len(image)):
            for col in range(len(image[0])//2 + middle):
                image[row][col], image[row][~col] = 1-image[row][~col], 1-image[row][col]
        return image
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # row, col = 0, 0
        # while row < len(image):
        #     col = 0
        #     while col < (len(image[row]) + 1)//2:
        #         image[row][col], image[row][~col] = image[row][~col] ^ 1, image[row][col] ^ 1
        #         col += 1
        #     row += 1
        # return image
    
        '''
        Time complexity: O(N) - N is total number of elements in image
        Space complexity: O(1)
        '''