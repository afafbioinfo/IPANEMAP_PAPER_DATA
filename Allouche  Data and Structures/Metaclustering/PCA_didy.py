import Functions as mylibrary

import collections 
from collections import defaultdict
#import Diana as Dn
#import draw3dPareto
#rna=Functions.ParseFasta(rnafile,"RNAfold")
#numberssamples=len(constraintes)

if __name__ == '__main__':
    
    #constraintes=["didyNO","didy1M7", "didy1M7Mg", "didyNMIA", "didyNMIAMg", "didyBzCNMg", "didyCMCTMg",  "didyNaiMg","didyDMSMg","didyNai", "didyNMIAMgCE","didy1M7ILU3","didy1M7ILU","didy1M7ILU3Mg","didy1M7ILUMg"]
    constraintes=["didyThermo","didy1M7CE","didy1M7MgCE", "didyNMIA", "didyNMIAMg", "didyNMIACE", "didyNMIAMgCE", "didyBzCNMg", "didyBzCN", "didyCMCTMg",  "didyNaiMg","didyDMSMg","didyNai","didy1M7ILU3","didy1M7ILU","didy1M7ILU3Mg","didy1M7ILUMg"]

    #constraintes=["didyThermo","didy1M7Mg", "didyNMIA", "didyNMIAMg", "didyNMIAMgCE", "didyBzCNMg","didyCMCTMg",  "didyNaiMg","didyDMSMg","didy1M7ILU3","didy1M7ILU","didy1M7ILU3Mg","didy1M7ILUMg","didy1M7CE","didy1M7MgCE"]
 
    #constraintes=["a83uDMS","a152uDMS","a223uDMS","c102gDMS","c219gDMS","c247gDMS","didyDMS","g101cDMS","g134cDMS","u123aDMS","u163aDMS"]
    rna=mylibrary.Parsefile(rnafile)[1]
    startimebig=time.time()

    print '**************Calculation of Eucledian distance between different BP dot plot conditions**********'
    #mylibrary.plotClusteringDistribution(numberofsruct,Matrixproba,len(rna))

    mylibrary.DotplotRnaFold(Psdotpath,PathConstrainteFile,PathConstrainteFileShape)

    mylibrary.Writeproba(Psdotpath,Matrixproba,constraintes,rna)

    mylibrary.plotClusteringDistribution(int(numberofsruct),Matrixproba,len(rna))
    print "Eucledian distance done"
