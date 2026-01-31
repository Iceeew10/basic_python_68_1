# Function

def my_fullname(firstname="ICE", lastname="WANSU"):  # def คือการสร้างฟังก์ชัน
    return firstname + " " + lastname  # return คือการส่งค่ากลับ


print(my_fullname())  # ICE WANSU
print(my_fullname(firstname="ICE"))  # ICE WANSU
print(my_fullname(lastname="Ekui"))  # ICE Ekui
print(my_fullname("Uoi", "WANSU"))  # Uoi WANSU
print(my_fullname(firstname="ICE", lastname="WANSU"))  # ICE WANSU


def redPotion(hp):  # def คือการสร้างฟังก์ชัน
    return hp + 50  # return คือการส่งค่ากลับ


def bluePotion(mp):  # def คือการสร้างฟังก์ชัน
    return mp + 20  # return คือการส่งค่ากลับ


print(redPotion(100))  # 150
