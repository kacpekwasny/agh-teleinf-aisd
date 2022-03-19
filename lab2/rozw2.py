


def main():
    in_name = "zadanie2.csv"
    out_name = "out_" + in_name
    id_val = []
    with open(in_name, "r") as f:
        while l := f.readline():
            l = l.split(",")
            if l[1].replace(" ", "") == "":
                continue
            id_val = [int(l[0].strip()), l[1].lower()]
        
    lines = sorted(id_val, key=lambda x: x[0])

    ajdi = -999
    for kv in lines: # kv = [id, val]
        if kv[0] == ajdi:
            kv[0] = ajdi + 1
            ajdi += 1
            continue
        ajdi = kv[0]
            


    

if __name__ == "__main__":
    main()