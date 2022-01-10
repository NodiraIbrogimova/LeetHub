class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # Approach 2
        # the number of U with D, and L with R should be equal for robot to come back to the original position
        move_map = {'L': 0, 'R': 0, 'U': 0, 'D':0}
        for move in moves:
            move_map[move]+=1
        return move_map['R'] == move_map['L'] and move_map['U'] == move_map['D']
        
        # Approach 1
        # Check the axis positions and return result accordingly
        move_map = {'L': -1, 'R': 1, 'U': 1, 'D':-1}
        origin = [0,0]
        for move in moves:
            if move == 'R' or move == 'L':
                origin[0]+=move_map[move]
            else:
                origin[1]+=move_map[move]
        return origin == [0,0]