# Create posterior samples:
python ../globe_tossing_posterior.py -n 15 -k 8

# Analyze samples:
python ../highest_density_interval.py --mass 0.9
python posterior_predictive_check.py -n 15 -k 8
python posterior_predictive_check.py -n 9 -k 6

