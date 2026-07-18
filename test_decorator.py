from utils.decorators import retry

count = 0

@retry(max_attempts=3)
def test():

    global count

    count += 1

    print("Trying...")

    if count < 3:
        raise Exception("Error")

    print("Success!")

test()