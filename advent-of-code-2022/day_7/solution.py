class TreeNode:
    def __init__(self, name):
        self.parent = None
        self.children = []
        self.value = 0
        self.name = name
            
    def add_child(self, child_node):
        # creates parent-child relationship
        self.children.append(child_node)
    
    def add_parent(self, parent_node):
        self.parent = parent_node
    
    def get_child(self, name):
        for child in self.children:
            if name in child.name:
                return child


def load_data():
    with open('input.txt', 'r') as f:
        data = f.read().splitlines()
    return data
    

def write_data(solution1, solution2):
    with open('output.txt', 'w') as f:
        f.write(solution1)
        f.write('\n')
        f.write(solution2)

def build_tree(data):
    root = TreeNode(name='/')
    curr_node = root
    for d in data[1:]:
        d = d.split()
        
        if 'cd' in d:
            if '..' in d:
                curr_node.parent.value += curr_node.value
                curr_node = curr_node.parent
            else:
                name = d[-1]
                curr_node = curr_node.get_child(name)
    
        elif d[0].isdigit():
            curr_node.value += int(d[0])
    
        elif 'dir' in d:
            # Add node if not exist
            dir_name = d[-1]
            if dir_name not in curr_node.children:
                node = TreeNode(name=dir_name)
                curr_node.add_child(node)
                node.add_parent(curr_node)
    return root


def get_total_size(node, answer, threshold=100000):
    if not node.children:
        if node.value <= threshold:
            answer += node.value
        return node, answer
    else:
        if node.value <= threshold:
            answer += node.value
        for child in node.children:
            node, answer = get_total_size(child, answer)
        return node, answer


def get_potential_dir(node, answer, threshold):
    if not node.children:
        if node.value >= threshold:
            answer.append(node.value)
        return node, answer
    else:
        if node.value >= threshold:
            answer.append(node.value)
        for child in node.children:
            node, answer = get_potential_dir(child, answer, threshold)
        return node, answer
    
    
def main():
    data = load_data()
    root = build_tree(data)
    
    solution1 = 0
    node, solution1 = get_total_size(root, solution1, threshold=100000)
    solution1 = str(solution1)
    
    filesystem = 70000000
    least = 30000000
    new_threshold = least - (filesystem - root.value)
    solution2 = []
    node, solution2 = get_potential_dir(root, solution2, threshold=new_threshold)
    solution2.sort()
    solution2 = str(solution2[0])
    
    write_data(solution1, solution2)
    


if __name__ == '__main__':
    main()
