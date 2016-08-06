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
    url_title = [ (data['self_url'],data['title']) for data in dataset ]
    url_to_title = { url:title for url,title in list(set(url_title)) }
    return urls, url_to_idx, url_to_title


if __name__ == '__main__':
    dataset = get_data()
    urls, url_to_idx, url_to_title = proc_data(dataset)
    print(len(urls),url_to_idx['https://en.wikipedia.org/wiki/Rio_de_Janeiro'],url_to_title['https://en.wikipedia.org/wiki/Rio_de_Janeiro'])
'''
def build_graph():

g = Graph()
g.add_vertex(4)
label = g.new_edge_property("string")
e = g.add_edge(0, 1)
label[e] = "A"
e = g.add_edge(2, 3)
label[e] = "foo"
e = g.add_edge(3, 1)
label[e] = "bar"
e = g.add_edge(0, 3)
label[e] = "gnat"
'''
