


class Trie:
    def __init__(self) -> None:
        self.root = {}
    
    def select(self,file):
        node = self.root
        parts = file.split('/')
        for part in parts:
            
            part2 = part.split('.')
            extension = part2[1] if len(part2) == 2 else None
            
            if extension == 'txt':
                if 'selected' not in node: node['selected'] = set()
                node['selected'].add(file)
                if len(node['selected']) == len(node['files']):
                    node['all'] = '/'.join(parts[:-1])
                continue
            node = node[part]



                

    def insert(self,file):
        parts = file.split('/')
        node = self.root
        for part in parts:
            part2 = part.split('.')
            extension = part2[1] if len(part2) == 2 else None
            if extension == 'txt':
                if 'files' not in node: node['files'] = set()
                node['files'].add(part)
                continue

            if part not in node: node[part] = {}
            node = node[part]

    def output(self,node):
        if not node: return
        if 'all' in node:
            print(node['all'])
            return
        if 'selected' in node:
            for file in node['selected']:
                print(file)
            return
        for child in node.values():
            self.output(child) 



t = Trie()

dirs = [
"/a/b/x.txt",
"/a/b/p.txt",
"/a/c",
"/a/d/y.txt",
"/a/d/z.txt"
]
selected = [
"/a/d/y.txt",
"/a/d/z.txt",
"/a/b/p.txt"
]

for dir in dirs:
    t.insert(dir)
for select in selected:
    t.select(select)

t.output(t.root)


    