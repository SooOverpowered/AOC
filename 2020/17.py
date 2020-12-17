def part1(data):
    initial_layer= data.rstrip().split('\n')
    initial_layer=[[cube for cube in layer] for layer in initial_layer]
    l=len(initial_layer)
    w=len(initial_layer[0])
    layer_indexing={0:initial_layer}
    prev_state={0:initial_layer}
    cycle=0
    while cycle!=7:
        existing=sorted(prev_state.keys())
        for i in existing:
            if i+1 not in prev_state.keys():
                prev_state[i+1]=None
                

def part2(data):
    pass