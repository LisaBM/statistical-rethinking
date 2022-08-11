set -Ee

# Create posterior samples:
DIR_UNIFORM=uniform
python ../globe_tossing_posterior.py \
    -n 15 \
    -k 8 \
    --prior uniform \
    --output-dir $DIR_UNIFORM

DIR_STEP=step
python ../globe_tossing_posterior.py \
    -n 15 \
    -k 8 \
    --prior step \
    --output-dir $DIR_STEP

# Analyze samples:
for DIR in $DIR_UNIFORM $DIR_STEP
do
    echo "Using $DIR prior:"
    python ../highest_density_interval.py --mass 0.9 -i $DIR/samples.npy
    python posterior_predictive_check.py -n 15 -k 8 -i $DIR/samples.npy
    python posterior_predictive_check.py -n 9 -k 6 -i $DIR/samples.npy
done
