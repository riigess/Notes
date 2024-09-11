Products of Array Discluding Self

Input: [1, 2, 4, 6]
Output: [48, 24, 12, 8]
- nums[1], nums[2], nums[3] == 48
- nums[0], nums[2], nums[3] == 24
- nums[0], nums[1], nums[3] == 12
- nums[0], nums[1], nums[2] == 8

# O(n^2) time solution
SET ret TO EMPTY LIST
iterate 0 ..< len(nums) = i
    SET tot TO 1
    iterate 0 ..< len(nums) = j
        if tot EQUALS 0, break
        if i DOES NOT EQUAL j:
            SET tot TO tot * nums[j]
    APPEND tot TO ret
RETURN ret

# Converting this to be an O(n) time sol'n
SET ret TO EMPTY LIST
