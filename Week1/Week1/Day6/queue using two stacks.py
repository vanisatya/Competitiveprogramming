class QueueTwoStacks(object):

    # Implement the enqueue and dequeue methods
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def enqueue(self, item):
        while(self.stack1!=[]):
            self.stack2.append(self.stack1.pop())
        self.stack1.append(item)
        while(self.stack2!=[]):
            self.stack1.append(self.stack2.pop())

    def dequeue(self):
        if(self.stack1==[]):
            raise Exception
        else:
            return self.stack1.pop()