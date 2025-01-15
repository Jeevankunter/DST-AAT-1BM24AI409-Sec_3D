class QueueUsingTwoStacks:
    def __init__(self):
        self.stack1 = []  
        self.stack2 = []  

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.stack2.pop()

    def peek(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    queue = QueueUsingTwoStacks()
    queries = int(data[0])

    for i in range(1, queries + 1):
        query = data[i].split()
        if query[0] == '1':  
            queue.enqueue(int(query[1]))
        elif query[0] == '2':  
            queue.dequeue()
        elif query[0] == '3':
            print(queue.peek())
