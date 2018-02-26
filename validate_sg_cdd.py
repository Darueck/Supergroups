#!/usr/bin/python3

from glob import glob

supergrp = {}
CDD = {}


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


handler = open('/home/darueck1/artigo/lista_cdd_prt.txt', 'r')
prt_lista = handler.read().strip().split('\n')
handler.close()

for prt in prt_lista:
    prt_id = prt.split()[0]
    if prt_id not in CDD:
        CDD[prt_id] = prt.split()[-1]

del prt_lista


write('sg_EQU_CDD.csv', 'SG,PROTEIN,CDD\n')
write('sg_NO_CDD.csv', 'SG,PROTEIN,CDD\n')
write('sg_DIF_CDD.csv', 'SG,PROTEIN,CDD\n')


rst = []

for sg in supergrp.keys():
    for prt in supergrp[sg]:
        rst.append('%s,%s,%s' % (sg, prt, CDD[prt]))


spf = list(filter((lambda x: ('SEM_' in x)), rst))
spf_grp = list(set(map((lambda x: (x.split(',')[0].strip())), spf)))


no_CDD = sorted(set(filter((lambda x: ((x.split(',')[0].strip()) in spf_grp)), rst)))


for item in no_CDD:
    rst.remove(item)



equ_CDD = []

for grp in set(map((lambda x: (x.split(',')[0])), rst)):
    grp_rst = list(set(filter((lambda x: grp in x), rst)))
    if len(set(map((lambda x: x.split(',')[-1]), grp_rst))) == 1:
        equ_CDD.extend(grp_rst)

equ_CDD = sorted(set(equ_CDD))


for gp in set(map((lambda x: (x.split(',')[0])), equ_CDD)):
    if gp in spf_grp:
        print(gp)


for item in equ_CDD:
    rst.remove(item)


rst = sorted(set(rst))


write('sg_EQU_CDD.csv', ('\n'.join(equ_CDD)))
write('sg_NO_CDD.csv', ('\n'.join(no_CDD)))
write('sg_DIF_CDD.csv', ('\n'.join(rst)))


