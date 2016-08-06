from graph_tool.all import *
import json

def get_data(filename='wiki.json'):
    with open(filename) as f:
        dataset = json.load(f)
    return dataset

def proc_data(dataset):
    urls = list(set([ data['self_url'] for data in dataset ]))
    urls.extend( list(set([ data['ext_url'] for data in dataset ])) )
    url_to_idx = { url:i for i, url in enumerate(urls) }
    # build dataset, replacing urls with ids
    mod_dataset = []
    for data in dataset:
        mod_dataset.append((url_to_idx[data['self_url']],url_to_idx[data['ext_url']],data['title'],data['ext_title']))
    # return modified dataset
    return mod_dataset, len(urls)

def build_graph(dataset,node_count):
    g = Graph()
    g.add_vertex(node_count)
    # label -> title
    label = g.new_edge_property('string')
    for n1,n2,t1,t2 in dataset:
        # connect nodes
        e = g.add_edge(n1,n2)
        # name edge
        label[e] = t2
    # return the graph
    return g, label


if __name__ == '__main__':
    dataset, node_count = proc_data(get_data())
    g, label = build_graph(dataset,node_count)
    graph_draw(g, edge_text=label, edge_font_size=13, edge_text_distance=30, edge_marker_size=10,output_size=(7500, 7500), output="graph-op.png")
