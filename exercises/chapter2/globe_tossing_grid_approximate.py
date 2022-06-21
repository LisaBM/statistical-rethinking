import argparse
import pathlib
from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom


PLOT_DIR=pathlib.Path("plots")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-tosses", "-n", dest="n_tosses", type=int, required=True)
    parser.add_argument("--n-water", "-k", dest="n_water", type=int, required=True)
    parser.add_argument("--prior", dest="prior", type=str, default="uniform")
    return parser.parse_args()


def make_prior(x: np.ndarray, prior_name: str, **kwargs) -> Callable:
    if prior_name == "uniform":
        return np.ones(len(x))
    if prior_name == "greater_0.5":
        return np.where(x < 0.5, 0, 1)


def run() -> None:
    args = parse_args()
    n = 1000
    grid = np.linspace(0, 1, num=n)
    prior = make_prior(grid, args.prior)
    likelihood = np.zeros(n)
    for i, p in enumerate(grid):
        likelihood[i] = binom.pmf(k=args.n_water, n=args.n_tosses, p=p)
    posterior = likelihood * prior
    posterior /= sum(posterior)

    pathlib.Path.mkdir(PLOT_DIR, exist_ok=True, parents=True)
    fig = plt.plot(grid, posterior)
    plt.savefig(PLOT_DIR / f"plot_{args.n_tosses}_{args.n_water}")

if __name__ == "__main__":
    run()