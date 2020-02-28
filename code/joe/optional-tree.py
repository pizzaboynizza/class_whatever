# Lab : Tree
# Author : Joe

import random

names = ["virginia", "christine", "carl", "lillian"]


def generate_tree(depth):
    n_children = int(random.random()*10/depth)
    if n_children == 0:
        return {"type": "leaf", "name": random.choice(names)}
    branch = {"type": "branch", "children": []}
    for i in range(n_children):
        child = generate_tree(depth+1)
        branch["children"].append(child)
    return branch


def print_node(node, indentation):
    if node["type"] == "leaf":
        print(indentation + node["name"])
    else:
        print(indentation + "-")
        for i in range(len(node["children"])):
            print_node(node["children"][i], indentation + "\t")


# count all trees and branches
def count_nodes(node):
    if node["type"] == "leaf":
        return 1
    r = 1
    for i in range(len(node["children"])):
        r += count_nodes(node["children"][i])
    return r

# Impelmented function
def count_leaves(node):
    if node["type"] == "leaf":
        return 1
    r = 0 # this is basically the only difference between count_leaves and count_nodess
    for i in range(len(node["children"])):
        r += count_leaves(node["children"][i])
    return r

# Implemented function
def rename_leaves(node, to_find, to_replace):
    if node["type"] == "leaf":
        if node["name"] == to_find:
            node["name"] = to_replace
    else:
        for i in range(len(node["children"])):
            rename_leaves(node["children"][i], to_find, to_replace)

root = generate_tree(1)
print_node(root, "")
print(f"\nNumber of nodes: {count_nodes(root)}")
print(f"Number of leaves: {count_leaves(root)}")

fin = input("Enter name to be replaced: ")
rep = input("Enter replacement name: ")
rename_leaves(root, fin, rep)
print_node(root, "")