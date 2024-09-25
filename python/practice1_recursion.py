# Problem
# Design an algorithm to print all permutations of a string. 
# For simplicity, assume all characters are unique.

import sys

def permute(s: str) -> list[str]:
    output = []
    visited = [0] * len(s)
    def backtrack(tmp):
        if len(tmp) == len(s):
            output.append(tmp)
            return
        for i in range(len(s)):
            if not visited[i]:
                visited[i] = True
                backtrack(s[i]+tmp)
                visited[i] = False
    backtrack('')
    return output

if __name__ == '__main__':
    out = permute(sys.argv[1])
    print(out)