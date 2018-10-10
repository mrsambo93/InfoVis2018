import json

data = dict()
with open("got-graph-images.json") as graph:
	data = json.load(graph)

new_graph = dict()
keys = ['mother', 'father', 'sibling', 'lover', 'spouse']

new_graph['nodes'] = list()
new_graph['links'] = list()

def contains_id(nodes, id):
	for n in nodes:
		if n['id'] == id:
			return True
	return False

for link in data['links']:
	if link['relation'] in keys:
		new_graph['links'].append(link)

for new_link in new_graph['links']:
	for node in data['nodes']:
		if new_link['source'] == node['id'] or new_link['target'] == node['id']:
			if not contains_id(new_graph['nodes'], node['id']):
				new_graph['nodes'].append(node)

with open('family_tree.json', 'w') as output:
	json.dump(new_graph, output, indent=4)
