class jar:
    def __init__(self, capacity = 12):
        self.capacity = capacity
        self.n = 0
    def __str__(self):
        cookies = ""
        for _ in range(self.n):
            cookies = f"{cookies}🍪"
        return cookies
    def deposit(self, n):
        if n + self.n > self.capacity:
            raise ValueError("capacity exceeded")
        else:
            self.n = n + self.n
    def withdraw(self, n):
        if self.n - n < 0:
            raise ValueError("Not enough cookies")
        else:
            self.n = self.n - n
    @property
    def capacity(self):
        return self._capacity
    
    @property
    def size(self):
        return self.n
    
    @capacity.setter
    def capacity(self, cap):
        if cap < 0:
            raise ValueError("Capacity must be positive")
        else:
            self._capacity = cap



    
x = jar(10)
x.deposit(2)
x.deposit(2)
y = x.size
print(y)
print(x)