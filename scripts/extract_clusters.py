
import sys
import networkx as nx
from modules import get_clusters
import csv
   
[_, graph, output_file] = sys.argv

graph = nx.read_gpickle(graph)
clusters, c2n, n2c = get_clusters(graph, is_include_noise = True)
#print(clusters)

output_data = [{'identifier':n, 'cluster':c} for n, c in n2c.items()]    
# Export data
with open(output_file, 'w') as f:  
    w = csv.DictWriter(f, ['identifier', 'cluster'], delimiter='\t', quoting = csv.QUOTE_NONE, quotechar='')
    w.writeheader()
    w.writerows(output_data)
