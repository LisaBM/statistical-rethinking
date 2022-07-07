# Create posterior samples:
python globe_tossing_posterior.py

# Analyze samples:
python defined_boundaries.py --lower 0 --upper 0.2
python defined_boundaries.py --lower 0.8 --upper 1
python defined_boundaries.py --lower 0.2 --upper 0.8

python defined_mass.py --mass 0.2 --below
python defined_mass.py --mass 0.2 --above

python highest_density_interval.py --mass 0.66

python defined_mass.py --mass 0.66 --central