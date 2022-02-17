class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        '''
        Two players: A and B
        1. Move takes place only when the cell is empty == ' '
        2. Sequence of char placement: X -> O -> X -> ... 
        
        3. Win when X/O fills a row, col or diagonal
            Checked: winner for odd count of moves is A, B otherwise
            return A/B
        4. Draw when game finishes with no win(/or lose of opponent) and moves == 9
            return 'Draw'
        5. Pending if count of moves < 9
        
        Questions:
        1. Do any of the moves repeat in a given input
        2. Are there any negative values or other than 'X' or 'O' values in input?
        
        For positions:
        0 1 2
        3 4 5
        6 7 8
        win_cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        '''
        win_cases = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        recorded = [None]*9
        players, curr = ['A', 'B'], 0
        for row, col in moves:
            recorded[row*3+col] = players[curr]
            for pos1, pos2, pos3 in win_cases:
                if recorded[pos1] == recorded[pos2] == recorded[pos3] != None:
                    return recorded[pos1]
            curr ^= 1
        if len(moves) == 9:
            return 'Draw'
        return "Pending"
        
        
        
        