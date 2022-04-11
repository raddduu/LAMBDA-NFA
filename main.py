def verify(word,index_litera,stare):
    if index_litera > len(word):
        return
    drum.append(stare)
    if stare in stari_finale and index_litera==len(word):
        global acceptat
        acceptat = 1
        iesire.write("DA\nDrumul este: ")
        for pozitie in drum:
            iesire.write(str(pozitie)+" ")
        iesire.write("\n")
        return
    for i in range(nr_noduri):
        if mat[stare][i] == '#':
            verify(word,index_litera,i)
    for i in range(nr_noduri):
        if mat[stare][i] == word[index_litera]:
            verify(word,index_litera+1,i)
    drum.pop()

intrare = open("date.in","r")
iesire = open("date.out","w")

(nr_noduris,nr_muchiis) = intrare.readline().split()
nr_noduri = int(nr_noduris)
nr_muchii = int(nr_muchiis)

mat = []
acceptat = 0
drum = []

for i in range(nr_noduri):
    lista = []
    for j in range(nr_noduri):
        lista.append(0)
    mat.append(lista)

for i in range(nr_muchii):
    (initials,finals,litera) = intrare.readline().split()
    initial = int(initials)
    final = int(finals)
    mat[initial][final] = litera

stare_initiala = int(intrare.readline())
linie_stari_finale = intrare.readline().split()
nr_stari_finale = int(linie_stari_finale[0])
stari_finale = set()

for i in range(1,nr_stari_finale+1):
    stari_finale.add(int(linie_stari_finale[i]))
nr_cuvinte = int(intrare.readline())

for i in range(nr_cuvinte):
    cuvant = intrare.readline()
    cuvant = cuvant[:-1]
    verify(cuvant,0,0)
    if acceptat == 0:
        iesire.write("NU\n")
    drum.clear()
    acceptat = 0