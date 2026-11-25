import os

TEXT = "Sorry, I auto-scaled my mistake: one bad config, faithfully replicated to 14 regions in 9 seconds — replication is flawless, judgment is still in beta."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
