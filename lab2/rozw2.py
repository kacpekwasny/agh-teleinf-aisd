
"""Two letter prefix consists of following ascii chars"""
def ascii_pref(string):
    if len(string) < 2:
        return False
    ch1, ch2 = string[:2]
        # the chars are following
    return abs(ord(ch1)-ord(ch2)) == 1


def main():
    in_name = "zadanie2.csv"
    out_name = "out_zadanie2.csv"
    lines = open(in_name, "r").read().splitlines()
    idval = [] # list of [ID, VALUE] example: [1234, "Lorem ipsum dores..."]
    for l in lines[1:]:
        split = l.split(",")
        id_ = int(split[0])

        # podpunkt 5
        val = ",".join(split[1:]).lower()
        if val.strip() == "":
            continue
        words = val.split(" ")
        for i, word in enumerate(words):
            if ascii_pref(word):
                if word[-1] == ",":
                    words[i] = ","
                    print(word)
                else:
                    print(words.pop(i))
    
        idval.append([id_, val])

    lines = sorted(idval, key=lambda x: x[0])
    last_id = -999
    for kv in lines: # kv = [id, val]
        print(last_id, kv[0])
        if kv[0] <= last_id:
            kv[0] = last_id + 1
            last_id += 1
            continue
        last_id = kv[0]

    with open(out_name, "w") as f:
        f.writelines([f"{id_},{val}\n" for id_, val in lines])


    

if __name__ == "__main__":
    main()