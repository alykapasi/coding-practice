// Leetcode 338 - Reverse Bits
// Dec. 1, 2023

#include <stdlib.h>

uint32_t reverseBits(uint32_t n) {
    uint32_t ans = 0;
    for (int i = 0; i < 32; i++) {
        ans <<= 1;
        if (n & 1) ans |= 1;
        n >>= 1;
    }

    return ans;
}