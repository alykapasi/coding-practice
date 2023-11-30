// Leetcode 371 - Sum of Two Integers
// Nov. 29, 2023

int getSum(int a, int b) {
    unsigned c;
    while (b) {
        c = a & b;
        a ^= b;
        b = c << 1;
    }
    return a;
}