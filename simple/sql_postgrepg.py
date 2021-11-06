import psycopg
from psycopg.rows import dict_row

# conn = psycopg.connect(conninfo="postgresql://postgres:789456@localhost:5432/test1")
# cur = conn.cursor()

# cur.execute(
#     """INSERT INTO hands (user_name, time_left) VALUES (%(user_name)s, %(time_left)s);""",
#     {"user_name": "len", "time_left": 15},
# )
# conn.commit()

# cur.execute("SELECT * FROM hands")
#
# full_fetch = cur.fetchall()
# for item in full_fetch:
#     print(f"{item=} {type(item)=}")
#
# cur.close()
# conn.close()

# with psycopg.connect(
#     conninfo="postgresql://postgres:789456@localhost:5432/test1"
# ) as conn:
#     with conn.cursor(row_factory=dict_row) as cur:
#
#         cur.execute("SELECT * FROM hands")
#         full_fetch = cur.fetchall()
#         print(full_fetch)

conn = psycopg.connect(conninfo="postgresql://postgres:789456@localhost:5432/test1")
try:
    with conn:
        with conn.cursor(row_factory=dict_row) as cur:

            cur.execute("SELECT * FROM hands WHERE user_name = %s", ("goro",))
            full_fetch = cur.fetchall()
            print(full_fetch)

            cur.execute("SELECT * FROM hands WHERE user_name = %s", ("goro1",))
            full_fetch = cur.fetchall()
            print(full_fetch)

finally:
    print("finally")
    conn.close()

# with conn:
#     with conn.cursor(row_factory=dict_row) as cur:
#         cur.execute("SELECT * FROM hands")
#         full_fetch = cur.fetchall()
#         print(full_fetch)

#
# def get_data_hand(user_name: str) -> dict_row:
#     conn = psycopg.connect(conninfo="postgresql://postgres:789456@localhost:5432/test1")
#
#     try:
#         with conn:
#             with conn.cursor(row_factory=dict_row) as cur:
#                 cur.execute("SELECT * FROM hands WHERE user_name = %s;", (user_name,))
#                 data_sql = cur.fetchall()
#     finally:
#         conn.close()
#     return data_sql
#
#
# def save_db(hand: Hand):
#     conn = psycopg.connect(conninfo="postgresql://postgres:789456@localhost:5432/test1")
#
#     try:
#         with conn:
#             with conn.cursor(row_factory=dict_row) as cur:
#                 cur.execute(
#                     """INSERT INTO hands VALUES (%(user_name)s,
#                                                     %(opened_cards)s,
#                                                     %(available_cards)s,
#                                                     %(time_left)s,
#                                                     %(police)s,
#                                                     %(police_cards)s,
#                                                     %(last_card)s,
#                                                     %(jail)s,
#                                                     %(rate)s);""",
#                     {
#                         "user_name": hand.user_name,
#                         "opened_cards": json.dumps(list(hand.opened_cards)),
#                         "available_cards": json.dumps(list(hand.available_cards)),
#                         "time_left": hand.time_left,
#                         "police": hand.police,
#                         "police_cards": json.dumps(list(hand.police_cards)),
#                         "last_card": hand.last_card,
#                         "jail": hand.jail,
#                         "rate": hand.rate,
#                     },
#                 )
#                 conn.commit()
#     finally:
#         conn.close()
#
#
# def update_db(hand: Hand):
#     conn = psycopg.connect(conninfo="postgresql://postgres:789456@localhost:5432/test1")
#
#     try:
#         with conn:
#             with conn.cursor(row_factory=dict_row) as cur:
#                 cur.execute(
#                     """UPDATE hands SET user_name = %(user_name)s,
#                                 opened_cards = %(opened_cards)s,
#                                 available_cards = %(available_cards)s,
#                                 time_left = %(time_left)s,
#                                 police = %(police)s,
#                                 police_cards = %(police_cards)s,
#                                 last_card = %(last_card)s,
#                                 jail = %(jail)s,
#                                 rate = %(rate)s
#                             WHERE user_name = %(user_name)s;""",
#                     {
#                         "user_name": hand.user_name,
#                         "opened_cards": json.dumps(list(hand.opened_cards)),
#                         "available_cards": json.dumps(list(hand.available_cards)),
#                         "time_left": hand.time_left,
#                         "police": hand.police,
#                         "police_cards": json.dumps(list(hand.police_cards)),
#                         "last_card": hand.last_card,
#                         "jail": hand.jail,
#                         "rate": hand.rate,
#                     },
#                 )
#                 conn.commit()
#     finally:
#         conn.close()
#
#
