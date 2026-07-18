import time

class Timer:

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Execution Time: {end - self.start:.4f} seconds")