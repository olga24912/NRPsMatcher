import sys
import networkx as nx
import matplotlib.pyplot as plt
from math import *
from matplotlib import rc

colors = [
"#FF0000",
"#008000",
"#F2B400",
"#0000FF",
"#00308F",
"#FF00FF",
"#800000",
"#00FF00",
"#D3AF37",
"#FF7E00",
"#C9FFE5",
"#0048BA",
"#B0BF1A",
"#F19CBB",
"#AB274F",
"#D3212D",
"#3B7A57",
"#FFBF00",
"#72A0C1",
"#AF002A",
"#F2F0E6",
"#F0F8FF",
"#391802",
"#804040",
"#34B334",
"#FF8B00",
"#FF9899",
"#431C53",
"#B32134",
"#FF033E",
"#CFCFCF",
"#551B8C",
"#9966CC",
"#79C257",
"#7CB9E8",
"#B284BE",
"#5D8AA8",
"#E32636",
"#C46210",
"#EFDECD",
"#D6D6D6",
"#E52B50",
"#9F2B68",
"#A4C639",
"#3B3B6D",
"#CD9575",
"#665D1E",
"#915C83",
"#841B2D",
"#FAEBD7",
"#008000",
"#66B447",
"#8DB600",
"#FBCEB1",
"#00FFFF",
"#7FFFD4",
"#D0FF14",
"#C0C0C0",
"#4B5320",
"#3B444B",
"#8F9779",
"#E9D66B",
"#7DC242",
"#32AD61",
"#66C992",
"#80C197",
"#C86500",
"#CA7309",
"#B2BEB5",
"#87A96B",
"#003A6C",
"#FF9966",
"#A52A2A",
"#FDEE00",
"#6E7F80",
"#568203",
"#FF2052",
"#63775B",
"#007FFF",
"#F0FFFF",
"#DBE9F4",
"#89CFF0",
"#A1CAF1",
"#F4C2C2",
"#FEFEFA",
"#FF91AF",
"#21ABCD",
"#FAE7B5",
"#FFE135",
"#006A4E",
"#E85395",
"#D3419D",
"#F364A2",
"#F7238A",
"#FF3988",
"#FC419A",
"#E94196",
"#E0218A",
"#7C0A02",
"#1DACD6",
"#848482",
"#C3540A",
"#5FC9BF",
"#98777B",
"#BCD4E6",
"#9F8170",
"#F28E1C",
"#FA6E79",
"#F5F5DC",
"#2E5894",
"#9C2542",
"#E88E5A",
"#FFE4C4",
"#3D2B1F",
"#967117",
"#CAE00D",
"#BFFF00",
"#FE6F5E",
"#BF4F51",
"#000000",
"#3D0C02",
"#1B1811",
"#3B2F2F",
"#54626F",
"#253529",
"#3B3C36",
"#8F5973",
"#16110D",
"#BFAFB2",
"#FFEBCD",
"#A57164",
"#318CE7",
"#ACE5EE",
"#FAF0BE",
"#8A0303",
"#D1001C",
"#660000",
"#A41313",
"#630F0F",
"#0000FF",
"#1F75FE",
"#0093AF",
"#0087BD",
"#0018A8",
"#333399",
"#0247FE",
"#A2A2D0",
"#00B9FB",
"#0088DC",
"#6699CC",
"#0D98BA",
"#064E40",
"#5DADEC",
"#ACE5EE",
"#553592",
"#0095B6",
"#0CBFE9",
"#126180",
"#8A2BE2",
"#7366BD",
"#4D1A7F",
"#5072A7",
"#4F86F7",
"#1C1CF0",
"#DE5D83",
"#79443B",
"#E3DAC9",
"#DDE26A",
"#CC0000",
"#006A4E",
"#873260",
"#0E9CA5",
"#0070FF",
"#87413F",
"#B5A642",
"#FF631C",
"#CB4154",
"#1DACD6",
"#EBECF0",
"#66FF00",
"#BF94E4",
"#D891EF",
"#C32148",
"#1974D2",
"#FF007F",
"#08E8DE",
"#D19FE8",
"#FFAA1D",
"#3399FF",
"#F4BBFF",
"#FF55A3",
"#FB607F",
"#004225",
"#88540B",
"#CD7F32",
"#B08D57",
"#737000",
"#993300",
"#AF593E",
"#964B00",
"#A52A2A",
"#6B4423",
"#AF6E4D",
"#5F1933",
"#4A2C2A",
"#CC9966",
"#1B4D3E",
"#FFC1CC",
"#E7FEFF",
"#7BB661",
"#F0DC82",
"#480607",
"#800020",
"#DEB887",
"#A17A74",
"#CC5500",
"#E97451",
"#8A3324",
"#CAAC6E",
"#24A0ED",
"#BD33A4",
"#702963",
"#536872",
"#5F9EA0",
"#A9B2C3",
"#91A3B0",
"#0A1195",
"#006B3C",
"#ED872D",
"#B60C26",
"#E30022",
"#FFF600",
"#7F3E98",
"#A67B5B",
"#4B3621",
"#1E4D2B",
"#FCFFA4",
"#A3C1AD",
"#C19A6B",
"#EFBBCC",
"#78866B",
"#FFFF99",
"#FFEF00",
"#FF0800",
"#E4717A",
"#00BFFF",
"#592720",
"#FFD59A",
"#C41E3A",
"#00CC99",
"#1AC1DD",
"#960018",
"#D70040",
"#EB4C42",
"#FF0038",
"#FFA6C9",
"#B31B1B",
"#56A0D3",
"#ED9121",
"#00563F",
"#062A78",
"#703642",
"#C95A49",
"#92A1CF",
"#ACE1AF",
"#007BA7",
"#2F847C",
"#B2FFFF",
"#4997D0",
"#246BCE",
"#DE3163",
"#EC3B83",
"#007BA7",
"#2A52BE",
"#001440",
"#6D9BC3",
"#1DACD6",
"#007AA5",
"#E03C31",
"#A0785A",
"#F7E7CE",
"#F1DDCF",
"#36454F",
"#232B2B",
"#D0748B",
"#E68FAC",
"#DFFF00",
"#7FFF00",
"#FFA600",
"#DE3163",
"#FFB7C5",
"#954535",
"#FFC34D",
"#DE6FA1",
"#A8516E",
"#141414",
"#365194",
"#CD8032",
"#AB381F",
"#D0DB61",
"#CC9900",
"#F37042",
"#DE70A1",
"#720B98",
"#CD071E",
"#AA381E",
"#CCCCCC",
"#856088",
"#E2E5DE",
"#FFB200",
"#4AFF00",
"#3F000F",
"#58111A",
"#3C1421",
"#7B3F00",
"#D2691E",
"#2A8FBD",
"#365194",
"#5D2B2C",
"#4C1F02",
"#3C8D0D",
"#007502",
"#CAA906",
"#FF6600",
"#D56C2B",
"#FFCCCB",
"#E34285",
"#663398",
"#4D084B",
"#AA0114",
"#B01B2E",
"#E1DFE0",
"#FFCC00",
"#FEF200",
"#A8A9AD",
"#FFA700",
"#98817B",
"#E34234",
"#D2691E",
"#CD607E",
"#E4D00A",
"#933709",
"#9FA91F",
"#7F1734",
"#FBCCE7",
"#0047AB",
"#D2691E",
"#965A3E",
"#E9EDF6",
"#6F4E37",
"#3C3024",
"#C4D8E2",
"#FFFFCC",
"#F88379",
"#002E63",
"#8C92AC",
"#EEE0B1",
"#B87333",
"#DA8A67",
"#AD6F69",
"#CB6D51",
"#996666",
"#FF3800",
"#FF7F50",
"#F88379",
"#FF4040",
"#FD7C6E",
"#F6A494",
"#893F45",
"#FBEC5D",
"#B31B1B",
"#6495ED",
"#93CCEA",
"#FFF8DC",
"#2E2D88",
"#FFF8E7",
"#81613C",
"#FFBCD9",
"#FFFDD0",
"#DC143C",
"#BE0032",
"#990000",
"#A7D8DE",
"#68A0B0",
"#F5F5F5",
"#00FFFF",
"#4E82B4",
"#4682BF",
"#28589C",
"#188BC2",
"#00B7EB",
"#58427C",
"#FFD300",
"#F56FA1",
"#FFFF31",
"#F0E130",
"#FDDB6D",
"#00008B",
"#666699",
"#804A00",
"#514100",
"#654321",
"#88654E",
"#5D3954",
"#A40000",
"#08457E",
"#333333",
"#986960",
"#490206",
"#3C1321",
"#26428B",
"#CD5B45",
"#008B8B",
"#536878",
"#AA6C39",
"#B8860B",
"#A9A9A9",
"#013220",
"#006400",
"#1F262A",
"#00416A",
"#00147E",
"#1A2421",
"#BDB76B",
"#483C32",
"#734F96",
"#8BBE1B",
"#534B4F",
"#543D37",
"#8B008B",
"#A9A9A9",
"#003366",
"#4A5D23",
"#02075D",
"#556B2F",
"#FF8C00",
"#9932CC",
"#779ECB",
"#03C03C",
"#966FD6",
"#C23B22",
"#E75480",
"#003399",
"#4F3A3C",
"#301934",
"#872657",
"#8B0000",
"#E9967A",
"#560319",
"#8FBC8F",
"#3C1414",
"#71706E",
"#8CBED6",
"#483D8B",
"#2F4F4F",
"#177245",
"#918151",
"#FFA812",
"#483C32",
"#CC4E5C",
"#00CED1",
"#D1BEA8",
"#9400D3",
"#9B870C",
"#00703C",
"#555555",
"#D70A53",
"#9C8AA4",
"#40826D",
"#A9203E",
"#EF3038",
"#E9692C",
"#DA3287",
"#FAD6A5",
"#B94E48",
"#704241",
"#9B351B",
"#C154C1",
"#056608",
"#0E7C61",
"#004B49",
"#333366",
"#F5C71A",
"#9955BB",
"#CC00CC",
"#820000",
"#D473D4",
"#355E3B",
"#FFCBA4",
"#FF1493",
"#A95C68",
"#850101",
"#843F5B",
"#FF9933",
"#00BFFF",
"#4A646C",
"#556B2F",
"#7E5E60",
"#66424D",
"#330066",
"#BA8759",
"#1560BD",
"#2243B6",
"#669999",
"#C19A6B",
"#EDC9AF",
"#EA3C53",
"#B9F2FF",
"#696969",
"#C53151",
"#9B7653",
"#B5651E",
"#E8E4C9",
"#1E90FF",
"#FEF65B",
"#D71868",
"#85BB65",
"#828E84",
"#2496CD",
"#2E963D",
"#F7C58E",
"#967117",
"#00009C",
"#B07939",
"#E6D0AB",
"#E1BD27",
"#E5CCC9",
"#EFDFBB",
"#5D3A1A",
"#E1A95F",
"#555D50",
"#C2B280",
"#1B1B1B",
"#614051",
"#F0EAD6",
"#1034A6",
"#17182B",
"#7DF9FF",
"#B56257",
"#FF003F",
"#00FFFF",
"#00FF00",
"#6F00FF",
"#F4BBFF",
"#CCFF00",
"#FF3503",
"#F62681",
"#BF00FF",
"#E60000",
"#3F00FF",
"#8F00FF",
"#FFFF33",
"#50C878",
"#046307",
"#6C3082",
"#1B4D3E",
"#B48395",
"#AB4B52",
"#CC474B",
"#563C5C",
"#96C8A2",
"#44D7A8",
"#39569C",
"#C19A6B",
"#801818",
"#B53389",
"#DE5285",
"#F400A1",
"#E5AA70",
"#4D5D53",
"#FDD5B1",
"#4F7942",
"#FF2800",
"#6C541E",
"#FF5470",
"#B22222",
"#CE2029",
"#E95C4B",
"#E25822",
"#FC8EAC",
"#6B4423",
"#F7E98E",
"#EEDC82",
"#FFE9D1",
"#216BD6",
"#FB0081",
"#A2006D",
"#FFFAF0",
"#F498AD",
"#15F4EE",
"#FFBF00",
"#FF1493",
"#CCFF00",
"#FF004F",
"#5FA777",
"#014421",
"#228B22",
"#A67B5B",
"#856D4D",
"#0072BB",
"#FD3F92",
"#86608E",
"#9EFD38",
"#D473D4",
"#FD6C9E",
"#811453",
"#4E1609",
"#C72C48",
"#F64A8A",
"#77B5FE",
"#8806CE",
"#AC1E44",
"#A6E7FF",
"#E936A7",
"#FF00FF",
"#C154C1",
"#FF77FF",
"#CC397B",
"#C74375",
"#E48400",
"#CC6666",
"#4C2F27",
"#F2F3F4"];

detailMolFN = "/home/olga/bio/NRP/data/bacteria_complete/details_mols/streptomedb.84" #sys.argv[1]
predictionFN = "/home/olga/bio/NRP/data/bacteria_complete/predictions/GCF_000203835.1_ASM20383v1_genomic"#sys.argv[2]
molName = "streptomedb.84"#sys.argv[4]
genomeName = "GCF_000203835.1_ASM20383v1_genomic"#sys.argv[5]

G = nx.Graph()
g = []
color = dict()

def SplitBranchCicle():
    v = 0
    for i in range(len(g)):
        if (len(g[i]) == 0):
            v = i
    line = []
    circl = []
    line.append(v)
    u = v
    v = g[v][0]
    while (len(g[v]) == 2):
        line.append(v)
        if (g[v][0] != u):
            u = v
            v = g[v][0]
        else:
            u = v
            v = g[v][1]

    start = v
    circl.append(v)
    if (g[v][0] != u):
        u = v
        v = g[v][0]
    else:
        u = v
        v = g[v][1]
        
    while (v != start):
        circl.append(v)
        if (g[v][0] != u):
            u = v
            v = g[v][0]
        else:
            u = v
            v = g[v][1]
    return (circl, line)
    

def hasLeaf():
    for i in range(len(g)):
        if (len(g[i]) == 1):
            return True
    return False

def SplitGraph():
    if (hasLeaf()):
        return SplitBranchCicle()
    circ = []
    circ.append(0)
    u = 0
    v = g[0][0]
    while (v != 0):
        circ.append(v)
        if (g[v][0] != u):
            u = v
            v = g[v][0]
        else:
            u = v
            v = g[v][1]
    return (circ, [])
    

choosePred = dict()
usedOrfs = set()

info = ""
score = ""

def ParseExtraInfo(s):
    global info
    info = ' '.join(s.split(' ')[1:])
    print(info)
    print(s)

def ParseScore(s):
    global score
    score = s.split(' ')[-1]
    

def parseGraph():
    with open(detailMolFN) as f:
        lines = f.readlines()
        cur = 0
        while (molName not in lines[cur]) or (genomeName not in lines[cur + 1]):
            while (cur < len(lines) and lines[cur] != "\n"):
                cur += 1
            while (cur < len(lines) and lines[cur] == "\n"):
                cur += 1

        ParseExtraInfo(lines[cur])
        ParseScore(lines[cur + 2])
        cur += 5 # cnt prefix line
        n = int(lines[cur].split(' ')[-1])
        cur += 1
        vertInfo = []
        nodecolor = [0]*n
        labels = dict()
        for i in range(n):
            g.append([])
            vertInfo.append(lines[cur].split(' '))
            if (vertInfo[-1][-1] == '-\n'):
                vertInfo[-1].append('-')
                vertInfo[-1].append('-')
                vertInfo[-1].append('-')
            G.add_node(i)
            nodecolor[i] = color[vertInfo[-1][-2]]
            labels[i] = ""
            if (vertInfo[-1][4] != "-\n"):
                labels[i] = vertInfo[-1][4].split('(')[0] + "\n" + "(" + vertInfo[-1][4].split('(')[1] + " " + vertInfo[-1][5] + "\n"
            if (vertInfo[-1][1] != "-"):
                labels[i] += vertInfo[-1][1] + "\n"
            if (vertInfo[-1][-2] != "-"):
                labels[i] += vertInfo[-1][-2] + " " + vertInfo[-1][-1] + "\n"
                usedOrfs.add(vertInfo[-1][-2])
            labels[i] += "\n\n\n\n"
            if (vertInfo[-1][4] != "-\n"):
                if (vertInfo[-1][-2] not in choosePred):
                    choosePred[vertInfo[-1][-2]] = dict()
                choosePred[vertInfo[-1][-2]][int(vertInfo[-1][-1])] = vertInfo[-1][4].split('(')[0]

            cur += 1
            

        m = int(lines[cur].split(' ')[-1])
        cur += 1
        for i in range(m):
            G.add_edge(int(lines[cur].split(' ')[0]), int(lines[cur].split(' ')[-1]))
            g[int(lines[cur].split(' ')[0])].append(int(lines[cur].split(' ')[-1]))
            g[int(lines[cur].split(' ')[-1])].append(int(lines[cur].split(' ')[0]))
            cur += 1

        circ, line = SplitGraph()

        pos = dict()
        step = 60
        cur = step
        for i in range(len(line) - 1, -1, -1):
            pos[line[i]] = (cur, 0)
            cur += step

        if (len(circ) != 0):
            anglStep = 2*pi/len(circ)
            curA = 0
            R = len(circ) * 10
            for i in range(len(circ)):
                x = R * cos(curA) - R
                y = R * sin(curA)
                pos[circ[i]] = (x, y)
                curA += anglStep
                
        
        nx.draw(G, pos=pos, node_color = nodecolor, labels=labels, node_size=600)
        plt.savefig('pic.png')
        print(lines)

predictionInfo = dict()
predictionList = []
def parsePrediction():
    with open(predictionFN) as f:
        lines = f.readlines()
        for line in lines:
            spl = line.split('\t')
            orfname = spl[0]
            orfname = orfname.split('_')[1]
            num = int(spl[0].split('_')[-1][1:]) - 1
            if (orfname not in predictionInfo):
                predictionInfo[orfname] = []
                predictionList.append(orfname)
                color[orfname] = colors[len(predictionList) - 1]
            predictionInfo[orfname].append([])
            predictionInfo[orfname][num] = spl[-1].split(';')
    color['-'] = "#000000"
    
def drawPrediction():
    fig = plt.figure(figsize=(15,15))
    ax = fig.add_subplot(111)

    stepY = -30
    curY = 0
    maxX = 0
    for orf in predictionList:
        text = orf
        stepX = 30
        curX = 60
        ax.text(0, curY - 5, text,  fontweight='bold', color=color[orf])
        for i in range(len(predictionInfo[orf])):
            for j in range(3):
                if (orf in choosePred):
                    print(choosePred[orf])
                if (orf in choosePred) and (i in choosePred[orf]) and (choosePred[orf][i].split('-')[-1] == predictionInfo[orf][i][j].split('(')[0]):
                    ax.text(curX, curY - 5 * j, predictionInfo[orf][i][j], fontweight='bold')
                else:
                    ax.text(curX, curY - 5 * j, predictionInfo[orf][i][j])
            curX += stepX
        curY += stepY
        maxX = max(maxX, curX)

    ax.axis([ 0, maxX, curY, 0])
    ax.set_axis_off()
    plt.savefig('pic2.png')


def createHead(fw):
    fw.write("<!DOCTYPE html>\n");
    fw.write("<html lang=\"en\">\n");
    fw.write("<head>\n");
    fw.write("    <meta charset=\"UTF-8\">\n");
    fw.write("    <meta name=\"viewport\" content=\"width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0, minimal-ui\">\n");
    fw.write("    <title>NRPmathcher</title>\n");
    fw.write("    <style>")
    fw.write("    th, td {border-bottom: 1px solid #ddd; text-align: left;}")
    fw.write("    </style>")
    fw.write("</head>\n")
    fw.write("<body>\n")
            

def createTop(fw):
    fw.write("    <div class=\"top\" style=\"position: fixed;height: 60px;left: 0px;right: 0px;top:0px;")
    fw.write("background: #E4E4E4;border: 1px solid #BDBDBD;box-sizing: border-box;padding-left: 10px;padding-right: 10px;\">\n")
    fw.write("        <span style=\"font-family: Roboto;font-style: normal;font-weight: bold;line-height: normal;font-size: 48px;color: #000000;\">NRPmatcher</span>")
    fw.write("</div>")

def createInfoPanel(fw):
    fw.write("    <div style=\"position: fixed;width: 350px;bottom: 0px;right: 0px;top:59px;border: 1px solid#BDBDBD;\"> \n")
    fw.write("     <div style=\"margin-left: 10px;\">")
    fw.write("    <p><b>Score:</b> " + score + "</p>\n")
    fw.write("    <p><b>Mol ID:</b> " + molName + "</p>\n")
    fw.write("    <p>" + info + "</p>\n") 
    fw.write("    <p><b>Genome ID:</b> " + genomeName + "</p>\n")
    fw.write("    </div>\n")
    fw.write("    </div>\n")

def createPic(fw):
    fw.write("    <div style=\"overflow:scroll; position: fixed;left:0px; bottom:0px; top:60px;right: 351px;\">\n")
    fw.write("        <table style=\"width:100%;border: 1px solid black;border-collapse: collapse;\">\n")

    mxlen = 0
    cntOrfs = [0]*30
    for orf in predictionList:
        if orf not in usedOrfs:
            cntOrfs[len(predictionInfo[orf])] += 1
            continue
        mxlen = max(mxlen, len(predictionInfo[orf]))
    
    for orf in predictionList:
        if orf not in usedOrfs:
            continue
        fw.write("        <tr>\n")
        fw.write("        <th rowspan=\"3\" style = \"padding: 10px\">" + orf + "</th>\n")
        for j in range(3):
            for i in range(len(predictionInfo[orf])):
                if (j == 0):
                    style = "\"padding-top: 10px; border-bottom: 1px solid #fff\""
                if (j == 1):
                    style = "\"border-bottom: 1px solid #fff\""    
                if (j == 2):
                    style = "\"padding-bottom: 10px;\""
                if (orf in choosePred) and (i in choosePred[orf]) and (choosePred[orf][i].split('-')[-1] == predictionInfo[orf][i][j].split('(')[0]):
                    fw.write("        <td style=" + style + "><font color=" + color[orf] + "><b>" + predictionInfo[orf][i][j] + "</b></font></td>\n")
                else:
                    fw.write("        <td style=" + style + ">" + predictionInfo[orf][i][j] + "</td>\n")
            for i in range(len(predictionInfo[orf]), mxlen):
                if (j == 0):
                    style = "\"padding-top: 10px; border-bottom: 1px solid #fff\""
                if (j == 1):
                    style = "\"border-bottom: 1px solid #fff\""    
                if (j == 2):
                    style = "\"padding-bottom: 10px;\""
                fw.write("        <td style=" + style + ">""</td>\n")
                
            fw.write("        </tr>\n")
            if j != 2:
                fw.write("        <tr>\n")

    fw.write("        </table>\n")
    orfsInfo = ""
    for i in range(29, 0, -1):
        if cntOrfs[i] != 0:
            orfsInfo += str(i) + " AA: " + str(cntOrfs[i]) + ";    " 
                    
    fw.write("        <pre> " + str(sum(cntOrfs)) + " more orfs:    "+ orfsInfo + "</pre>")
    fw.write("        <img src=\"pic.png\" style=\"max-width: 700px;width:100%;display: block;margin-left: auto;margin-right: auto;margin-top: 50px;\">\n")
    fw.write("    </div>\n")

def createEnd(fw):
    fw.write("</body>\n")
    fw.write("</html>\n")
    

def generatePic():
    pass

parsePrediction()
parseGraph()
with open("main.html", "w") as fw:
    createHead(fw)
    createTop(fw)
    createInfoPanel(fw)
    generatePic()
    createPic(fw)
    createEnd(fw)
    
