# Algorithms
## Binary Search
Speed: O(log(n))
Memory: O(1)
```python
class BinarySearch:
    def search(arr:list[int], target:int) -> int:
    #This could also be written as a while loop, and would be preferred because of recursive depth errors in Python
        def run(high:int, low:int=0) -> int:
            mid = (high + low) // 2
            if arr[mid] > target:
                return run(mid - 1, low)
            elif arr[mid] < target:
                return run(high, mid + 1)
            if arr[mid] == target:
                return mid
            elif arr[low] == target:
                return low
            elif arr[high] == target:
                return high
        return run(len(arr) - 1)

arr = [1, 2, 3, 5 7, 10, 11, 12, 22, 55]
bs = BinarySearch()
ret = bs.search(arr, 55)
assert ret == len(arr) - 1
print(f"Found index:", ret)
```

## Depth First Search
- O(n), typically
- Concept: Explore first, then return data & back track
```python
class TreeNode:
    def __init__(self, data:int = 0, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

#Post-order Traversal
def left_postorder_dfs(root) -> list[int]:
    if not isinstance(root, TreeNode):
        return []
    return left_postorder_dfs(root.left) + left_postorder_dfs(root.right) + [root.data]

#Another Post-order Traversal
def right_postorder_dfs(root) -> list[int]:
    if not isinstance(root, TreeNode):
        return []
    return right_postorder_dfs(root.right) + right_postorder_dfs(root.left) + [root.data]

#In-order Traversal
def left_inorder_dfs(root) -> list[int]:
	if not isinstance(root, TreeNode):
		return []
	return left_inorder_dfs(root.left) + [root.data] + left_inorder_dfs(root.right)

#Another inorder traversal
def right_inorder_traversal(root) -> list[int]:
	if not isinstance(root,TreeNode):
		return []
	return right_inorder_traversal(root.right) + [root.data] + right_inorder_traversal(root.left)

#Preorder Traversal
def left_preorder_traversal(root) -> list[int]:
	if not isinstance(root, TreeNode):
		return []
	return [root.data] + left_preorder_traversal(root.left) + left_preorder_traversal(root.right)

#Another Preorder Traversal
def right_preorder_traversal(root) -> list[int]:
	if not isinstance(root, TreeNode):
		return []
	return [root.data] + right_preorder_traversal(root.right) + right_preorder_traversal(root.left)

root = TreeNode(data=5,
    left=TreeNode(data=6,
        left=TreeNode(data=7),
        right=TreeNode(data=8)),
    right=TreeNode(data=9,
        left=TreeNode(data=10),
        right=TreeNode(data=11)))
print("left_postorder_dfs:", left_postorder_dfs(root))
```

## Breadth First Search
- Concept: Gather data, then traverse
### With a Queue
```python
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    if root is None:
        return
    q = [ root ]
    while len(q) > 0:
        temp = q.pop(0)
        print(temp.data, end=" ")
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printLevelOrder(root)
```

### Functionally
```python
class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

def printLevelOrder(root):
    h = height(root)
    for i in range(1, h+1):
        printCurrentLevel(root, i)

def printCurrentLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printCurrentLevel(root.left, level-1)
        printCurrentLevel(root.right, level-1)

def height(node):
    if node is None:
        return 0
    else:
        lheight = height(node.left)
        rheight = height(node.right)
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    printLevelOrder(root)
```

## Sliding Window
```python
data = [1, 2, 3, 1]
k = 3

def containsDuplicate(a:list[int], k:int) -> bool:
    hs = set()
    L, r = 0, len(a) - 1

    for R in range(len(nums)):
        if R - L > k:
            hs.remove(nums[L])
            L += 1
        if nums[R] in window:
            return True
        hs.add(nums[R])

    return False
```

# Patterns
## Prefix Sum Pattern
- Running sums...
```python
arr = [i for i in range(1, 8)] #list of 1...7 (inclusive)
prefix_sum = [arr[0]]
for i in range(len(arr) - 1):
    prefix_sum.append(prefix_sum[i] + arr[i+1])
```

## Two Pointers Pattern
- Two pointers (usually left and right, or i and j) that move towards or away from each other depending on the problem
```python
def is_palindrome(a:str) -> bool:
    left, right = 0, len(a) - 1
    for i in range(len(a) // 2):
        if a[left] == a[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
```
