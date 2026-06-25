class CPU:
    def __init__(self):
        self.memory = [0] * 16
        self.registers = {
            "R0": 0,
            "R1": 0,
            "R2": 0
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
            'JZ': self.JZ
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

    def run(self, program):
        while self.pc < len(program) and self.running == True:
            instruction = program[self.pc]
            self.ops[instruction[0]](instruction)
            self.pc += 1
    
def load_fwd(prog):
    program = []
    with open(prog) as fwd:
        lines = fwd.readlines()
    for line in lines:
        parts = line.split()
        command = []
        for i in range(0, len(parts)):
            if parts[i].isdigit() is True:
                command.append(int(parts[i]))
                continue
            command.append(parts[i])
        program.append(tuple(command))
    return program

cpu = CPU()
program = load_fwd("program.fwd")
cpu.run(program)