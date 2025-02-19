from doubly_linked_list import ListNode
from doubly_linked_list import DoublyLinkedList

class LRUCache:
  def __init__(self, limit=10):
    self.storage = {}
    self.order_of_use = []

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the top of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key in self.storage:
        for i in range(0, len(self.order_of_use)):
            if self.order_of_use[i] == key:
                swapped_element = self.order_of_use[0]
                self.order_of_use[0] = self.order_of_use[i]
                self.order_of_use[i] = swapped_element
                break
        return self.storage[key]
    return None
  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if len(self.storage) == 10:
        self.storage[self.order_of_use[-1]] = None
        self.order_of_use.remove(-1)
    if key in self.storage:
        for i in range(0, len(self.order_of_use)):
            if self.order_of_use[i] == key:
                swapped_element = self.order_of_use[0]
                self.order_of_use[0] = self.order_of_use[i]
                self.order_of_use[i] = swapped_element
                break
    else:
        self.order_of_use.insert(0, key)
    self.storage[key] = value
