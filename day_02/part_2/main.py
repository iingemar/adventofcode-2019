class Intcode:
    def __init__(self, input, noun, verb):
        self.memory = [int(x) for x in input.split(',')]
        self.memory[1] = noun
        self.memory[2] = verb
        self.instruction_pointer = 0
        self.params = []

        while self.opcode() != 99:
            self.update_parameters()

            if self.opcode() == 1:
                self.opcode_1()
            elif self.opcode() == 2:
                self.opcode_2()
            self.move_forward()

    def update_parameters(self):
        self.params = [
            self.memory[self.instruction_pointer + 1],
            self.memory[self.instruction_pointer + 2],
            self.memory[self.instruction_pointer + 3]
        ]

    def opcode(self):
        return self.memory[self.instruction_pointer]

    def value(self, position):
        return self.memory[position]

    def opcode_1(self):
        result = self.value(self.params[0]) + self.value(self.params[1])
        self.memory[self.params[2]] = result

    def opcode_2(self):
        result = self.value(self.params[0]) * self.value(self.params[1])
        self.memory[self.params[2]] = result

    def move_forward(self):
        self.instruction_pointer += 4


def find_answer():
    for noun in range(100):
        for verb in range(100):
            r = Intcode(
                '1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,2,19,9,23,1,23,5,27,2,6,27,31,1,31,5,35,1,35,5,39,2,39,6,43,2,43,10,47,1,47,6,51,1,51,6,55,2,55,6,59,1,10,59,63,1,5,63,67,2,10,67,71,1,6,71,75,1,5,75,79,1,10,79,83,2,83,10,87,1,87,9,91,1,91,10,95,2,6,95,99,1,5,99,103,1,103,13,107,1,107,10,111,2,9,111,115,1,115,6,119,2,13,119,123,1,123,6,127,1,5,127,131,2,6,131,135,2,6,135,139,1,139,5,143,1,143,10,147,1,147,2,151,1,151,13,0,99,2,0,14,0',
            noun, verb)
            print('%s,%s > %s' % (noun, verb, r.memory[0]))
            if r.memory[0] == 19690720:
                return

find_answer()
