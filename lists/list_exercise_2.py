# จงแสดง "rat"
animal = ["cat", "bat", "rat", "dog"]
print(animal[2])
for value in animal:
    if value == "rat":
        print(value)
# จงแก้ไขข้อมูลจาก "cat" เป็น "hen"
animal = ["cat", "bat", "rat", "dog"]
animal[0] = "hen"

animal = ["cat", "bat", "rat", "dog"]
i = 0
for value in animal:
    if value == "bat":
        animal[i] = "hen"
    i = i + 1
print(animal)
# จงเพิ่ม "hen" ไปยัง animal list
animal = ["cat", "bat", "rat", "dog"]
animal.append("hen")
animal.pop()
animal.insert(0, "hen")

# จงเพิ่ม "hen" ไประหว่าง "rat" กับ "ิิdog"
animal = ["cat", "bat", "rat", "dog"]
animal.insert(3, "hen")


# จงลบ "rat" จาก list
animal = ["cat", "bat", "rat", "dog"]
animal.remove("rat")

# จงแสดงตัวสุดท้ายของ animal
animal = ["cat", "bat", "rat", "dog"]
print(animal[len(animal) - 1])

# จงแสดงจำนวนของ animal
animal = ["cat", "bat", "rat", "dog"]
print(len(animal))