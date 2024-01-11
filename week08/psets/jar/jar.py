# Cookie Jar


class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Expected positive int or float")
        self.__capacity = capacity
        self.__size = 0

    def __str__(self):
        return "🍪" * self.size
    
    def deposit(self, n):
        if type(n) not in [int, float]:
            raise ValueError("Expected int or float")
        if not n > 0:
            raise ValueError("Expected positive int or float")
        self.size += n

    def withdraw(self, n):
        if type(n) not in [int, float]:
            raise ValueError("Expected int or float")
        if not n > 0:
            raise ValueError("Expected positive int or float")
        self.size -= n

    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, c):
        if not (isinstance(c, int) or isinstance(c, float)):
            raise ValueError("Expected int or float")
        if c < 0:
            raise ValueError("Expected positive int or float")
        self.__capacity = c

    @property
    def size(self):
        return self.__size
    
    @size.setter
    def size(self, s):
        if not (isinstance(s, int) or isinstance(s, float)):
            raise ValueError("Expected int or float")
        if s < 0:
            raise ValueError("Expected positive int or float")
        elif s > self.capacity:
            raise ValueError(f"Size can't exceed cookie jar's capacity of {self.capacity}")
        self.__size = s