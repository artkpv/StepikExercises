from requests import get

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE0Nzg2MDQ0MjIsImlhdCI6MTQ3Nzk5OTYyMiwiYXVkIjoiNTgxODdiMzAyNzViMjQxMjk3MDAwNDg5IiwiaXNzIjoiR3Jhdml0eSIsImp0aSI6IjU4MTg3YzA2YjIwMmEzNjU4ODAwMDAxYyJ9.jL7UMr6vz89ZcOlKBle_PE5gHTIGMRFvEbXM33s20_0'

ids = '''
53164f7e275b244ce00000d5
511294005c85615a61000082
4d8b929c4eb68a1b2c0002e4
55f0747b7261693808000030
5524173772616947559b0200
4e96f792be2b4e0001002fb1
554a78d87261692b00710400
548632a7726169516a620100
51e041ac275b2407470001b1
4e1620155ee1940001000006
542e86e47261695773da1700
4f5f64c13b555230ac000004
4f5f64c13b555230ac000007
53e126267261692d6bf50100
4df3e547a1772600010057da
'''.split()

a = []
for id_ in ids :
    r = get('https://api.artsy.net/api/artists/' + id_, headers = {'X-Xapp-Token' : token})
    data = r.json()
    print(data)
    a += [data['birthday'] + data['sortable_name']]

print(repr(a))

for artist in sorted(a) :
    print(artist[4:])

