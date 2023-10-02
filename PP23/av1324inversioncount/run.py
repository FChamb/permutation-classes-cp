
# create the param file

import sys, os

solver = sys.argv[1]
length = sys.argv[2]
nbInv = sys.argv[3]

paramfile = f'params/{solver}-{length}-{nbInv}.param'

with open(paramfile, "w") as out:
    print('letting turnedOn be true', file=out)
    print('letting classic_avoidance be {sequence(1,3,2,4)}', file=out)
    print(f'letting length be {length}', file=out)
    print(f'letting nInversions be {nbInv}', file=out)

# run conjure

if solver == "minionseq":
    solvername = "minion"
    opts = ""
elif solver == "minionpar":
    solvername = "minion"
    opts = '--savilerow-options "-preprocess SSACBounds" --solver-options "-parallel -cores 32"'
elif solver == "nbcsat":
    solvername = "nbc_minisat_all"
    opts = ""

os.system(f'conjure solve av1324invcount.essence {paramfile} --number-of-solutions=all --solutions-in-one-file --output-format=json --solver={solvername} {opts}')

# cleanup