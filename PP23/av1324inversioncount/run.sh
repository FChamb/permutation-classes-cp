
mkdir -p params
mkdir -p outputs

# this is made for a large machine!
# 256 cores, 1TB memory

python3 gen_commands_seq.py > commands_seq.txt

parallel --no-notice -j240 \
    --joblog outputs/gnuparallel-joblog-seq.tsv \
    --results outputs/gnuparallel-results-seq \
    --memfree 100G \
    --shuf \
    --eta \
    :::: commands_seq.txt



python3 gen_commands_par.py > commands_par.txt

parallel --no-notice -j4 \
    --joblog outputs/gnuparallel-joblog-par.tsv \
    --results outputs/gnuparallel-results-par \
    --memfree 100G \
    --shuf \
    --eta \
    :::: commands_par.txt

