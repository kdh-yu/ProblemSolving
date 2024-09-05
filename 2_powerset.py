# Problem
# Write a method to return all subsets of a set.

def power_set(A: list[int]) -> list[list[int]]:
    output = []
    for i in range(1<<len(A)):
        subset = []
        for j in range(len(A)):
            if i & (1<<j):
                print(i, (1<<j))
                subset.append(A[j])
        output.append(subset)
    return output

if __name__ == '__main__':
    lst = [1,2,3]
    out = power_set(lst)
    print(out)