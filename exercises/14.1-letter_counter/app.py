par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
for l in par:
    if l != ' ':
        l = l.lower()
        if l in counts:
            counts[l] += 1
        else:
            counts[l] = 1

print(counts)
