import argparse
import logging

import numpy as np


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--lower", dest="lower", type=float, required=True)
    parser.add_argument("--upper", dest="upper", type=float, required=True)
    parser.add_argument("--input-data", "-i", dest="input_data", required=True)
    return parser.parse_args()


def run() -> None:
    args = parse_args()
    samples = np.load(args.input_data)
    in_interval = np.where((args.lower <= samples) & (samples <= args.upper), 1,
                           0)
    prob = np.sum(in_interval) / len(samples)
    logging.info(f"{prob * 100:.2f}% of the posterior probability lies in "
                 f"[{args.lower}, {args.upper}].")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run()
