#!
import toolbox as tbx
import pprint as pp

seqType, seq = input(
    "Enter the type 'D'-DNA, 'R'-RNA, 'A'-Protein followed by the sequence. Include a space in between the type and sequence\n").upper().split()

#print(seqType, '\n')
#print(seq, '\n')

#
if not tbx.validateseq(seqType, seq):
    print("Invalid sequence. Unexpected character found")

if tbx.validateseq(seqType, seq):
    codontbl = tbx.codoncount(seq)

    print('\n',"Codon Count :",codontbl)

    revComp = tbx.revComplement(seq)
    
    print('\n',"Reverse Complement :",revComp)
    
    print("\n","Possible ORF Postions")
    for frame in range(0,6,1):
        if frame <=2:
            orfPositions=tbx.orfLocator(seq, frame)    
            print("\n","Reading frame ",frame+1,orfPositions)
        elif frame >2:
            orfPositions=tbx.orfLocator(revComp, frame)    
            print("\n","Reading frame ",frame+1,orfPositions)