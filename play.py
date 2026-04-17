happiness = 50

def play_with_pet():
    global happiness
    happiness = min(100, happiness + 15)
    print(f"Поиграли! Счастье: {happiness}")

def main():
    print("MyPett - Игра")
    play_with_pet()

if __name__ == "__main__":
    main()
