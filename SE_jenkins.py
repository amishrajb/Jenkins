#!/usr/bin/python3

def add_6_to_list(l):
	for i in range(len(l)):
		l[i] += 6
	return l

l = [93,69,44,11,74]
print(add_6_to_list(l))
