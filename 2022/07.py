class Folder:
    def __init__(self,name, parent=None):
        self.name = name
        self.value = 0
        self.subfolders = {}
        self.parent = parent
    def add_folder(self, name):
        self.subfolders[name] = Folder(name, self)
    def add_value(self, value):
        self.value += value
        if self.parent!=None:
            self.parent.add_value(value)
        
    
def dfs(folder):
        result = 0
        for sub in folder.subfolders.values():
            if sub.value <= 100000:
                result+=sub.value
            result+=dfs(sub)
        return result

def dfs_2(folder, needed, curr_min):
    for sub in folder.subfolders.values():
        if sub.value >= needed and sub.value < curr_min:
            curr_min = sub.value
        curr_min = dfs_2(sub, needed, curr_min)
    return curr_min
    
def parser(data):
    root = Folder("root")
    curr = root
    for line in data.split("\n")[1::]:
        if line.startswith('$'):
            cmd = line.split(' ')[1]
            if cmd == 'cd':
                if line.split(' ')[-1] == '..':
                    curr = curr.parent
                else:
                    curr=curr.subfolders[line.split(' ')[-1]]
        elif line.startswith('dir'):
            curr.add_folder(line.split(' ')[-1])
        else:
            curr.add_value(int(line.split(' ')[0]))
    return root

def part1(data):
    root = parser(data)
    return dfs(root)

def part2(data):
    root = parser(data)
    needed = root.value -40000000
    return dfs_2(root, needed, root.value)
    
