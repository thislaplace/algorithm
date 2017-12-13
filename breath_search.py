#!/usr/bin/python
# coding=utf-8

#
# 寻找目标，就进队，目标不符合条件就出队，并把他的邻接目标进队
#

from collections import deque

graph = {}
graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["jonny"] = []

def person_is_seller(person):
    return person[-1] == "m"

def breadth_search():
    searched = []
    search_queue = deque()
    search_queue += graph["you"]
    while search_queue:
        person = search_queue.popleft()
        if person in searched:
            continue

        if person_is_seller(person):
            print(person + " is a mango seller!")
            return True
        else:
            search_queue += graph[person]
            searched.append(person)

    return False

if __name__ == "__main__":
    breadth_search()
