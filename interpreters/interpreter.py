import re

with open(input('file: '), "r") as f:
    CODE = f.read()

CELL_OVERFLOW = 256

pointer = 0
tape = [0]

CODE = re.sub("[^><\+-\.,\[\]#]", "", CODE)


def findMatchingBracket(start, direction, char):
    BRACKETS = "[]"
    bracketCount = 1
    end = ((len(CODE) - 1) + (direction * (len(CODE) - 1))) // 2 + direction
    for i in range(
        start + direction,
        end,
        direction,
    ):
        if CODE[i] == BRACKETS[char]:
            bracketCount += 1
        elif CODE[i] == BRACKETS[(char + 1) % len(BRACKETS)]:
            bracketCount -= 1

        if bracketCount == 0:
            return i

    raise ValueError(f"Missing matching bracket for bracket at position {start}")


def movePointer(move):
    global pointer
    pointer += move
    if pointer >= len(tape):
        tape.append(0)
    elif pointer < 0:
        pointer = 0
        tape.insert(0, 0)


char_i = 0
while char_i < len(CODE):
    if CODE[char_i] == "+":
        tape[pointer] = (tape[pointer] + 1) % CELL_OVERFLOW

    elif CODE[char_i] == "-":
        tape[pointer] = (tape[pointer] - 1) % CELL_OVERFLOW

    elif CODE[char_i] == ">":
        movePointer(1)

    elif CODE[char_i] == "<":
        movePointer(-1)

    elif CODE[char_i] == ".":
        print(chr(tape[pointer]), end="")

    elif CODE[char_i] == ",":
        tmp = input()
        tmp = ord(tmp[0]) if len(tmp) > 0 else 0
        tape[pointer] = int(tmp)

    elif CODE[char_i] == "[":
        if tape[pointer] == 0:
            closing = findMatchingBracket(char_i, 1, 0)
            char_i = closing

    elif CODE[char_i] == "]":
        if tape[pointer] != 0:
            opening = findMatchingBracket(char_i, -1, 1)
            char_i = opening

    elif CODE[char_i] == "#":
        tmp = tape.copy()
        tmp[pointer] = str(tape[pointer])
        print(tmp)
        input()

    char_i += 1


# tape[pointer] = str(tape[pointer])
# print(tape)
