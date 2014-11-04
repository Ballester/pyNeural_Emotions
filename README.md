-->External libs:
scipy, networkx


-->The configuration file is organized as follows:

external_delay 3
update_delay 2
external_deviation 2

external_delay: time in seconds to wait between two external inputs

update_delay: time in seconds for the network update (an update is realized everytime the external_input is done too)

external_deviation: the uncertainty involved in the external input

nnodes: Number of nodes in the tree

nedges: Number of edges in the tree

w_threshold: Threshold involved in the edge relation strenght

followed by n_nodes of:
node_name Level_of_node Power_of_node

followd by n_edges of:
edge: From_node To_node Edge_relation


-->The external input file is organized as follows:

any number of lines of:
confirmed_feeling disconfirmed_feeling confirmed_input disconfirmed_input confirm_chance
