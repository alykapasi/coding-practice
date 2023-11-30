// Leetcode 11 - Container with Most Water
// Nov. 29, 2023

int maxArea(int* height, int heightSize) {
    int ans = 0, l = 0, r = heightSize - 1;
    while (l < r) {
        int area = (height[l] < height[r] ? height[l] : height[r]) * (r - l);
        ans = ans > area ? ans : area;
        if (height[l] < height[r]) l++;
        else r--;
    }
    return ans;
}