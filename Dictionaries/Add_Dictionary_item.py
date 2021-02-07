thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
model = thisdict["color"] = "red"
print(thisdict)

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
model = thisdict.update({"color": "red"})
print("model:", model)
