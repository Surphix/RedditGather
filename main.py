import os, argparse
from reddit.gather import gather
import time



if __name__ == "__main__":
    start = time.time()
    parser = argparse.ArgumentParser(description="Scrape reddit post data")
    parser.add_argument('-k', type=str, help="Keyword used to search", required=True)
    parser.add_argument('-l', type=int, help="Limit of submissions to search", required=True)
    gather(parser.parse_args()).launch()
    end = time.time()
    print(end - start)