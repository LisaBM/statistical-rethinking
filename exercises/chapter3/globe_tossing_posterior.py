import argparse

import matplotlib.pyplot as plt
from soupsieve import match
import numpy as np
from scipy.stats import binom

N = 1000
SEED = 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-tosses",
                        "-n",
                        dest="n_tosses",
                        type=int,
                        required=True)
    parser.add_argument("--n-water",
                        "-k",
                        dest="n_water",
                        type=int,
                        required=True)
    parser.add_argument("--prior", default="uniform", required=False)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    np.random.seed(SEED)
    p_grid = np.linspace(start=0, stop=1, num=N)
    match args.prior:
        case "uniform":
            prior = np.ones(N)
        case "step":
            prior = np.where(p_grid < 0.5, 0, 1)
        case _:
            raise RuntimeError(
                "Invalid prior. Valid values are 'uniform' and 'step'.")
    likelihood = binom.pmf(k=args.n_water, n=args.n_tosses, p=p_grid)
    posterior = likelihood * prior
    posterior /= sum(posterior)
    samples = np.random.choice(p_grid, size=10000, replace=True, p=posterior)
    np.save("samples", samples)
    plt.hist(samples, bins=100)
    plt.savefig("postrior")


if __name__ == "__main__":
    run()
