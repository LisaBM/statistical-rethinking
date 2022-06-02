for n_k in "3 3" "4 3" "7 5"; do
    set -- $n_k
    n=$1 && k=$2
    python 2M1_globe_tossing_grid_approximate.py -n $n -k $k
done
