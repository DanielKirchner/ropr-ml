import matplotlib.pyplot as plt
import matplotlib

def main():
    path = r"../raw_data/p000/Pos. 1 - Vorne Nah/data.txt"

    lines = []
    i = 0
    with open(path) as raw:
        for line in raw:
            lines.append(line)

    x = []
    y = []
    names = []
    for chunk in chunks(lines,25):
        for line in chunk:
            splitted = line.split(";")
            x.append(float(splitted[2].replace(",",".")))
            y.append(float(splitted[3].replace(",",".")))
            names.append(splitted[0])
        break

    fig, ax = plt.subplots()
    ax.scatter(x,y,alpha=0.5)
    
    #for i, txt in enumerate(names):
    #    ax.annotate(txt, (x[i],y[i]))

    matplotlib.rcParams.update({'font.size': 24})
    #plt.show()



def chunks(l, n):
    n = max(1, n)
    return (l[i:i+n] for i in xrange(0, len(l), n))

if __name__ == "__main__":
    main()
