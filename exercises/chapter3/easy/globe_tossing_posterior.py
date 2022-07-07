import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import binom

N = 1000
SEED = 0


def run() -> None:
    np.random.seed(SEED)
    p_grid = np.linspace(start=0, stop=1, num=N)
    prior = np.ones(N)
    likelihood = binom.pmf(k=6, n=9, p=p_grid)
    posterior = likelihood * prior
    posterior /= sum(posterior)
    samples = np.random.choice(p_grid, size=10000, replace=True, p=posterior)
    np.save("samples", samples)
    plt.hist(samples, bins=100)
    plt.savefig("postrior")


if __name__ == "__main__":
    run()
