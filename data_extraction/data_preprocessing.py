#nodes
names = []
unif = open("../data/uni.csv","w",encoding='utf8')
unif.write("uni,name,type,symbol,monitored,url\n")
telef = open("../data/tele.csv","w",encoding='utf8')
telef.write("tele,name,type,symbol,monitored,url\n")
polyf = open("../data/poly.csv","w",encoding='utf8')
polyf.write("poly,name,type,symbol,monitored,url\n")
gof = open("../data/go.csv","w",encoding='utf8')
gof.write("go,name,type,symbol,monitored,url\n")
miscf = open("../data/misc.csv","w",encoding='utf8')
miscf.write("misc,name,type,symbol,monitored,url\n")
legalf = open("../data/legal.csv","w",encoding='utf8')
legalf.write("legal,name,type,symbol,monitored,url\n")
stif = open("../data/sti.csv","w",encoding='utf8')
stif.write("sti,name,type,symbol,monitored,url\n")
#relationships
un = open("../data/uni_name.csv","w",encoding='utf8')
un.write("uni,name\n")
pn = open("../data/poly_name.csv","w",encoding='utf8')
pn.write("poly,name\n")
tn = open("../data/tele_name.csv","w",encoding='utf8')
tn.write("tele,name\n")
gn = open("../data/go_name.csv","w",encoding='utf8')
gn.write("go,name\n")
mn = open("../data/misc_name.csv","w",encoding='utf8')
mn.write("misc,name\n")
ln = open("../data/legal_name.csv","w",encoding='utf8')
ln.write("legal,name\n")
sn = open("../data/sti_name.csv","w",encoding='utf8')
sn.write("sti,name\n")
#University
uni = open("uni.csv","r",encoding='utf8')
c = ""
h = ""
s = []
for line in uni:
    if len(line) <= 3:
        unif.write(c + "," + ";".join(s) + ",University,NA,Public Service Comission," + h +"\n")
        c= ""
        h= ""
        s=[]
    elif c == "":
        c= line.split(",,")[0]
        h = line.split(",,")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))      
        un.write(c + "," + " ".join(name) + "\n")
unif.write(c + "," + ";".join(s) + ",University,NA,Public Service Comission," + h +"\n")      
uni.close()
unif.close()
un.close()
#Telecommunication
tele =  open("tele.csv","r",encoding='utf8')
c= ""
h= ""
s= []
for line in tele:
    if len(line) <= 3:
        telef.write(c + "," + ";".join(s) + ",Telecommunication,NA,Public Service Comission," + h +"\n")
        c= ""
        h= ""
        s=[]
    elif c == "":
        c= line.split(",,")[0]
        h = line.split(",,")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))      
        tn.write(c + "," + " ".join(name) + "\n")
telef.write(c + "," + ";".join(s) + ",Telecommunication,NA,Public Service Comission," + h +"\n")
tele.close()
telef.close()
tn.close()
#Polytechnic
poly =  open("poly.csv","r",encoding='utf8')
c= ""
h= ""
s= []
for line in poly:
    if len(line) <= 3:
        polyf.write(c + "," + ";".join(s) + ",Polytechnic,NA,Public Service Comission," + h +"\n")
        s=[]
        c= ""
        h= ""
    elif c == "":
        c= line.split(",,")[0]
        h = line.split(",,")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))    
        pn.write(c + "," + " ".join(name) + "\n")
polyf.write(c + "," + ";".join(s) + ",Polytechnic,NA,Public Service Comission," + h +"\n")
poly.close()
polyf.close()
pn.close()
#Government Organisation
go =  open("go.csv","r",encoding='utf8')
c= ""
h= ""
s= []
for line in go:
    if len(line) <= 3:
        gof.write(c + "," + ";".join(s) + ",Government Organisation,NA,Public Service Comission," + h +"\n")
        s=[]
        c= ""
        h= ""
    elif c == "":
        c= line.split(",,")[0]
        h = line.split(",,")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))      
        gn.write(c + "," + " ".join(name) + "\n")
gof.write(c + "," + ";".join(s) + ",Government Organisation,NA,Public Service Comission," + h +"\n")
go.close()
gof.close()
gn.close()
#Legal Institution
legal =  open("legal.csv","r",encoding='utf8')
c= ""
h= ""
s= []
for line in legal:
    if len(line) <= 3:
        legalf.write(c + "," + ";".join(s) + ",Legal Institution,NA,NA," + h +"\n")
        s=[]
        c= ""
        h= ""
    elif c == "":
        c= line.split(",")[0]
        h = line.split(",")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))      
        ln.write(c + "," + " ".join(name) + "\n")
legalf.write(c + "," + ";".join(s) + ",Legal Institution,NA,NA," + h +"\n")
legal.close()
legalf.close()
ln.close()
#Misc
misc =  open("misc.csv","r",encoding='utf8')
c= ""
h= ""
s= []
for line in misc:
    if len(line) <= 3:
        miscf.write(c + "," + ";".join(s) + ",Misc,NA,NA," + h +"\n")
        s=[]
        c= ""
        h= ""
    elif c == "":
        c= line.split(",")[0]
        h = line.split(",")[1].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name)) 
        mn.write(c + "," + " ".join(name) + "\n")
miscf.write(c + "," + ";".join(s) + ",Misc,NA,NA," + h +"\n")
misc.close()
miscf.close()
mn.close()
#STI
stid = open("stid.csv","r")
s = []
c= ""
h= ""
sym = ""
for line in stid:
    if len(line) <= 9:
        stif.write(c + "," + ";".join(s) + ",Misc," + sym + ",Public Service Comission;Esplanade;IPOS," + h +"\n")
        s=[]
        c= ""
        h= ""
        sym = ""
    elif c == "":
        c= line.split(",,")[0]
        h = line.split(",,")[1].strip().strip(",")
        sym = line.split(",,")[2].strip().strip(",")
    else:
        line = str(line).strip().replace(",","").replace('"',"")
        name = []
        for i in line.split(" "):
            if len(i) > 1:
                if i[1] != ".":
                    s1 = i[0].upper()
                    s2 = i[1:].lower()
                    name.append(s1+s2)
                else:
                    name.append(i)
            else:
                name.append(i)
        names.append(" ".join(name))
        s.append(" ".join(name))      
        sn.write(c + "," + " ".join(name) + "\n")
stif.write(c + "," + ";".join(s) + ",Misc," + sym + ",Public Service Comission;Esplanade;IPOS," + h +"\n")
stid.close()
stif.close()
sn.close()
na = open("../data/name.csv","w",encoding='utf8')
na.write("name\n")
for i in set(names):
    na.write(i + "\n")
na.close()