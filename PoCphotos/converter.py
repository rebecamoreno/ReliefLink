import sys

def dont_ask(inpath, outpath):
    byte2str = ["{:08b}".format(i) for i in range(256)]
    with open(inpath, "rb") as fin:
        with open(outpath, "w") as fout:
            data = fin.read(1024)  # doesn't much matter
            while data:
                for b in map(ord, data):
                    fout.write(byte2str[b])
                data = fin.read(1024)

name = ((sys.argv[1]).split('.'))[0]+'.bin'
dont_ask(sys.argv[1], name)