import json

data = {
    "name": "John",
    "age": 25,
    "hobbies": ["reading", "coding", "gaming"]
}

# Writing to JSON
with open("data.json", "w") as file:
    json.dump(data, file, indent=4)

# Reading from JSON
with open("data.json", "r") as file:
    loaded_data = json.load(file)

print(loaded_data)
