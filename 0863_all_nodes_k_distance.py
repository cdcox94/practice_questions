import cProfile
from typing import List, Dict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        path_list = self.recursive_search(node=root, target_val=target.val)

        k_array = []
        self.recursive_get_k_array_from_subtree(target, k, 0, k_array)
        root_distance = len(path_list)
        while len(path_list)>0:
            
            distance = root_distance
            current_node = root
            for i in path_list[0:-1]:
                distance-=1
                if i == 0:
                    current_node = current_node.left
                else:
                    current_node = current_node.right
            if path_list[-1] == 0:
                current_node.left = None
            else:
                current_node.right = None
            if distance == k:
                k_array.append(current_node.val)
                break
            else:
                self.recursive_get_k_array_from_subtree(current_node, k, distance, k_array)
            
            path_list.pop()

        # print(k_array)
        return(k_array)

    def recursive_search(self, node:TreeNode, target_val:int, path_list:List[int]=[]):
        if node == None:
            return None
        elif node.val == target_val:
            return path_list
        else:
            path_list_c = path_list.copy()
            path_list_c.append(0)
            l_attempt = self.recursive_search(node=node.left, target_val=target_val, path_list=path_list_c)
            if l_attempt != None:
                return l_attempt
            path_list_c = path_list.copy()
            path_list_c.append(1)
            r_attempt = self.recursive_search(node=node.right, target_val=target_val, path_list=path_list_c)
            if r_attempt != None:
                return r_attempt
            return None
        
    def recursive_get_k_array_from_subtree(self, node:TreeNode, k:int, current_distance:int, k_array:List[int]):
        if node != None:
            if current_distance == k:
                k_array.append(node.val)
                return
            else:
                self.recursive_get_k_array_from_subtree(node.left, k, current_distance+1, k_array)
                self.recursive_get_k_array_from_subtree(node.right, k, current_distance+1, k_array)
        else:
            return

        