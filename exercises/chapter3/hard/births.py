import logging

import matplotlib.pyplot as plt
import numpy as np
import pymc3
from scipy.stats import binom


class PlotContext:

    def __init__(self, fig_name: str) -> None:
        self._fig_name = fig_name

    def __enter__(self) -> None:
        pass

    def __exit__(self, type, value, traceback) -> None:
        plt.savefig(self._fig_name)
        plt.clf()


def generate_data():
    return {
        "first_birth":
            np.array([
                1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1,
                0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1,
                1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0,
                0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0,
                0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1
            ]),
        "second_birth":
            np.array([
                0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 0,
                0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 0,
                0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0,
                0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0
            ])
    }


def run() -> None:
    data = generate_data()
    grid = np.linspace(0, 1, 1000)
    prior = np.ones_like(grid)
    n_births = len(data["first_birth"]) + len(data["second_birth"])
    n_boys = np.sum(data["first_birth"] + data["second_birth"])
    likelihood = binom.pmf(k=n_boys, n=n_births, p=grid)
    posterior = prior * likelihood
    posterior /= np.sum(posterior)
    samples = np.random.choice(grid, size=10000, replace=True, p=posterior)
    logging.info(f"p = {grid[np.argmax(posterior)]} maximizes the posterior "
                 "probability.")

    with PlotContext("postrior") as _:
        plt.hist(samples, bins=100)

    # 3H2
    for p in [.5, .89, .97]:
        hdi = pymc3.stats.hdi(samples, hdi_prob=p)
        logging.info(f"The highest density interval containing {p * 100}% of "
                     f"the posterior probability is {hdi}.")

    # 3H3
    n_boys_samples = [binom.rvs(n=200, p=p) for p in samples]
    with PlotContext("predictive_distribution_all_births") as _:
        plt.hist(n_boys_samples, bins=100)
        plt.axvline(n_boys, c="red")
        plt.xlabel("n_boys")

    # 3H4
    n_boys_samples = [binom.rvs(n=100, p=p) for p in samples]
    with PlotContext("predictive_distribution_first_birth") as _:
        plt.hist(n_boys_samples, bins=100)
        plt.axvline(np.sum(data["first_birth"]), c="red")
        plt.xlabel("n_boys")

    # 3H5
    n_first_girl = sum(data["first_birth"] == 0)
    n_boy_after_girl = sum(data["second_birth"][data["first_birth"] == 0])
    n_boys_after_girl_samples = [
        binom.rvs(n=n_first_girl, p=p) for p in samples
    ]
    with PlotContext("predictive_distribution_boy_after_girl") as _:
        plt.hist(n_boys_after_girl_samples, bins=100)
        plt.axvline(n_boy_after_girl, c="red")
        plt.xlabel("n_boys")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
