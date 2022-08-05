from BinarySearchTree import BinarySearchTree
from Interfaces import Set

class BinarySearchTreeWithDuplication(Set):
    def __init__(self, nil=None):
        self.binaryTree = BinarySearchTree()
        self.n = 0
        
    def size(self) -> int:
        return self.n 

    def find(self, x: object) -> object:
        return self.binaryTree.find(x)

    def add(self, key : object, value : object) -> bool:
        bookTitles = self.find(key)
        isAddedDupe = False

        if bookTitles is None:
          isAddedDupe = self.binaryTree.add(key, [value])
        else:
          bookTitles.append(value)
          matchingKeyNode = self.binarySearch(key)
          matchingKeyNode.v = bookTitles
          isAddedDupe = False
          
        return isAddedDupe

    def remove(self, x : object) -> bool:
        isRemovedNode = self.binaryTree.remove(x)
        print(f"isRemovedNode: {isRemovedNode}.")
        return isRemovedNode

    def binarySearch(self, key : object) -> object:
      curr = self.binaryTree.r
      while curr is not None:
        if key == curr.x:
          return curr
        elif key < curr.x:
          curr = curr.left
        else:
          curr = curr.right
      return None

# q = BinarySearchTreeWithDuplication()
# q.add(1, "a")
# q.add(1, "b")
# q.add(2, "c")
# q.add(3, "d")
# q.add(3, "e")

# print(q.find(1))
# print(q.find(2))
# print(q.find(3))