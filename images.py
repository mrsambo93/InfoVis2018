import json, csv

with open('thrones_characters.csv') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('got-graph.json') as got:
    graph = json.load(got)

result = dict()
result['nodes'] = list()
result['links'] = list(graph['links'])

for el2 in graph['nodes']:
    new_el = dict(el2)
    for el1 in rows:
        if el1['name'].lower() in el2['name'].lower():
            new_el['image'] = str(el1['image'])
    result['nodes'].append(new_el)

with open('got-graph-images.json', 'w') as output:
    json.dump(result, output, indent=4)
