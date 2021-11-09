"""
Слово «двуликий» состоит из 8 букв. Байт в двоичном формате имеет 8 бит. Байт может представлять символ.
Мы можем использовать слово «двуликий» для выражения слов в двоичном формате,
если используем заглавные буквы как единицы, а строчные — как нули.
Создайте функцию, которая будет переводить слово в виде обычного текста в «двуликий код».

Примечание: переводите слова, написанные латиницей, и цифры. За перевод кириллицы - дополнительный балл.
"""


def translator(text: str) -> str:
    twoface = "двуликий"
    len_bin = len(twoface)
    word_in_twoface = list()
    for letter in text:
        # translation taking into account Cyrillic [-len_bin::]
        letter_in_bin = bin(ord(letter))[2::].zfill(len_bin)[-len_bin::]
        letter_in_twoface = "".join(
            [
                twoface[i].upper() if letter_in_bin[i] == "1" else twoface[i]
                for i in range(len_bin)
            ]
        )
        word_in_twoface.append(letter_in_twoface)
    return " ".join(word_in_twoface)


assert translator("Hi") == "дВулИкий дВУлИкиЙ"
assert translator("123") == "двУЛикиЙ двУЛикИй двУЛикИЙ"
assert translator("Привет") == "двуЛИКИЙ дВуликий двУЛИкий двУЛикИй двУЛиКиЙ дВуликИй"

# print(translator("Hi"))
# print(translator("123"))
# print(translator("Привет"))
