def bowling(nums: list[int]) -> int:
    score = 0
    idx = 0
    while idx < len(nums):
        if idx == len(nums)-1:
            if nums[idx] >= 0:
                score += nums[idx]
            idx += 1
        elif nums[idx] < 0:
            if nums[idx+1] < 0:
                score += nums[idx] * nums[idx+1]
                idx += 1
        elif nums[idx] + nums[idx+1] < nums[idx] * nums[idx+1]:
            score += nums[idx] * nums[idx+1]
            idx += 1
        else:
            score += nums[idx]
        idx += 1
    return score

if __name__ == "__main__":
    # Example 1
    nums = [-3,1,1,9,9,2,-5,-5]
    out = bowling(nums)
    print(out)

    # Example 2
    nums = [-1,1,1,1,9,9,3,-3,-5,2,2]
    out = bowling(nums)
    print(out)
