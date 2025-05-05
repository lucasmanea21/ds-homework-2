import time
import os
from structures.skip_list import SkipList
from structures.splay_tree import SplayTree

structures = {
    "SkipList": SkipList,
    "SplayTree": SplayTree,
}

def run_test(filename, structure_cls):
    
    with open(filename) as f:
        line = f.readline()
        if not line.strip():
            raise ValueError(f"Invalid or empty file: {filename}")
        
        n = int(line)
        operations = [list(map(int, f.readline().split())) for _ in range(n)]

    ds = structure_cls()
    op_count = {i: 0 for i in range(1, 7)}
    results = []

    start = time.perf_counter()

    for op in operations:
        op_type = op[0]
        op_count[op_type] += 1

        if op_type == 1:
            ds.insert(op[1])
        elif op_type == 2:
            ds.delete(op[1])
        elif op_type == 3:
            results.append(str(int(ds.search(op[1]))))
        elif op_type == 4:
            results.append(str(ds.floor(op[1])))
        elif op_type == 5:
            results.append(str(ds.ceil(op[1])))
            
        elif op_type == 6:
            r = ds.range_query(op[1], op[2])
            results.append(" ".join(map(str, r)))

    duration = time.perf_counter() - start
    return duration, op_count, len(ds), results

def print_stats(name, test_file, duration, op_count, size):
    
    # print(f"{test_file} --- [{name}]")
    print(f"{test_file} [{name}]")
    print(f"  Time: {duration:.3f}s")
    print(f"  Final size: {size}")
    for t in range(1, 7):
        if op_count[t]:
            print(f"  Type {t}: {op_count[t]}")
    print()

def run_all_tests(test_dir="tests", ext=".in"):
    test_files = sorted([f for f in os.listdir(test_dir) if f.endswith(ext)])
    
    
    if not test_files:
        print("No test files found.")
        return

    for test_file in test_files:
        path = os.path.join(test_dir, test_file)
        print(f"\nRunning: {test_file}")

        for struct_name, cls in structures.items():
            duration, operations, size, out = run_test(path, cls)

            output_file = f"{path.replace('.in', '')}.{struct_name.lower()}.out"
            with open(output_file, "w") as fout:
                fout.write("\n".join(out) + "\n")

            print_stats(struct_name, test_file, duration, operations, size)

if __name__ == "__main__":
    run_all_tests()