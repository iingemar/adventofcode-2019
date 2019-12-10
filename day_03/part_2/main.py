class FuelManagementSystem:
    def __init__(self, wire_input='', wire_1=None, wire_2=None):
        if wire_input:
            wire_inputs = wire_input.split()
            wire_inputs[0] = wire_inputs[0].split(',')
            wire_inputs[1] = wire_inputs[1].split(',')
        else:
            wire_inputs = [
                [],
                []
            ]
            wire_inputs[0] = wire_1.split(',')
            wire_inputs[1] = wire_2.split(',')

        self.wire_paths = [
            [(0, 0)],
            [(0, 0)]
        ]
        for wire_point in wire_inputs[0]:
            self.get_direction(0, wire_point)
        for wire_point in wire_inputs[1]:
            self.get_direction(1, wire_point)

        intersections = self.get_intersections()
        print('intersections: ' + str(intersections))
        scores = []
        for intersection in intersections:
            if intersection == (0, 0):
                print('(0, 0) continue')
                continue
            idx_1 = self.wire_paths[0].index(intersection)
            idx_2 = self.wire_paths[1].index(intersection)
            score = idx_1 + idx_2
            print('%s > %s steps' % (intersection, score))
            scores.append(score)

        self.closest_intersection = min(scores)
        print('closest_intersection: %s' % self.closest_intersection)

    def get_direction(self, wire_path_index, wire_point):
        direction = wire_point[0]
        length = wire_point[1:]
        path = []
        starting_point = self.wire_paths[wire_path_index][-1]
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
        self.wire_paths[wire_path_index].extend(path)

    def get_intersections(self):
        return list(set(self.wire_paths[0]).intersection(self.wire_paths[1]))

    def get_distance(self, point):
        distance = abs(0 - point[0]) + abs(0 - point[1])
        print('distance: %s' % distance)
        return distance


if __name__ == "__main__":
    with open('input.txt') as f:
        content = f.readlines()
        FuelManagementSystem('', content[0], content[1])
