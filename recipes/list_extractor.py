def process_list(filepath):
    data = open(filepath, "r")
    a=str()
    b=str()
    c = open('/home/brian/repos/odin-recipes/recipes/recipe2.txt', "a+")
    print(data)
    lines = data.readlines()
    for line in lines:
        if line.strip():
            a+=(line)
    a = a.splitlines()
    for index, item in enumerate(a):
        if index == 0:
            b += f"<p><h1>{item}</p></h1>"
        elif index == 1:
            b += f"<p><h2>{item}</p></h2>\n"
        elif index == 2:
            b += f"<ul><li>{item}</li>\n"
        elif index == len(a)-1:
            b += f"<li>{item}</li></ul>\n\n"
        else:
            b += f"<li>{item}</li>\n"
    c.write(b)
    c.close()
process_list("/home/brian/repos/odin-recipes/recipes/reamy-cajun-chicken-pasta.txt")