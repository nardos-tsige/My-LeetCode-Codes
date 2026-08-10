# 144. Binary Tree Preorder Traversal

## Problem Statement

Given the `root` of a binary tree, return the preorder traversal of its nodes' values.

**Preorder Traversal Order:** Visit the root node first, then recursively traverse the left subtree, followed by the right subtree. (Root → Left → Right)

---

## Examples

### Example 1

**Input:**
root = [1,null,2,3]


**Output:**
[1,2,3]


**Explanation:**
1

2
/
3
Preorder traversal: Visit root (1) → left subtree (null) → right subtree (2, then its left child 3)

**Result:** [1, 2, 3]

---

### Example 2

**Input:**
root = [1,2,3,4,5]


**Output:**
[1,2,4,5,3]


**Explanation:**
1
/
2 3
/
4 5
Preorder traversal: 1 → 2 → 4 → 5 → 3

---

---

## Constraints

- The number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

---
