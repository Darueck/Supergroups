#!/usr/bin/python3
# -*- coding: utf-8 -*-

from glob import glob

sg = '/home/darueck1/artigo/SG/'
omcl = '/home/darueck1/artigo/OMCL/'

acr = []

def scount(fl):
    handler = open(fl, 'r')
    text = handler.read().strip()
    handler.close()
    return(int(text.count('>')))


for fl_path in glob(sg+'*.fa*'):
    sg_c = scount(fl_path)
    sg_name = fl_path.split('/')[-1].strip()
    orth_name = (((sg_name.replace('SG_', 'ORTHOMCL')).split('.')[0])+'.fasta')
    om_c = scount((omcl+orth_name).replace('//','/'))
    print('%s %i\n%s %i\n' % (sg_name, sg_c, orth_name, om_c))
    if sg_c > om_c:
        diff = (sg_c - om_c)
        acr.append('Name:%s\nQTD:%i\nAddition of:%i sequences\nPath:%s' % (sg_name, sg_c, diff, fl_path))


print('\n\n\n'+'---------\n\nIncreased the number of sequences:\n')

for i in acr:
    print(i)
    print()

