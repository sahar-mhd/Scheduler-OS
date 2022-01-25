
class Task:
    def __init__(self, name, type, duration):
        self.name = name
        self.type = type
        self.duration = duration
        self.state = "ready"
        self.timeSpent = 0

    def print(self):
        print(self.name + " " + self.type + " " + self.state + " " + str(self.timeSpent))


def FCFS(a, b, c):
    w = []
    j = 0
    while len(T) != 0:
        print("round " + str(j))
        print("ready queue: " + str(l[1:]))
        print("waiting queue: " + str(w))
        if T[0].timeSpent == 0:
            T[0].state = "running"
            if T[0].type == 'X':
                # resource A, B
                if a > 0:
                    a -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
            elif T[0].type == "Y":
                # resource B,C
                if c > 0:
                    c -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
            else:
                # resource A, C
                if a > 0:
                    a -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
                if c > 0:
                    c -= 1
                else:
                    w.append(T[0])
                    T[0].state = "waiting"
        print("A:" + str(a) + " B:" + str(b) + " C:" + str(c))
        print("cpu state: ")
        T[0].timeSpent += 1
        T[0].print()
        if T[0].timeSpent == T[0].duration:
            if T[0].type == 'X':
                a += 1
                b += 1
            elif T[0].type == "Y":
                b += 1
                c += 1
            else:
                a += 1
                c += 1
            T.remove(T[0])
            l.remove(l[0])
        j += 1


if __name__ == '__main__':
    A, B, C = [int(x) for x in input().split(" ")]
    n = int(input())
    l = []
    for i in range(n):
        l.append(input().split(" "))
        l[i][2] = int(l[i][2])
    T = []
    for i in range(n):
        t = Task(l[i][0], l[i][1], l[i][2])
        T.append(t)

    print("FCFS")
    FCFS(A, B, C)
