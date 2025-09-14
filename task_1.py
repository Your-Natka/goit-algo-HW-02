import time
import random
from queue import Queue

class RequestProcessor:
    def __init__(self):
        self.queue = Queue()
        self.request_id = 1

    def generate_request(self):
        request = f"Заявка №{self.request_id}"
        self.queue.put(request)
        print(f"🆕 Створено {request}")
        self.request_id += 1

    def process_request(self):
        if not self.queue.empty():
            current_request = self.queue.get()
            print(f"✅ Оброблено {current_request}")
        else:
            print("⚠️ Черга пуста, нових заявок немає.")


def main():
    processor = RequestProcessor()
    try:
        while True:
            processor.generate_request()
            processor.process_request()
            time.sleep(random.uniform(0.5, 1.5))
    except KeyboardInterrupt:
        print("\nПрограму завершено користувачем.")


if __name__ == "__main__":
    main()

