import os

from reddit_rss.feed_reader import run_reddit_rss_feed


if __name__ == "__main__":
    READER_MODE = os.getenv("READER_MODE")
    if not READER_MODE:
        raise ValueError(f"READER_MODE not set.")

    if READER_MODE == "reddit":
        run_reddit_rss_feed()
