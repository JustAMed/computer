def assemble(given_program):
    firstPass = []
    program = []
    labels = {}
    instruction_number = 0

    with open(given_program) as fwd:
        lines = fwd.readlines()
    for line in lines:
        line = line.strip()
        if line.endswith(':'):
            labels[line[:-1]] = instruction_number
        else:
            instruction_number += 1
        firstPass.append(line)

    for line in firstPass:
        if line.endswith(':'):
            continue
        parts = line.split()
        for i in range(0, len(parts)):
            if parts[i].isdigit():
                parts[i] = int(parts[i])
            if parts[i] in labels:
                parts[i] = labels[parts[i]]
        
        program.append(tuple(parts))

    return program