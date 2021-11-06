import threading
import time


def background_func(count):
    for _ in range(1000):
        print(f"i'm working {count=}")


if __name__ == "__main__":
    t1 = threading.Thread(target=background_func, args=(10,), daemon=True)
    t1.start()

    time.sleep(3)
    print("****")
    t1.join()  # mainthread не завершиться пока t1 backthread не закончит
