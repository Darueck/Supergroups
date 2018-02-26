#!/usr/bin/python3

from glob import glob

supergrp = {}
PFAM = {}


def write(file_path, content):
    handler = open(file_path, 'a')
    handler.write(content)
    handler.close()




for fasta in glob('/home/darueck1/artigo/SG/*.fa'):
    handler = open(fasta, 'r')
    content = (set(handler.read().strip().split('\n')))
    handler.close()
    temp_seq = list(filter((lambda x: ('>' in x)), content))
    temp_seq = list(map((lambda x: (x.replace('>',''))), temp_seq))
    for seq in temp_seq:
        prot_id = seq.split()[0]
        seq = (seq.replace(prot_id, '')).strip()
        sg = ((fasta.split('/')[-1]).split('.')[0].strip())
        if sg not in supergrp:
            supergrp[sg] = []
            supergrp[sg].append(prot_id)
        else:
            supergrp[sg].append(prot_id)
    handler.close()


handler = open('/home/darueck1/artigo/lista_pfam_prt.txt', 'r')
prt_lista = handler.read().strip().split('\n')
handler.close()

for prt in prt_lista:
    prt_id = prt.split()[0]
    if prt_id not in PFAM:
        PFAM[prt_id] = prt.split()[-1]

del prt_lista


write('sg_EQU_PFAM.csv', 'SG,PROTEIN,PFAM\n')
write('sg_NO_PFAM.csv', 'SG,PROTEIN,PFAM\n')
write('sg_DIF_PFAM.csv', 'SG,PROTEIN,PFAM\n')


rst = []

for sg in supergrp.keys():
    for prt in supergrp[sg]:
        rst.append('%s,%s,%s' % (sg, prt, PFAM[prt]))


spf = list(filter((lambda x: ('SEM_' in x)), rst))
spf_grp = list(set(map((lambda x: (x.split(',')[0].strip())), spf)))


no_PFAM = sorted(set(filter((lambda x: ((x.split(',')[0].strip()) in spf_grp)), rst)))


for item in no_PFAM:
    rst.remove(item)



equ_PFAM = []

for grp in set(map((lambda x: (x.split(',')[0])), rst)):
    grp_rst = list(set(filter((lambda x: grp in x), rst)))
    if len(set(map((lambda x: x.split(',')[-1]), grp_rst))) == 1:
        equ_PFAM.extend(grp_rst)

equ_PFAM = sorted(set(equ_PFAM))


for gp in set(map((lambda x: (x.split(',')[0])), equ_PFAM)):
    if gp in spf_grp:
        print(gp)


for item in equ_PFAM:
    rst.remove(item)


rst = sorted(set(rst))


write('sg_EQU_PFAM.csv', ('\n'.join(equ_PFAM)))
write('sg_NO_PFAM.csv', ('\n'.join(no_PFAM)))
write('sg_DIF_PFAM.csv', ('\n'.join(rst)))


