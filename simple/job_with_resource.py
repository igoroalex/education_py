# авто закрытие, для быстрого и простого способа
with open("example.txt", "w") as f:
    f.write("hello")

with open("example.txt", "r") as f:
    for i in f:
        # print(i)
        pass

f = open("example.txt", "w")
f.write("hello")
f.close()

# f.seek(20) позиционирование на 20 символе
# f.read(5) считывает след 5 символов с текущей позиции
# f.readline()  # считывает строку
# f.readlines() считывает все строки в list

# работа с какаим-то ресурсом: файл, обращение к абзе данных...
from contextlib import contextmanager


class Resource:
    def __init__(self):
        self.opened = False

    def open(self, *args):
        print(f"Resource opened with {args}")
        self.opened = True

    def close(self):
        print("Resource closed")
        self.opened = False

    def __del__(self):
        if self.opened:
            print("Memory leak detected")

    def action(self):
        print("Do everything")


# №1 через контекст менеджер
@contextmanager
def open_resource(*args):
    resource = None
    try:
        resource = Resource()
        resource.open(1, 2, 3)
        yield resource
    except Exception:
        raise
    finally:
        if resource:
            resource.close()


# №2 через класс лучше
class ResourceWorker:
    def __init__(self, *args):
        self.resource = None
        self.args = args

    def __enter__(self):
        self.resource = Resource()
        self.resource.open(1, 2, 3)
        return self.resource

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.resource:
            self.resource.close()


if __name__ == "__main__":
    # 1
    # with open_resource(1, 2, 3) as res:
    #     res.action()
    # 2
    with ResourceWorker(1, 2, 3) as res:
        res.action()
