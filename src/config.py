import argparse
import configparser


def load_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config


def parse_args(config):
    parser = argparse.ArgumentParser(description="Solve a maze.")
    parser.add_argument(
        "--rows",
        type=int,
        default=config.getint("maze", "num_rows"),
        help="Number of rows in the maze (default: %(default)s)",
    )
    parser.add_argument(
        "--cols",
        type=int,
        default=config.getint("maze", "num_cols"),
        help="Number of columns in the maze (default: %(default)s)",
    )
    parser.add_argument(
        "--margin",
        type=int,
        default=config.getint("maze", "margin"),
        help="Margin size around the maze (default: %(default)s)",
    )
    parser.add_argument(
        "--screen_x",
        type=int,
        default=config.getint("maze", "screen_x"),
        help="Width of the maze screen (default: %(default)s)",
    )
    parser.add_argument(
        "--screen_y",
        type=int,
        default=config.getint("maze", "screen_y"),
        help="Height of the maze screen (default: %(default)s)",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=config.getint("maze", "seed"),
        help="Random seed used to generate the maze (default: %(default)s)",
    )
    return parser.parse_args()


def update_config(args):
    config = configparser.ConfigParser()
    config.read("config.ini")
    config["maze"]["num_rows"] = str(args.rows)
    config["maze"]["num_cols"] = str(args.cols)
    config["maze"]["margin"] = str(args.margin)
    config["maze"]["screen_x"] = str(args.screen_x)
    config["maze"]["screen_y"] = str(args.screen_y)
    config["maze"]["seed"] = str(args.seed)
    with open("config.ini", "w") as configfile:
        config.write(configfile)
