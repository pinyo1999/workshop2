pub_ao_udom_set = {"อ่าวอุดมสโมสร", "สิบสามห้าง", "20flow", "SevenDays"}

# 1.จงเขียนคำสั่งเพื่อแสดงค่าของใน pub_ao_udom_set ทั้งหมด
for pub in pub_ao_udom_set:
    print(pub)
# 2.จงเขียนคำสั่งเพื่อเพิ่มค่าใน pub_ao_udom_set โดยเพิ่ม "Oldise" ลงไป
pub_ao_udom_set.add("Dldise")
# 3.จงเขียนคำสั่งเพื่ออัพเดตค่าใน pub_ao_udom_set โดยให้อัพเดต set ของ {"ผิงไฟ", "ตั้งหลัก"} ในตัวแปร pub_ao_udom_set
pub_ao_udom_set.update({"ผิงไฟ", "ตั้งหลัก"})
for pub in pub_ao_udom_set:
    print(pub)
# 4.จงเขียนคำสั่งเพื่อลบค่า "SevenDays" ออกจากตัวแปร  pub_ao_udom_set
pub_ao_udom_set.remove("SevenDays")
# 5.จงเขียนคำสั่งเพื่อสุ่มลบหนึ่งค่าในตัวแปร pub_ao_udom_set
pub_ao_udom_set.pop()
# 6.จงเขียนคำสั่งเพื่อเคลียค่าของ pub_ao_udom_set ทั้งหมด
pub_ao_udom_set.clear()