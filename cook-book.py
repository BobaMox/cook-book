from pprint import pprint


def reading_recipes() -> dict:
    """
    Считывает рецепты из файла и добавляет в словарь
    """
    cook_book = {}

    try:
        with open('recipes.txt', encoding='UTF-8') as file:
            for line in file:
                line = line.strip()
                if line and not line.isdigit() and '|' not in line:
                    dish_name = line
                    cook_book[dish_name] = []
                elif '|' in line:
                    ingredient, quantity, measure = line.split('|')
                    cook_book[dish_name].append({
                        'ingredient_name': ingredient.strip(),
                        'quantity': int(quantity.strip()),
                        'measure': measure.strip()
                    })
    except FileNotFoundError:
        print("Файл рецептов не найден.")
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")

    return cook_book


def get_shop_list_by_dishes(dishes: list, person_count: int):
    """
    Подготавливает количество ингредиентов для приготовления заказа
    :param dishes:
    :param person_count:
    """
    cook_book = reading_recipes()
    order = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count
                if ingredient_name in order:
                    order[ingredient_name]['quantity'] += quantity
                else:
                    order[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f"Рецепт для блюда {dish} не найден.")

    pprint(order)


if __name__ == '__main__':
    get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3)
