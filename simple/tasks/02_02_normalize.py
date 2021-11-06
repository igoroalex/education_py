import datetime


def normalize(sentence: str) -> str:
    """get string in capitalize and add ! if all letters is upper and not 22 oct, 22oct - caps day"""
    today = datetime.date.today()
    if today.month == 9 and today.day == 22:  # its caps day
        return sentence.upper()

    return f"{sentence.capitalize()}!" if sentence.upper() == sentence else sentence


# assert normalize("CAPS LOCK DAY IS OVER") == "Caps lock day is over!"
# assert normalize("Today is not caps lock day.") == "Today is not caps lock day."
# assert (
#         normalize("Let us stay calm, no need to panic.")
#         == "Let us stay calm, no need to panic."
# )
