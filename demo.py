import toml


with open("algo.toml", "r") as f:
    data = toml.load(f)
    print(data)

with open("algo.toml", "w") as f:
    data["collections"] = ["a", "b", "c"]
    toml.dump(data, f)
