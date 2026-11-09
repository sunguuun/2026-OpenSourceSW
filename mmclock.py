"""Display the current system time with millisecond precision."""

from datetime import datetime
import time


def main() -> None:
    try:
        while True:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
            print(f"\r{timestamp}.{now.microsecond // 1000:03d}", end="", flush=True)
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()
