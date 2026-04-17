hunger = 50
happiness = 50
cleanliness = 50

def feed_pet():
    global hunger
    hunger = max(0, hunger - 20)
    print(f"Питомец покормлен! Голод: {hunger}")

def play_with_pet():
    global happiness
    happiness = min(100, happiness + 15)
    print(f"Поиграли! Счастье: {happiness}")

def clean_pet():
    global cleanliness
    cleanliness = min(100, cleanliness + 25)
    print(f"Питомец чист! Чистота: {cleanliness}")

def show_status():
    print(f"Статус питомца:")
    print(f"Голод: {hunger}")
    print(f"Счастье: {happiness}")
    print(f"Чистота: {cleanliness}")

def main():
    print("=== MY PETT GAME ===")
    print("1 - Покормить")
    print("2 - Поиграть")
    print("3 - Почистить")
    print("4 - Статус")
    
    choice = input("Выберите действие: ")
    if choice == "1":
        feed_pet()
    elif choice == "2":
        play_with_pet()
    elif choice == "3":
        clean_pet()
    elif choice == "4":
        show_status()
    else:
        print("Неверный выбор")

if __name__ == "__main__":
    main()
