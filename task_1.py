import time
import random
from queue import Queue

# створюємо чергу
request_queue = Queue()
request_id = 1  # лічильник заявок


def generate_request():
    """Генерує нову заявку та додає її до черги"""
    global request_id
    request = f"Заявка №{request_id}"
    request_queue.put(request)
    print(f"🆕 Створено {request}")
    request_id += 1


def process_request():
    """Обробляє заявку з черги"""
    if not request_queue.empty():
        current_request = request_queue.get()
        print(f"✅ Оброблено {current_request}")
    else:
        print("⚠️ Черга пуста, нових заявок немає.")


def main():
    print("Система обробки заявок запущена. Натисніть Ctrl+C для завершення.\n")
    try:
        while True:
            generate_request()
            process_request()
            time.sleep(random.uniform(0.5, 1.5))  # пауза для наочності
    except KeyboardInterrupt:
        print("\nПрограму завершено користувачем.")


if __name__ == "__main__":
    main()
