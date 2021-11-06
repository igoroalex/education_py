import json

temp_json = """
{
	"rules":[
		{
			"name": "i1",
			"dauthers":["i1r"]
		}, 
		{
			"name": "i1r",
			"dauthers":["i2"]
		}, 
		{
			"name": "i2",
			"dauthers":["i2r"]
		}, 
		{
			"name": "i2r",
			"dauthers":["i3"]
		}, 
		{
			"name": "i3",
			"dauthers":["m1", "s1"]
		}
	] 
}"""

# data_cards = json.loads(temp_json)  # загружает из строки
# print(data_cards)
with open("pock-dect1.json", "r") as file:
    data = json.load(file)

print(data)
# new_json = json.dumps(data_cards, indent=2)
# new_json = json.dumps(data_cards)
# print(new_json)

# with open("pock-dect1.json", "w") as file:
#     json.dump(data_cards, file, indent=2)
