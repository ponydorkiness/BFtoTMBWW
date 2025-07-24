del input.txt
del orginal.txt
del output.txt
python 1_bf_tm.py
python 2_strip.py output.txt input.txt
python removeallblanks.py output.txt
ren "output.txt" "orginal.txt"
python 3_label.py input.txt output.txt
copy output.txt input.txt
python3 4_fuse.py input.txt output.txt
python3 5_orginal.py orginal.txt output.txt input.txt
python3 fixloops.py input.txt output.txt
echo nya
python 2_strip.py output.txt input.txt
python removeallblanks.py input.txt
del orginal.txt
del output.txt
python fixstart.py input.txt
python fixalllabels.py input.txt output.txt
copy output.txt program.txt
del input.txt
del output.txt