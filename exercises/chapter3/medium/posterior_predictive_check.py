# sample p from posterior
# use binomial distribution with sampled p to compute prob of k

import argparse
import logging

import numpy as np
from scipy.stats import binom


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-tosses", "-n", dest="n_tosses", type=int, required=True)
    parser.add_argument("--n-water", "-k", dest="n_water", type=int, required=True)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    samples = np.load("samples.npy")

    prob = 0
    for p in samples:
        prob += binom.pmf(args.n_water, args.n_tosses, p)
    prob /= len(samples) 


    logging.info(
        f"The posterior predictive probability of observing {args.n_water} "
        f"water in {args.n_tosses} tosses is {prob:.2f}.")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
