class queue:
    def __init__(self):
        self.list = []

    # 入队
    def enqueue(self, item):
        self.list.append(item)

    # 出队
    def dequeue(self):
        self.list.pop(0)

    # 判断是否为空
    def isempty(self):
        return len(self.list) == 0

    # 队列长度
    def length(self):
        return len(self.list)

    # 打印队列
    def print_queue(self):
        print(self.list)

    # 从队头元素开始打印队列
    def print_element(self):
        for i in self.list:
            print(i)


q = queue()
print('队列是否为空：', q.isempty())
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')
q.enqueue("d")
q.print_queue()
q.dequeue()
q.print_element()
print('队列长度为：', q.length())
