from collections import deque

#使用deque解 但是題目要求使用兩個stack來做
class MyQueue(object):

    def __init__(self):
        self.queue = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.queue.appendleft(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.queue.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[-1]

    def empty(self):
        """
        :rtype: bool
        """
        if not self.queue:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#使用兩個stack來做
class MyQueue(object):

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move_in_to_out()
        return self.out_stack.pop()

    def peek(self) -> int:
        self.move_in_to_out()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def move_in_to_out(self):
        # 只有當 out_stack 為空時，才將 in_stack 的元素全部移到 out_stack
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
