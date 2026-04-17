hunger = 50

def feed_pet():
    global hunger
    hunger = max(0, hunger - 20)
    print(f"Питомец покормлен! Голод: {hunger}")

def main():
    print("MyPett - Кормление")
    feed_pet()

if __name__ == "__main__":
    main()
