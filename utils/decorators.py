import time
from functools import wraps

def retry(max_attempts=3):

    def decorator(func):

        @wraps(func)
        def wrapper(*args, **kwargs):

            attempts = 0

            while attempts < max_attempts:

                try:
                    return func(*args, **kwargs)

                except Exception as e:

                    attempts += 1

                    print(f"Attempt {attempts} failed: {e}")

                    if attempts == max_attempts:
                        print("Maximum retry attempts reached.")
                        raise

                    time.sleep(1)

        return wrapper

    return decorator