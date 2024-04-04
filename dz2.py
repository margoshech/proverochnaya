class Toy:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

import random

class ToyLottery:
    def __init__(self):
        self.toys = []

    def add_toy(self, toy):
        self.toys.append(toy)

    def draw_toy(self, weight):
        available_toys = [toy for toy in self.toys if toy.weight >= weight]
        if available_toys:
            chosen_toy = random.choice(available_toys)
            return chosen_toy
        else:
            return None
        
def add_toy_dialog(lottery):
    name = input("Введите имя игрушки: ")
    weight = float(input("Введите вес игрушки: "))
    toy = Toy(name, weight)
    lottery.add_toy(toy)
    print(f"Игрушка '{name}' успешно добавлена в розыгрыш.")

def run_lottery_dialog(lottery):
    weight = float(input("Введите вес, чтобы выиграть игрушку: "))
    chosen_toy = lottery.draw_toy(weight)
    if chosen_toy:
        print(f"Вы выиграли игрушку '{chosen_toy.name}'!")
    else:
        print("К сожалению, нет доступных игрушек для данного веса.")

def main():
    lottery = ToyLottery()

    while True:
        print("\nМеню:")
        print("1. Добавить новую игрушку")
        print("2. Провести розыгрыш")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")

        if choice == "1":
            add_toy_dialog(lottery)
        elif choice == "2":
            run_lottery_dialog(lottery)
        elif choice == "3":
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()