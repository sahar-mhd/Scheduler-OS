import copy

from numpy import array

global l


class Task:
    def __init__(self, name, type, duration):
        self.name = name
        self.type = type
        self.duration = duration
        self.state = "ready"
        self.timeSpent = 0

    def print(self):
        print(self.name + " " + self.type + " " +
              self.state + " " + str(self.timeSpent))


def HRRN(a, b, c, li):
    T = []
    for i in range(n):
        t = Task(l[i][0], l[i][1], l[i][2])
        T.append(t)
    w = []
    j = 0
    min = 1000
    m = 0
    for k in range(len(T)):
        wt = j
        s = T[k].duration
        ratio = (wt + s) / s
        if ratio < min:
            min = ratio
            m = k
    li.remove(l[m])
    i = m
    while len(T) != 0:
        print("round " + str(j))
        print("ready queue: " + str(li))
        print("waiting queue: " + str(w))
        if T[i].timeSpent == 0:
            T[i].state = "running"
            if T[i].type == 'X':
                # resource A, B
                if a > 0:
                    a -= 1
                else:
                    w.append(T[i])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
            elif T[i].type == "Y":
                # resource B,C
                if c > 0:
                    c -= 1
                else:
                    w.append(T[i])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
            else:
                # resource A, C
                if a > 0:
                    a -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
                if c > 0:
                    c -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
        print("A:" + str(a) + " B:" + str(b) + " C:" + str(c))
        print("cpu state: ")
        T[i].timeSpent += 1
        T[i].print()
        if T[i].timeSpent == T[i].duration:
            if T[i].type == 'X':
                a += 1
                b += 1
            elif T[i].type == "Y":
                b += 1
                c += 1
            else:
                a += 1
                c += 1
            T.remove(T[i])
            min = 1000
            m = 0
            for k in range(len(T)):
                wt = j+1
                s = T[k].duration
                ratio = (wt + s) / s
                if ratio < min:
                    min = ratio
                    m = k
            if len(li)>0:
                li.remove(li[m])
            i = m
        j += 1


def SJF(a, b, c, li):
    li = sorted(li, key=lambda l: l[2])
    print(li)
    
    FCFS(a, b, c, li)


def FCFS(a, b, c, l):
    T = []
    for i in range(n):
        t = Task(l[i][0], l[i][1], l[i][2])
        T.append(t)
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


def RR(a, b, c, l):
    # q=1;
    T = []
    for i in range(n):
        t = Task(l[i][0], l[i][1], l[i][2])
        T.append(t)
    w = []
    j = 0
    i = 0
    while len(T) != 0:
        i = i % len(T)
        print("round " + str(j))
        print("ready queue: " + str(l[j+1:]))
        print("waiting queue: " + str(w))
        if T[i].timeSpent != T[i].duration:
            T[i].state = "running"
            if T[i].type == 'X':
                # resource A, B
                if a > 0:
                    a -= 1
                else:
                    w.append(T[i])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
            elif T[i].type == "Y":
                # resource B,C
                if c > 0:
                    c -= 1
                else:
                    w.append(T[i])
                    T[0].state = "waiting"
                if b > 0:
                    b -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
            else:
                # resource A, C
                if a > 0:
                    a -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"
                if c > 0:
                    c -= 1
                else:
                    w.append(T[i])
                    T[i].state = "waiting"

            print("A:" + str(a) + " B:" + str(b) + " C:" + str(c))
            print("cpu state: ")
            T[i].timeSpent += 1
            T[i].print()
            if T[i].type == 'X':
                a += 1
                b += 1
            elif T[i].type == "Y":
                b += 1
                c += 1
            else:
                a += 1
                c += 1
            T[i].state = "ready"
        if T[i].timeSpent == T[i].duration:
            T.remove(T[i])
        else:
            l.append([T[i].name, T[i].type, T[i].duration])
            i += 1
        j += 1


if __name__ == '__main__':
    A, B, C = [int(x) for x in input().split(" ")]
    n = int(input())
    l = []
    for i in range(n):
        l.append(input().split(" "))
        l[i][2] = int(l[i][2])

    print("FCFS")
    FCFS(A, B, C, copy.copy(l))
    print("______________________________")
    print("SJF")
    SJF(A, B, C, copy.copy(l))
    print("______________________________")
    print("HRRN")
    HRRN(A, B, C, copy.copy(l))
    print("______________________________")
    print("RR")
    RR(A, B, C, copy.copy(l))
