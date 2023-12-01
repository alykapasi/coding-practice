// Leetcode 338 - Counting Bits
// Dec. 1, 2023

int* countBits(int n, int* returnSize) {
    *returnSize = n + 1;
    int* ans = (int*)malloc(sizeof(int) * *returnSize);
    ans[0] = 0;

    for (int i = 1; i < *returnSize; i++) ans[i] = ans[i/2] + (i % 2);

    return ans;
}