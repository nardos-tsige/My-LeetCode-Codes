/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        //helper function to check if two subtrees are mirrors
        function<bool(TreeNode*, TreeNode*)> s = [&](TreeNode* a, TreeNode* b) -> bool {
            if (!a && !b) return true;
            if (!a || !b) return false;
            return (a->val == b->val) && 
                   s(a->left, b->right) && 
                   s(a->right, b->left);
        };
        
        return s(root->left, root->right);
    }
};
