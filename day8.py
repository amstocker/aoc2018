def get_metadata_sum(data):
    def helper(data, i):
        n_children = data[i]
        n_metadata = data[i+1]
        metadata = 0
        i += 2
        for n in range(n_children):
            child_metadata, i = helper(data, i)
            metadata += child_metadata
        metadata += sum(data[i:i+n_metadata])
        i += n_metadata
        return metadata, i
    return helper(data, 0)[0]

def get_root_value(data):
    def helper(data, i):
        n_children = data[i]
        n_metadata = data[i+1]
        i += 2
        if n_children > 0:
            child_values = {}
            for n in range(n_children):
                child_value, i = helper(data, i)
                child_values[n] = child_value
            value = sum(child_values[k-1] for k in data[i:i+n_metadata] \
                                          if (k-1) in child_values)
        else:
            value = sum(data[i:i+n_metadata])
        i += n_metadata
        return value, i
    return helper(data, 0)[0]


with open("day8_input.txt") as f:
    data = list(map(int, f.read().rstrip().split()))
    print(get_metadata_sum(data))
    print(get_root_value(data))
