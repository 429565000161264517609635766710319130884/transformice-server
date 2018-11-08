import os, random
root = os.getcwd()

def parseJson(path):
    filepath = f"{root}\\{path}"
    file = open(filepath, "r")
    return eval(file.read())

def getCaptcha():
    vocabulary = parseJson("resources\\json\\captcha.json")
    captcha = list(random.choice(list(vocabulary.keys())) for _ in range(4))
    px, py = 0, 1
    lines = []
    for count in range(1, 17):
        wc = 1
        values = []
        for char in captcha:
            ws = vocabulary[char]
            if count > len(ws):
                count = len(ws)
            ws = ws[str(count)]
            i = 1 if wc > 1 else 0
            values += ws.split(",")[i:]
            wc += 1
        lines += [",".join(map(str, values))]
        if px < len(values):
            px = len(values)
        py += 1
    return ["".join(captcha), (px + 2), 17, lines]