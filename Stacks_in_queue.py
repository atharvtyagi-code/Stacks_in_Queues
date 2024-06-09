class Stack_n_Queue():
    def __init__(self):
        self.stack = []
        self.queue = []


    def push(self):
        num = int(input("How many datas in the list: "))

        for i in range(num):
            n = input("Add a data in the list: ")
            self.stack.append(n)

        print(self.stack)

    def pop(self):
        if len(self.stack) == 0:
            print("There is nothing to remove from the list")

        else:
            self.stack.pop(-1)
            print(self.stack)

    def peek(self):
        if len(self.stack) == 0:
            print("There is nothing to remove from the list")

        else:
            print(self.stack[-1])

    def isEmpty(self):
        if len(self.stack) == 0:
            print("The first list is empty!")

        else:
            print("The first list is full!")

    def size(self):
        print(len(self.stack))



    def enqueue(self):
        num = int(input("How many datas in the list: "))

        for i in range(num):
            n = input("Add a data in the list: ")
            self.queue.append(n)

        print(self.queue)

    def dequeue(self):
        if len(self.queue) == 0:
            print("There is nothing to remove from the list")

        else:
            self.queue.pop(0)
            print(self.queue)

    def look(self):
        if len(self.queue) == 0:
            print("There is nothing to remove from the list")

        else:
            print(self.queue[0])

    def empty(self):
        if len(self.queue) == 0:
            print("The second list is empty!")

        else:
            print("The second list is full!")

    def length(self):
        print(len(self.queue))

stack_in_queue = Stack_n_Queue()

print("First list: ")
stack_in_queue.push()
stack_in_queue.pop()
stack_in_queue.peek()
stack_in_queue.isEmpty()
stack_in_queue.size()

print()

print("Second list: ")
stack_in_queue.enqueue()
stack_in_queue.dequeue()
stack_in_queue.look()
stack_in_queue.empty()
stack_in_queue.length()