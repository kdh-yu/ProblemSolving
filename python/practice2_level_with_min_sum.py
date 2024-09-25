from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Tree:
    def __init__(self, dic):
        i_root = 0
        if i_root not in dic:
            return
        self.root = TreeNode(dic[i_root])
        q = deque([(i_root, self.root)])
        while q:
            i_curr, curr = q.popleft()
            i_left = i_curr * 2 + 1
            if i_left in dic:
                child = TreeNode(dic[i_left])
                q.append((i_left, child))
                curr.left = child
            i_right = i_curr * 2 + 2
            if i_right in dic:
                child = TreeNode(dic[i_right])
                q.append((i_right, child))
                curr.right = child

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def level_with_min_sum(node):
    level_sum = {}
    def dfs(node_cur, level=0, vsum=0):
        vsum += node_cur.val
        if node_cur.left is None and node_cur.right is None:
            if not level_sum.get(level):
                level_sum[level] = float('inf')
            level_sum[level] = min(level_sum[level], vsum)
        else:
            dfs(node_cur.left, level+1, vsum)
            dfs(node_cur.right, level+1, vsum)
    dfs(node)
    return min(level_sum, key=level_sum.get)
    

if __name__ == '__main__':
    nodes = {0:9, 1:2, 2:3, 5:1, 6:5}
    T = Tree(nodes)
    result = level_with_min_sum(T.root)
    print(result)

