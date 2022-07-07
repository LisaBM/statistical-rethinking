import argparse
import logging

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mass", dest="mass", type=float, required=True)
    parser.add_argument("--below", dest="below", action="store_true")
    parser.add_argument("--above", dest="above", action="store_true")
    parser.add_argument("--central", dest="central", action="store_true")
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    samples = np.load("samples.npy")

    if args.below:
        percentile = np.percentile(samples, args.mass * 100)
        logging.info(
            f"{args.mass * 100}% of the posterior probability lies below "
            f"p = {percentile:.2f}.")
    elif args.above:
        percentile = -np.percentile(-samples, args.mass * 100)
        logging.info(
            f"{args.mass * 100}% of the posterior probability lies above "
            f"p = {percentile:.2f}.")
    elif args.central:
        q = args.mass + (1 - args.mass) / 2
        lower_bound = -np.percentile(-samples, q * 100)
        upper_bound = np.percentile(samples, q * 100)
        logging.info(
            f"The central credible interval containing {args.mass * 100}% of "
            f"the posterior probability is "
            f"[{lower_bound:.2f}, {upper_bound:.2f}].")

    else:
        raise RuntimeError("One of --above or --below needs to be provided.")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
