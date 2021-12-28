import json

persons = {
    "Ars Kalinichenko": {
        "age": 18,
        "gender": True,
        "height": 180
    },
    "Elon Mask": {
        "age": 50,
        "gender": 100,
        "height": 250
    },
    "Oleg Olegha": {
        "age": 7777748,
        "gender": -1000,
        "height": None
    }
}

with open("test.txt", "w") as file:
    x = json.dumps(persons)
    file.write(x)


def read_from_json(path: str) -> dict:
    with open(path, "r") as test_file_for_you_egor:
        text = test_file_for_you_egor.read()
        return json.loads(text)


p = read_from_json("test1.txt")
print("From read_from_json function: ", p)
print("Type: ", type(p))
