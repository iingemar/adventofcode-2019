class FuelManagementSystem:
    def __init__(self, wire_input):
        wires = wire_input.split()
        wires[0] = wires[0].split(',')
        wires[1] = wires[1].split(',')
        print()
        print(wires[0])
        print(wires[1])

        self.wire_path_01 = [(0, 0)]
        for wire_point in wires[0]:
            self.get_direction(wire_point)

    def get_direction(self, wire_point):
        print(wire_point)
        direction = wire_point[0]
        print(direction)
        length = wire_point[1:]
        print(length)
        path = []
        starting_point = self.wire_path_01[-1]
        print(starting_point)
        for x in range(int(length)):
            if direction == "U":
                path.append((starting_point[0], starting_point[1] + 1))
            elif direction == "D":
                path.append((starting_point[0], starting_point[1] - 1))
            elif direction == "L":
                path.append((starting_point[0] - 1, starting_point[1]))
            elif direction == "R":
                path.append((starting_point[0] + 1, starting_point[1]))
            starting_point = path[-1]
        print(path)
        self.wire_path_01.extend(path)
        print(self.wire_path_01)


    def get_intersections(self):
        pass

    def get_distance(self):
        return 0



