hunger = 50
happiness = 50
cleanliness = 50

def show_status():
    print(f"Статус питомца:")
    print(f"Голод: {hunger}")
    print(f"Счастье: {happiness}")
    print(f"Чистота: {cleanliness}")

def main():
    print("MyPett - Статус")
    show_status()

if __name__ == "__main__":
    main()
