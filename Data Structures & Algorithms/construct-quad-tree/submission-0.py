"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def univalue_grid(self, grid, bounding_coords):
        tl_row, tl_col, br_row, br_col = bounding_coords
        val = grid[tl_row][tl_col]
        for i in range(tl_row, br_row + 1):
            for j in range(tl_col, br_col + 1):
                if grid[i][j] != val:
                    return False
        return True

    def construct(self, grid: List[List[int]], bounding_coords=[]) -> 'Node':
        if not bounding_coords:
            tl_row, tl_col = 0, 0
            br_row, br_col = len(grid) - 1, len(grid[0]) - 1
            bounding_coords = [tl_row, tl_col, br_row, br_col]

        tl_row, tl_col, br_row, br_col = bounding_coords
        if tl_row > br_row or tl_col > br_col:
            return None

        if self.univalue_grid(grid, bounding_coords):
            root = Node(grid[tl_row][tl_col], True, None, None, None, None)
            return root
        
        mid_col = (tl_col + br_col + 1) // 2
        mid_row = (tl_row + br_row + 1) // 2
        # Top Left subgrid
        tl_Node = self.construct(grid, [tl_row, tl_col, mid_row-1, mid_col-1])
        # Top Right subgrid
        tr_Node = self.construct(grid, [tl_row, mid_col, mid_row-1, br_col])
        # Bottom Left subgrid
        bl_Node = self.construct(grid, [mid_row, tl_col, br_row, mid_col-1])
        # Bottom Right subgrid
        br_Node = self.construct(grid, [mid_row, mid_col, br_row, br_col])

        root = Node(0, False, tl_Node, tr_Node, bl_Node, br_Node)
        return root


        
        
