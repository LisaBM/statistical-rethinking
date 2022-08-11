import argparse
import logging

import numpy as np
import pymc3


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mass", dest="mass", type=float, required=True)
    parser.add_argument("--input-data", "-i", dest="input_data", required=True)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    samples = np.load(args.input_data)

    hdi = pymc3.stats.hdi(samples, hdi_prob=args.mass)

    logging.info(
        f"The highest density interval containing {args.mass * 100}% of the "
        f"posterior probability is {hdi}.")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    np.set_printoptions(formatter={"float_kind": "{:.2f}".format})
    run()
