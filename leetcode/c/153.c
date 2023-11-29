// Leetcode 153 - Find Minimum in Rotated Sorted Array
// Nov. 28, 2023

int findMin(int* nums, int numsSize) {
    int l = 0, r = numsSize - 1, m;
    while (l < r) {
        m = (l+r)/2;
        if (nums[r] < nums[m]) l = m+1;
        else r = m;
    }
    return nums[r];
}