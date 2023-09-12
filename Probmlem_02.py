vij=dict()
for i in range(26):
    alphabet=input("enter alphabet:")
    vij[alphabet]=ord(alphabet)
print("Unsorted Dictionary:\n",vij)

def item(x):
    return vij[x]
sorted_keys = sorted(vij, key=item)
v = {}
for i in sorted_keys:
    v[i] = vij[i]
print("Sorted Dictionary:\n",v)
