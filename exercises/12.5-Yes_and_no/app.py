the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

def wiki_or_woko(value):
    return "wiki" if value == 1 else "woko"


new_list = list(map(wiki_or_woko, the_bools))

print(new_list)


