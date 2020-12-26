#!/bin/bash

cat $1 |
    sed '1d' |
    awk -F, '{print "N0"$1,"G0"$2,"X"$3".","Z"$4".", "R"$5".","F"$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17,$18,$19,$20,$21,$22,$23}' |
    sed -e 's/N0 //g' |
    sed -e 's/G0 //g' |
    sed -e 's/X. //g' |
    sed -e 's/Z. //g' |
    sed -e 's/R. //g'  |
    sed -e 's/F //g'  |
    sed -e 's/M /M/g' |
    sed -e 's/U 0/U0./g'  |
    sed -e 's/W 0/W0./g' |
    sed -e 's/ \+/ /g' > N$(basename $1 .csv).txt
