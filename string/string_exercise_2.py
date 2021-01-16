# จงเขียนคำสั่งเพื่อแสดงความยาวของตัวอักษร "I am the best programmer"
print(len("I am the best programmer"))
# จงเขียนคำสั่งเพื่อแสดงอักษรแรกของข้อความ "I am the best programmer"
print(("I am the best programmer"[0]))
# จงเขียนคำสั่งเพื่อแสดง "best" ของข้อความ "I am the best programmer"
print(("I am the best programmer"[9:13]))
print(("I am the best programmer"[-15:-11]))
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ไม่มี space
string = "I am the best programmer"
list = string.split(" ")
print(list[0] + list[1] + list[2] + list[3] + list[4])
string = ""
for loop in list:
    string = string + loop
print(string)
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมใหญ่ทั้งหมด
string = "I am the best programmer"
print(string.upper())
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ให้เป็นตัวพิมเล็กทั้งหมด
print(string.lower())
# จงเขียนคำสั่งเพื่อแสดข้อความ "I am the best programmer" ที่ถูกแทนที่อักษร e ด้วย z ทั้งหมด
print(string.replace("e", "z"))
# จงเติมคำในช่องว่าเพื่อแสดงชื่อ
myname = "I"
txt = "{} is the best programmer"
print(txt.format(myname))