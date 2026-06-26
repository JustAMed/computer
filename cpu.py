from assembler import assemble

class CPU:
    def __init__(self):
        self.memory = [0] * 16
        self.registers = {
            "R0": 0,
            "R1": 0,
            "R2": 0,
            "R3": 0
        }

        self.program = []
        self.running = True
        self.pc = 0

        self.ops = {
            'LOAD': self.LOAD,
            'ADD': self.ADD,    
            'PRINT': self.PRINT,
            'HALT': self.HALT,
            'JMP': self.JMP,
            'CMP': self.CMP,
            'JZ': self.JZ,
            'LOADM': self.LOADM,
            'STORE': self.STORE,
        }

        self.flag_zero = 0

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
        self.running = False

    def JMP(self, instruction):
        _, v = instruction
        self.pc = v - 1
    
    def CMP(self, instruction):
        _, r0, r1 = instruction
        self.flag_zero = (self.registers[r0] == self.registers[r1])

    def JZ(self, instruction):
        _, addr = instruction
        if self.flag_zero:
            self.pc = addr - 1

    def LOADM(self, instruction):
        _, reg, mem = instruction
        self.registers[reg] = self.memory[mem]

    def STORE(self, instruction):
        _, mem, reg = instruction
        self.memory[mem] = self.registers[reg]

    def run(self, program):
        while self.pc < len(program) and self.running == True:
            instruction = program[self.pc]
            self.ops[instruction[0]](instruction)
            self.pc += 1

cpu = CPU()
program = assemble("program.fwd")
cpu.run(program)