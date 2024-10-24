# Definition for a binary tree node.
from typing import List, Optional

# To switch a sorted array to BST we find the middle as that will be the root node. We then repeat the function
# for the left and right half of the array. This way we ensure that the left subtree of
# a node contains only nodes with keys less than the node's key and the right subtree of a
# node contains only nodes with keys greater than the node's key.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base condition
        if not nums:
            return None
        # set the middle node
        mid = len(nums)//2
        # Initialise root node with value same as nums[mid]
        root = TreeNode(nums[mid])
        # Assign left subtrees as the same function called on left subranges
        root.left = self.sortedArrayToBST(nums[:mid])
        # Assign right subtrees as the same function called on right subranges
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root
            
        