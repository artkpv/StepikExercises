import json

class DFS :
    def __init__(self, graph, name) :
        assert name, 'empty name'
        assert type(graph) == dict
        self.graph = graph
        self.marked = []
        self._dfs(name)

    def _dfs(self, name) :
        assert name in self.graph, '"{}" not in "{}"'.format(name, repr(self.graph))
        for n in self.graph[name] :
            if n not in self.marked :
                self.marked += [n]
                self._dfs(n)

def get_descendants(jsData) :
    ancestors = {}

    # build graph:
    for c in jsData :
        name = c['name']
        parents = c['parents']
        if not name :
            continue
        if name not in ancestors:
            ancestors[name] = []
        assert type(parents) == list
        for p in parents :
            if p not in ancestors:
                ancestors[p] = []
            ancestors[p] += [name]

    # get ancestors:
    d = {}
    for n in ancestors :
        dfs = DFS(ancestors, n)
        count = len(dfs.marked) + 1
        d[n]= count

    for k in sorted(d) :
        print('{} : {}'.format(k, d[k]))


data = input()
parsed = json.loads(data)
get_descendants(parsed)
