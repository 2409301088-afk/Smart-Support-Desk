def notify(*channels, **details):

    print("\n===== Notification =====")

    print("Channels:")
    for channel in channels:
        print("-", channel)

    print("\nDetails:")
    for key, value in details.items():
        print(f"{key}: {value}")