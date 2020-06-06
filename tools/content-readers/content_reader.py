import os
import time

from reddit_rss.feed_reader import run_reddit_rss_feed


if __name__ == "__main__":
    READER_MODE = os.getenv("READER_MODE")
    if not READER_MODE:
        raise ValueError(f"READER_MODE not set.")

    JOB_SLEEP_TIME_SECONDS = int(os.getenv("JOB_SLEEP_TIME_SECONDS"))
    if not JOB_SLEEP_TIME_SECONDS:
        JOB_SLEEP_TIME_SECONDS = 30

    try:
        while True:
            if READER_MODE == "reddit":
                run_reddit_rss_feed()
            else:
                raise ValueError(f"READER_MODE {READER_MODE} not supperted")
            time.sleep(JOB_SLEEP_TIME_SECONDS)
    except KeyboardInterrupt:
        print("KeyboardInterrupt called. Exiting.")
