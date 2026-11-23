import time
import sys
from pathlib import Path
from collections import deque

# Project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Make project root available for imports
sys.path.insert(0, str(BASE_DIR))

# Import the correct AI prediction function
from ai.engine import predict_threat

# AMF log file
LOG_FILE = BASE_DIR / "logs" / "amf.log"

# Store timestamps of recent events
request_times = deque()
failure_times = deque()

# Keywords used to identify log events
REGISTRATION_KEYWORDS = (
    "registration request",
    "ue registration",
    "registration for ue",
    "registering ue"
)

AUTH_FAILURE_KEYWORDS = (
    "authentication failed",
    "authentication failure",
    "auth failed",
    "auth_failure"
)


def follow(file):
    """Read new log entries as they are written."""

    # Start monitoring from the end of the file
    file.seek(0, 2)

    while True:
        line = file.readline()

        if not line:
            time.sleep(1)
            continue

        yield line


def remove_old_events(events, current_time):
    """Keep only events from the last 60 seconds."""

    while events and current_time - events[0] > 60:
        events.popleft()


def monitor_logs():

    print("AI LOG MONITOR STARTED...")
    print(f"Monitoring: {LOG_FILE}")

    if not LOG_FILE.exists():
        print("AMF log file not found. Start AMF first.")
        return

    with open(LOG_FILE, "r") as file:

        for line in follow(file):

            current_time = time.time()
            log_text = line.lower()

            # Identify registration requests
            is_registration = any(
                keyword in log_text
                for keyword in REGISTRATION_KEYWORDS
            )

            # Identify failed authentication attempts
            is_auth_failure = any(
                keyword in log_text
                for keyword in AUTH_FAILURE_KEYWORDS
            )

            # Record registration event
            if is_registration:
                request_times.append(current_time)

            # Record failed authentication event
            if is_auth_failure:
                failure_times.append(current_time)

            # Remove events older than 60 seconds
            remove_old_events(request_times, current_time)
            remove_old_events(failure_times, current_time)

            # Analyze only when a relevant event is found
            if is_registration or is_auth_failure:

                rpm = len(request_times)
                failed_auth = len(failure_times)

                result = predict_threat(rpm, failed_auth)

                if result:
                    status = "POTENTIAL THREAT"
                else:
                    status = "NORMAL"

                print(
                    f"{status} | "
                    f"RPM: {rpm} | "
                    f"Failed Auth: {failed_auth} | "
                    f"{line.strip()}"
                )


if __name__ == "__main__":
    monitor_logs()
