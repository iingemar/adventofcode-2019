class FuelManagementSystem:
    def __init__(self, wire_input):
        wire_inputs = wire_input.split()
        wire_inputs[0] = wire_inputs[0].split(',')
        wire_inputs[1] = wire_inputs[1].split(',')
        print()
        print(wire_inputs[0])
        print(wire_inputs[1])

        self.wire_paths = [
            [(0, 0)],
            [(0, 0)]
        ]
        for wire_point in wire_inputs[0]:
            self.get_direction(0, wire_point)
        for wire_point in wire_inputs[1]:
            self.get_direction(1, wire_point)

        intersections = self.get_intersections()
        distances = []
        for intersection in intersections:
            distance = self.get_distance(intersection)
            distances.append(distance)
        print(distances)
        # Remove 0
        distances.remove(0)
        self.closest_intersection = min(distances)
        print(self.closest_intersection)

    def get_direction(self, wire_path_index, wire_point):
        print(wire_point)
        direction = wire_point[0]
        print(direction)
        length = wire_point[1:]
        print(length)
        path = []
        starting_point = self.wire_paths[wire_path_index][-1]
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
        self.wire_paths[wire_path_index].extend(path)
        print(self.wire_paths[wire_path_index])

    def get_intersections(self):
        intersections = list(set(self.wire_paths[0]).intersection(self.wire_paths[1]))
        print('intersections')
        print(intersections)
        return intersections

    def get_distance(self, point):
        distance = abs(0 - point[0]) + abs(0 - point[1])
        print('distance: %s' % distance)
        return distance


with open('input.txt') as f:
    content = f.readlines()
    FuelManagementSystem(content)
