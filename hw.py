import heapq

def min_connection_cost(cables):
    # Створюємо мінімальну купу з кабелів
    heapq.heapify(cables)

    total_cost = 0

    # Поки в купі більше одного елемента
    while len(cables) > 1:
        # Витягуємо два найменші елементи
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        # Об'єднуємо їх
        cost = first + second
        total_cost += cost

        # Додаємо новий кабель назад у купу
        heapq.heappush(cables, cost)

    return total_cost

# Приклад використання
cables = [4, 3, 2, 6]
result = min_connection_cost(cables)
print(f"Мінімальна сума витрат 1: {result}")

cables = [1, 2, 3, 4, 5]
result = min_connection_cost(cables)
print(f"Мінімальна сума витрат 2: {result}")

cables = [5, 10, 15]
result = min_connection_cost(cables)
print(f"Мінімальна сума витрат 3: {result}")
