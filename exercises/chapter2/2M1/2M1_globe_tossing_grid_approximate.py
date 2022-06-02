import argparse

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-tosses", "-n", dest="n_tosses", type=int, required=True)
    parser.add_argument("--n-water", "-k", dest="n_water", type=int, required=True)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    n = 1000
    grid = np.linspace(0, 1, num=n)
    prior = np.ones(n)
    likelihood = np.zeros(n)
    for i, p in enumerate(grid):
        likelihood[i] = binom.pmf(k=args.n_water, n=args.n_tosses, p=p)
    posterior = likelihood * prior
    posterior /= sum(posterior)
    fig = plt.plot(grid, posterior)
    plt.savefig(f"plots/plot_{args.n_tosses}_{args.n_water}")

if __name__ == "__main__":
    run()