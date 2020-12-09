""" The module is a repository for commonly used operations like
sequence formatting, sequence validation, reverse complement, etc.
Will be expanded or modified as required """

import dnaconstants as dc
import timeit as stopclock


def validateseq(seqType, seq):
	if seqType == 'D':
		for nuc in seq:
			if nuc not in dc.dbase:
				return False
	elif seqType == 'R':
		for nuc in seq:
			if nuc not in dc.rbase:
				return False
	elif seqType == 'P':
		for nuc in seq:
			if nuc not in dc.aaResidue:
				return False	
	return True

def codoncount(seq):
	cdn_tbl = dict()
	for idx in range(0,len(seq),3):
		if len(seq[idx:idx+3]) == 3:
			cdn_tbl[seq[idx:idx+3]] = cdn_tbl.get(seq[idx:idx+3],0)+1
	return cdn_tbl

def revComplement(seq):
	revcomp=''
	for base in seq[::-1]:
		if base in dc.dnaBaseComplement:
			revcomp += dc.dnaBaseComplement[base]
	return revcomp

def orfLocator(seq):
	startCodonPos=[]
	stopCodonPos=[]
	for index in range(0,len(seq), dc.codonLength):
		if seq[index:index+3] in dc.dnaStartCd:
			startCodonPos.append(index)
		elif seq[index:index+3] in dc.dnaStopCd:
			stopCodonPos.append(index)
	return[startCodonPos,stopCodonPos]
