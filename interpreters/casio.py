import math

"""
* 1: >
* 2: <
* 3: +
* 4: -
* 5: ,
* 6: .
* 7: [
* 8: ]

* A: cp
* B: tp
* C: code
* D: tapesub
* E: inp
* F: out

* X: curr instruction
* Y: balance dir
* M: balance
"""

A = 0
B = 0

C = 515732418269
D = 2000

E = 1002003000  # end zero-ed cell to prevent floating point
F = 1

X = 0
Y = 0
M = 0


def mod(a: int, b: int):
    return a - a//b * b
    # return a - int(a / b) * b


def length(n: int):
    return int(math.log10(n)) + 1


def get_digits_at(n: int, start: int, digits: int):
    return mod(n // 10 ** (length(n) - start - digits), 10**digits)
    # return mod(int(n / 10 ** (length(n) - start - digits)), 10**digits)


def equal(a: int, b: int):
    return int(math.cos(a - b))


def get_cell_at(tape, ptr):
    return get_digits_at(tape, 1 + ptr * 3, 3)


def move_pointer():
    global A, B, C, D, X, Y, M, E, F
    # move pointer if not balance
    B = B + (equal(X, 1) - equal(X, 2)) * equal(M, 0)
    # new cell if out of bound
    D = D + equal(B, -1) * 1998 * 10 ** (length(D) - 1)  # left bound
    D = D * (999 * equal(B, (length(D) - 1) / 3) + 1)  # right bound
    # reset pointer if out of bound
    B = (1 - equal(B, -1)) * B


def modify_cell():
    global A, B, C, D, X, Y, M, E, F
    # add/sub curr cell if not balance
    D = D + (equal(X, 3) - equal(X, 4)) * 10 ** (length(D) - 4 - B * 3) * equal(M, 0)
    # overflow cell
    D = D + equal(get_cell_at(D, B), 999) * 256 * 10 ** (length(D) - 4 - B * 3)
    D = D + equal(get_cell_at(D, B), 256) * -256 * 10 ** (length(D) - 4 - B * 3)


def bracket():
    global A, B, C, D, X, Y, M, E, F
    # set direction if bracket, keep direction when balance
    Y = equal(M, 0) * (equal(X, 7) - equal(X, 8) - Y) + Y
    # add balance if
    #   D[B] == 0 and C[A] = [
    #   D[B] != 0 and C[A] = ]
    M += (equal(X, 7) - equal(X, 8)) * (
        1 - equal(equal(X, 8) - equal(get_cell_at(D, B), 0) - equal(M, 0) + 1, 0)
    )


def io():
    global A, B, C, D, X, Y, M, E, F
    # replace cell with input
    D = D + equal(X, 5) * (get_cell_at(E, 0) - get_cell_at(D, B)) * equal(M, 0)
    E = E - equal(X, 5) * (get_cell_at(E, 0) + 999) * 10 ** (length(E) - 4) * equal(
        M, 0
    )
    # print cell
    F = equal(X, 6) * (999 * F + get_cell_at(D, B)) * equal(M, 0) + F


def tick():
    global A, B, C, D, X, Y, M, E, F
    X = get_digits_at(C, A, 1)
    move_pointer()
    modify_cell()
    io()
    bracket()
    # inc if not balance
    # add Y if balance
    A = A + Y + equal(M, 0) * (1 - Y)


# for i in range(30):
i=1
while X != 9:
    tick()
    print("tape", D, B)
    print("code", A, Y, M)
    print("io", E, F)
    print("---")
    i+=1
print(i)
