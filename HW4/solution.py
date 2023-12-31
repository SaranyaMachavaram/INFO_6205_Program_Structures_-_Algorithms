
############################################################
#  Write code in this file
# Post this file in Canvas
# Cut and paste the whole file in Leetcode and run. All tests must pass
# Note that you should do 4 times in 225, 235,622 and 641
# TA will run this file 4 times in 225, 235,622 and 641
# All tests must pass for 100
########################################################### 

class ListNode:
    #NOTHING CAN BE CHANGED HERE
    def __init__(self, val = 0, next= None):
        self.val = val
        self.next = next
         
            
############################################################
#  class  Slist
###########################################################   
class Slist():
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._first = None
        self._last = None
        self._len = 0 
        
    #############################
    # WRITE All public functions BELOW
    # YOU CAN HAVE ANY NUMBER OF PRIVATE FUNCTIONS YOU WANT
    #############################
  
  
############################################################
#  class  MyStack
#225. Implement Stack using Queues

#https://leetcode.com/problems/implement-stack-using-queues
########################################################### 
class MyStack:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()
    def push(self, x: int) -> None:
        newnode = ListNode(x)
        if self._s._len == 0:
            self._s._first = newnode
            self._s._last = newnode
        else:
            newnode.next=self._s._first
            self._s._first = newnode
        self._s._len += 1

    def pop(self) -> int:
        if self._s._len == 0:
            return None
        val = self._s._first.val
        self._s._first = self._s._first.next
        self._s._len -= 1
        return val

    def top(self) -> int:
        if self._s._len == 0:
            return None
        return self._s._first.val

    def empty(self) -> bool:
        return self._s._len == 0


############################################################
#  class  MyQueue
#232. Implement Queue using Stacks

# https://leetcode.com/problems/implement-queue-using-stacks/
########################################################### 
class MyQueue:
    def __init__(self):
        #NOTHING CAN BE CHANGED HERE
        self._s = Slist()

    def push(self, x: int) -> None:
        newnode = ListNode(x)
        if self._s._len == 0:
            self._s._first = newnode
            self._s._last = newnode
        else:
            self._s._last.next=newnode
            self._s._last = newnode
        self._s._len += 1

    def pop(self) -> int:
        if self._s._len == 0:
            return None
        val = self._s._first.val
        self._s._first = self._s._first.next
        self._s._len -= 1
        return val

    def peek(self) -> int:
        if self._s._len == 0:
            return None
        return self._s._first.val

    def empty(self) -> bool:
        return self._s._len == 0
############################################################
#  MyCircularQueue
# 622. Design Circular Queue
# https://leetcode.com/problems/design-circular-queue/
########################################################### 

class MyCircularQueue:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
 
    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        newnode = ListNode(value)
        if self.isEmpty():
            self._s._front = newnode
            self._s._last = newnode
        else:
            self._s._last.next = newnode
            self._s._last = newnode
            self._s._last.next=self._s._first
        self._s._len += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self._s._front = self._s._front.next
        self._s._last.next=self._s._front
        self._s._len -= 1
        return True
        
    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self._s._front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self._s._last.val

    def isEmpty(self) -> bool:
        return self._s._len == 0

    def isFull(self) -> bool:
        return self._s._len == self._K

############################################################
#  MyCircularDeque
#641. Design Circular Deque
#https://leetcode.com/problems/design-circular-deque

###########################################################  
class MyCircularDeque:
    def __init__(self, k: int):
        #NOTHING CAN BE CHANGED HERE
        self._K = k 
        self._s = Slist()
        
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newnode = ListNode(value)
        if self.isEmpty():
            self._s._first = newnode
            self._s._last = newnode
        else:
            newnode.next = self._s._first
            self._s._first = newnode
            self._s._last.next=self._s._first
        self._s._len += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newnode = ListNode(value)
        if self.isEmpty():
            self._s._first = newnode
            self._s._last = newnode
        else:
            self._s._last.next = newnode
            self._s._last = newnode
            self._s._last.next=self._s._first
        self._s._len += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        if self._s._len == 1:
            self._s._first = self._s._last = None
        else:
            self._s._first = self._s._first.next
            self._s._last.next=self._s._first
        self._s._len -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        if self._s._len == 1:
            self._s._first = self._s._last = None
        else:
            current = self._s._first
            while current.next != self._s._last:
                current = current.next
            current.next = None
            self._s._last = current
            self._s._last.next=self._s._first
        self._s._len -= 1
        return True

    def getFront(self) -> int:
        return self._s._first.val if self._s._first else -1

    def getRear(self) -> int:
        return self._s._last.val if self._s._last else -1

    def isEmpty(self) -> bool:
        return self._s._len == 0

    def isFull(self) -> bool:
        return self._s._len == self._K

