cleanliness = 50

def clean_pet():
    global cleanliness
    cleanliness = min(100, cleanliness + 25)
    print(f"Питомец чист! Чистота: {cleanliness}")

def main():
    print("MyPett - Уход")
    clean_pet()

if __name__ == "__main__":
    main()
