#!/bin/bash

#$ -N bigass_svs_conversion
#$ -t 1-5:1
#$ -M aaji
#$ -m ae
#$ -r y


SEEDFILE=/home/aaji/temp/filelist.txt
SEED=$(awk "NR==$SGE_TASK_ID" $SEEDFILE)

# ~/programs/simulation -s $SEED -o ~/results/output.$SGE_TASK_ID
cat $SEED > /home/aaji/temp/output.$SGE_TASK_ID
# cat input_${SGE_TASK_ID}
