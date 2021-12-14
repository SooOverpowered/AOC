import functools


class Map:
    def __init__(self):
        self.nodes = dict()
        self.paths = set()

    def add_node(self, node):
        self.nodes[node] = []

    def add_connection(self, one, two):
        self.nodes[one].append(two)
        self.nodes[two].append(one)

    def path_find(self, curr=None, traversed=None):
        curr = 'start' if curr is None else curr
        traversed = '' if traversed is None else traversed
        if curr == 'end':
            self.paths.add(traversed+',end')
        else:
            for node in self.nodes[curr]:
                if node.islower() and ','+node in traversed:
                    pass
                else:
                    self.path_find(node, traversed=traversed+','+curr)

    def path_find_twice(self, curr='start', traversed=set(), twice_traverse=True, twice=None):
        if curr == 'end':
            return 1
        if curr == 'start' and len(traversed) != 0:
            return 0
        if curr.islower() and curr in traversed and not twice_traverse:
            return 0
        elif curr.islower() and curr in traversed and twice_traverse:
            if twice is None:
                twice = curr
            else:
                return 0
        traversed= traversed | {curr}
        count = 0
        for node in self.nodes[curr]:
            count += self.path_find_twice(node,
                                          traversed, twice_traverse, twice)
        return count


def part1(data):
    lines = data.split('\n')
    cave_map = Map()
    for line in lines:
        nodes = line.split('-')
        for node in nodes:
            if node not in cave_map.nodes:
                cave_map.add_node(node)
        cave_map.add_connection(nodes[0], nodes[1])
    cave_map.path_find()
    return len(cave_map.paths)


def part2(data):
    lines = data.split('\n')
    cave_map = Map()
    for line in lines:
        nodes = line.split('-')
        for node in nodes:
            if node not in cave_map.nodes:
                cave_map.add_node(node)
        cave_map.add_connection(nodes[0], nodes[1])
    return cave_map.path_find_twice()


if __name__ == '__main__':
    import runner
    runner.run(day=12)
