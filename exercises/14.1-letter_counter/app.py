par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

par = par.lower().replace(" ", "")


for letter in par:
    if letter in counts:
        counts[letter] += 1
    else:
        counts[letter] = 1


        


print(counts)
