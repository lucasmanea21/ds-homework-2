import os
import random

def save_file(path, operations):
    with open(path, "w") as f:
        f.write(f"{len(operations)}\n")
        
        for op in operations:
            f.write(" ".join(map(str, op)) + "\n")

def sorted_inserts(n):
    return [(1, i) for i in range(n)]

def random_operations(n, val_range=(0, 10**9)):
    operations = []
    inserted = set()
    
    for _ in range(n):
        t = random.choices([1, 2, 3, 4, 5, 6], weights=[40, 15, 15, 10, 10, 10])[0]
        x = random.randint(*val_range)
        if t == 1:
            inserted.add(x)
            operations.append((1, x))
        elif t == 2 and inserted:
            x = random.choice(list(inserted))
            inserted.remove(x)
            operations.append((2, x))
        elif t in [3, 4, 5]:
            operations.append((t, x))
        elif t == 6:
            y = random.randint(x, min(val_range[1], x + 1000))
            operations.append((6, x, y))
            
    return operations

def repeated_insert_delete(n, val=123456):
    return [(1, val) if i % 2 == 0 else (2, val) for i in range(n)]

def sparse_inserts(n):
    return [(1, i * 1_000_000) for i in range(n)]

def heavy_ranges(n, data_range=(0, 10**6)):
    operations = [(1, i) for i in range(data_range[1])]
    for _ in range(n):
        operations.append((6, data_range[0], data_range[1]))
    return operations

def dense_ranges(n, max_val=100_000):
    operations = [(1, i) for i in range(max_val)]
    for _ in range(n):
        x = random.randint(0, max_val - 100)
        operations.append((6, x, x + 100))
    return operations

def search_fails(n, val_range=(10**9, 2 * 10**9)):
    return [(3, random.randint(*val_range)) for _ in range(n)]

def generate_all():
    os.makedirs("tests", exist_ok=True)


    tests = {
        "sorted_insertions.in": sorted_inserts(100_000),
        # "random_operations.in": random_operations(1_000_000),
        "random_operations.in": random_operations(200_000),
        "repeated_insert_delete.in": repeated_insert_delete(100_000),
        "sparse_insertions.in": sparse_inserts(100_000),
        "heavy_range_queries.in": heavy_ranges(50),
        "dense_range_queries.in": dense_ranges(1000),
        "search_misses.in": search_fails(100_000),
    }

    for name, data in tests.items():
        save_file(f"tests/{name}", data)

    print("Tests generated in 'tests/' folder")

if __name__ == "__main__":
    generate_all()
