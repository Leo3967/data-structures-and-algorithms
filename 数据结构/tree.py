class Node:
    def __init__(self, name, type='dir') -> None:
        self.name = name
        self.type = type  # 'dir' or 'file'
        self.children = []
        self.parent = None
    
    def __repr__(self) -> str:
        return self.name

class FileSystemTree:
    def __init__(self) -> None:
        self.root = Node('/')
        self.now = self.root

    def mkdir(self, name):
        # name必须是文件夹，即以/结尾
        if name[-1] != '/':
            name += '/'
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now
    
    def ls(self):
        return self.now.children
    
    def cd(self, name):
        # 绝对路径和相对路径
        if name[-1] != '/':
            name += '/'
        if name == '../':
            self.now = self.now.parent
            return

        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        else:
            raise ValueError('invalid dir')

tree = FileSystemTree()
tree.mkdir('var/')
tree.mkdir('bin/')
tree.mkdir('usr/')
tree.cd('bin/')
tree.mkdir('python/')
tree.cd('../')
print(tree.ls())