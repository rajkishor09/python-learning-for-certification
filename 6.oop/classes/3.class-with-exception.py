class QueueError(IndexError):
    pass # placeholder for future code

class Queue(QueueError):
    def __init__(self):
        self.queue = []
    
    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) > 0:
            elem = self.queue[-1]
            del self.queue[-1]
            return elem
        else:
            raise QueueError

# que = Queue()
# que.put(1)
# que.put("dog")
# que.put(False)
# try:
#     for i in range(4):
#         print(que.get())
# except:
#     print("Queue error")

class SuperQueue(Queue):
    def isEmpty(self):
        return len(self.queue) == 0
    
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(5):
    if not que.isEmpty():
        print(que.get())
    else:
        print("Queue empty")
