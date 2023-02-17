a=str()
b=str()
c = open('recipe2.txt', "w")
with open('recipe.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()

    for line in lines:
        if line.strip():
            a+=(line)
    a = a.splitlines()
    for item in a:
        b += f"<li>{item}</li>\n"
c.write(b)
c.close()