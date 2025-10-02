class listNode:
    def __init__(self, value, next) -> None:
        self.value = value
        self.next = next

    def list(self) -> None:
        print(self.value, end="")
        if type(self.next) is listNode:
            print(" -> ", end="")
            self.next.list()

    def add_to_end(self, value) -> None:
        if type(self.next) is listNode:
            self.next.add_to_end(value=value)
        else:
            self.next = listNode(value=value, next=None)

a = listNode(value=1, next=None)
for i in range(2, 11):
    a.add_to_end(value=i)

a.list()