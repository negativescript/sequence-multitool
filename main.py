#!
import toolbox as tbx
import pprint as pp

seqType, seq = input(
    "Enter the type 'D'-DNA, 'R'-RNA, 'A'-Protein followed by the sequence. Include a space in between the type and sequence\n").upper().split()

print(seqType, '\n')
print(seq, '\n')


res = tbx.validateseq(seqType, seq)
#
print("res: ", res, '\n')
#
if not tbx.validateseq(seqType, seq):
    print("Invalid sequence. Unexpected character found")

codontbl = tbx.codoncount(seq)

pp.pprint(codontbl)

revComp = tbx.revComplement(seq)

print('\n',"Reverse Complement :",revComp)

orfPositions=tbx.orfLocator(seq)

print("ORF Postions")
print(orfPositions)
