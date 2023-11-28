// Leetcode 217 - Contains Duplicate
// Nov. 25, 2023

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// need to implement a hash_table
// o(n2) times out leetcode

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define HASH_SIZE 10000

typedef struct hash_node {
    int key;
    struct hash_node* next;
} hash_node;

hash_node* hash_table[HASH_SIZE];

unsigned int hash_code(int key) {
    return (unsigned int) key % HASH_SIZE;
}

bool insert(int key) {
    unsigned int hash_index = hash_code(key);
    hash_node* new_node = (hash_node*) malloc(sizeof(hash_node));
    if (new_node == NULL) {
        return false; // Allocation failed
    }
    new_node->key = key;
    new_node->next = NULL;

    if (hash_table[hash_index] == NULL) {
        hash_table[hash_index] = new_node;
    } else {
        hash_node* temp = hash_table[hash_index];
        while (temp != NULL) {
            if (temp->key == key) {
                free(new_node);
                return true; // Duplicate found
            }
            temp = temp->next;
        }
        new_node->next = hash_table[hash_index];
        hash_table[hash_index] = new_node;
    }
    return false;
}

void free_hash_table() {
    for (int i = 0; i < HASH_SIZE; i++) {
        hash_node* temp = hash_table[i];
        while (temp != NULL) {
            hash_node* toDelete = temp;
            temp = temp->next;
            free(toDelete);
        }
    }
}

bool containsDuplicate(int* nums, int numsSize) {
    for (int i = 0; i < HASH_SIZE; i++) {
        hash_table[i] = NULL;
    }

    for (int i = 0; i < numsSize; i++) {
        if (insert(nums[i])) {
            free_hash_table();
            return true;
        }
    }

    free_hash_table();
    return false;
}
