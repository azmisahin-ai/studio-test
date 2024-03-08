from src.package import Tracking


def main():
    tracker = Tracking()

    # Example usage
    tracker.trace("This is a trace message.")
    tracker.debug("This is a debug message.")
    tracker.info("This is an info message.")
    tracker.warn("This is a warning message.")
    tracker.error("This is an error message.")


if __name__ == "__main__":
    main()
