'''****************************************'''

##    python TestSeqs.py overlap overlapTestFiles
##    python TestSeqs.py [testType] [outputFolder] [option=value]
##    python TestSeqs.py overlap overlapTestFiles vectors=10000 dim=1000

'''*************** OPTIONS ****************

    **General Options**
        -infile (default null)    -File for input data generation
    
        -scaling (default true)     -Toggle scaling of generated data
        -minValue (default -.999)    -Max value of output data
        -maxValue (default .999)    -Min value of output data
        
        -dim (default 100)        -Number of significant columns to generate
        -dummyCols (default 50) -Number of uncorrelated columns to generate
        
        -clusters (default 3)    -Number of clusters to generate
        -vectors (default 1000)    -Number of vectors to generate

        -charts (default pdf)     -Generated chart format (save, show, none, all, png, pdf)
    ____________________________________

    **Generation Distribution Options**
        -dist (default gauss)    -Distribution to generate points on
            -gauss or normal        -Generate points on gaussian distribution
            -uniform or uni         -Generate points uniformly
            -binomial or binom      -Generate points using a binomial distribution
            -exponential or exp     -Generate points using an exponential distribution
    ____________________________________
   
    **CENTROID OPTIONS**
        -corg (default random)     -Organization of clusters to be generated (pairs, triplets, etc.)
                                    -random, bi, tri, quad, all
        -cdist (default .4)     -Target distance of cluster centroid orgs
        -csigma (default .1)    -Deviation of a cluster
        -ccounts (default random) -Cluster counts to partition total vectors into
                                    -random, equal, (TODO)separated
    ____________________________________

    **Output Randomization Options**
        -rshuf (default true)  (true, false) -Randomize the vectors (Rows)
        -cshuf (default random) (separated, intermixed, random)
                                    -Determine how to shuffle the columns; separated keeps significant
                                        columns stacked on low indexed features and dummy columns on 
                                        high indexed features; intermixed disperses evenly; random
                                        performs a shuffle on the columns
        -noise (default 0%) (0-1)  -TODO Amount of noise to add to final output
    ____________________________________

```****************************************'''

from MultiRun import *


def overlapTest(argsDict, foName):
    argsDict['clusters'] = [4]
    argsDict['csigma'] = [.05]
    argsDict['corg'] = ['bi']
    argsDict['vectors'] = [1000]
    
    if not os.path.exists('./' + foName + '/'):
        os.mkdir('./' + foName + '/')
    
    for i in range(0, 10):
        argsDict['cdist'] = [.5 * (10-i)]
        print argsDict['cdist'][0]
        runMultiRun(argsDict, foName + '/' + foName + str(i), foName + str(i), 5)


'''
Main
    -Check if an input file exists
        -if so, use input file to generate the output data
        -if not, use internal method to generate the output data
'''
if __name__ == "__main__":
    
    argsdict = {}
    if len(sys.argv) > 2:
        testType = sys.argv[1]
        print os.getcwd()
        print "Starting Test Generation and Analysis for " + testType
    
        foName = sys.argv[2]
        cRaw = ''
        for i in range(0, len(sys.argv)):
            cRaw += sys.argv[i] + ' '
            
        for farg in sys.argv[3:]:
            (arg,val) = farg.split("=")
        
            argsdict[arg] = [val]
            
        if testType == 'overlap':
            overlapTest(argsdict, foName)
        
    