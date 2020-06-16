# your code goes here
import queue

q = queue.Queue()
visited = set()


def f(x, y, z):
    return 172 + 600 * x - 288 * y - 238 * z


def enqueueIfNotExist(try_solution):
    if try_solution not in visited:
        q.put(try_solution)
        visited.add(try_solution)


def main():
    q.put((0, 0, 0))
    visited.add((0, 0, 0))
    while not q.empty():
        try_solution = q.get()
        x = try_solution[0]
        y = try_solution[1]
        z = try_solution[2]
        remain = f(x, y, z)
        print("x,y,z=", x, ",", y, ",", z, " remain ", remain)
        if remain == 0:
            return try_solution
        elif remain > 0:
            try_solution = (x, y + 1, z)
            enqueueIfNotExist(try_solution)

            try_solution = (x, y, z + 1)
            enqueueIfNotExist(try_solution)
        elif remain < 0:
            try_solution = (x + 1, y, z)
            enqueueIfNotExist(try_solution)


if __name__ == "__main__":
    main() 