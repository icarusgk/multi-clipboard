import sys
import clipboard
import json

FILENAME = "clipboard.json"

def save_data(filepath, data):
	with open(filepath, "w") as f:
		json.dump(data, f)

def load_data(filepath):
	try:
		with open(filepath, "r") as f:
			data = json.load(f)
			return data
	except:
		return {}


# Verify commands given
if len(sys.argv) == 2:
	command = sys.argv[1]

	data = load_data(FILENAME)

	if command == "save":
		key = input("Enter a key: ")
		data[key] = clipboard.paste()

		save_data(FILENAME, data)
		
		print("The data has been succesfully saved!")
	elif command == "load":
		key = input("Enter a key: ")

		if key in data:
			clipboard.copy(data[key])

			print("Data copied.")
		else:
			print("Print does not exists.")

	elif command == "list":
		print(data)
	else:
		print("Unknown command")
else:
	print("Please pass exactly one command.")
