
#stack: LIFO structure
stack=[]
stack.append("umar")
stack.append("imran")
stack.append("ali")
stack.append("ahmad")
#print(stack)
#print (stack.pop())

from collections import deque
#queue: FIFO
queue=deque()
queue.append("Ali")
queue.append("Umar")
queue.append("Ahmad")
queue.append("imran")
print(queue.popleft())