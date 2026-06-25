from sys import exit

class CPU:
    def __init__(self):
        self.memory = [0] * 16
        self.registers = {
            "R0": 0,
            "R1": 0
        }

        self.program = []
        self.running = True
        self.pc = 0

        self.ops = {
            'LOAD': self.LOAD,
            'ADD': self.ADD,
            'PRINT': self.PRINT,
            'HALT': self.HALT,
        }

    def LOAD(self, instruction):
        _, reg, v = instruction
        self.registers[reg] = v

    def ADD(self, instruction):
        _, reg, regv = instruction
        self.registers[reg] += self.registers[regv]

    def PRINT(self, instruction):
        _, reg = instruction
        print(self.registers[reg])

    def HALT(self, _):
        exit()

    def run(self, program):
        while self.pc < len(program):
            instruction = program[self.pc]
            self.ops[instruction[0]](instruction)
            self.pc += 1

program = [
    ("LOAD", "R0", 2),
    ("LOAD", "R1", 3),
    ("ADD", "R0", "R1"),
    ("PRINT", "R0"),
    ("HALT",)
]

cpu = CPU()
cpu.run(program)