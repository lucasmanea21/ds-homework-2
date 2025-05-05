import random

class Node:
    def __init__(self, value, level):
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    max = 16
    prob = 0.5

    def __init__(self):
        self.head = Node(None, self.max)
        self.level = 0
        self.size = 0

    def __len__(self):
        return self.size

    def random_level(self):
        lvl = 0
        while random.random() < self.prob and lvl < self.max:
            lvl += 1
        return lvl

    def insert(self, value):
        update = [None] * (self.max + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        
        if current is None or current.value != value:
            new_lvl = self.random_level()
            if new_lvl > self.level:
                for i in range(self.level + 1, new_lvl + 1):
                    update[i] = self.head
                self.level = new_lvl

            new_node = Node(value, new_lvl)
            for i in range(new_lvl + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            self.size += 1

    def delete(self, value):
        update = [None] * (self.max + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]
        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

            self.size -= 1

    def search(self, value):
        current = self.head
        
        for i in range(self.level, -1, -1):
            
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        
        return current is not None and current.value == value

    def floor(self, x):
        current = self.head
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value <= x:
                current = current.forward[i]
        return current.value if current and current.value is not None else None

    def ceil(self, x):
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < x:
                
                
                current = current.forward[i]
        current = current.forward[0]
        return current.value if current else None

    def range_query(self, x, y):
        current = self.head
        
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < x:
                current = current.forward[i]
        current = current.forward[0]

        result = []
        
        while current and current.value <= y:
            result.append(current.value)
            current = current.forward[0]
        return result

    def display(self):
        print("Skip List:")
        
        for i in range(self.level + 1):
            current = self.head.forward[i]
            level_vals = []
            
            while current:
                level_vals.append(str(current.value))
                current = current.forward[i]
                
            print(f"Level {i}: {' -> '.join(level_vals)}")
