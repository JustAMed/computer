from sys import exit

memory = [0] * 16
registers = {
    "R0": 0,
    "R1": 0
}

program = [
    ("LOAD", "R0", 2),
    ("LOAD", "R1", 3),
    ("ADD", "R0", "R1"),
    ("PRINT", "R0"),
    ("HALT",)
]

def LOAD(instruction):
    _, reg, v = instruction
    registers[reg] = v

def ADD(instruction):
    _, reg, regv = instruction
    registers[reg] += registers[regv]

def PRINT(instruction):
    _, reg = instruction
    print(registers[reg])

def HALT(_):
    exit()

ops = {
    'LOAD': LOAD,
    'ADD': ADD,
    'PRINT': PRINT,
    'HALT': HALT,
}

def main():
    pc = 0
    while True:
        instruction = program[pc]
        ops[instruction[0]](instruction)
        pc += 1

main()

