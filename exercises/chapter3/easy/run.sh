set -Ee

# Create posterior samples:
DIR_UNIFORM=uniform
python ../globe_tossing_posterior.py \
    -n 9 \
    -k 6 \
    --prior uniform \
    --output-dir $DIR_UNIFORM

DIR_STEP=step
python ../globe_tossing_posterior.py \
    -n 9 \
    -k 6 \
    --prior step \
    --output-dir $DIR_STEP

# Analyze samples:
for DIR in $DIR_UNIFORM $DIR_STEP
do
    echo "Using $DIR prior:"
    python ../defined_boundaries.py --lower 0 --upper 0.2 -i $DIR/samples.npy
    python ../defined_boundaries.py --lower 0.8 --upper 1  -i $DIR/samples.npy
    python ../defined_boundaries.py --lower 0.2 --upper 0.8  -i $DIR/samples.npy

    python ../defined_mass.py --mass 0.2 --below  -i $DIR/samples.npy
    python ../defined_mass.py --mass 0.2 --above  -i $DIR/samples.npy

    python ../highest_density_interval.py --mass 0.66  -i $DIR/samples.npy

    python ../defined_mass.py --mass 0.66 --central  -i $DIR/samples.npy
done
