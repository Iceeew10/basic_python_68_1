# collection of python
# list
# tuple
# set
# dictionary


# list คือข้อมูลที่เก็บได้หลายอย่าง
this_list = ["apple", "banana", "cherry"]
print(this_list)
print(this_list[0])  # apple
print(this_list[1])  # banana
print(this_list[2])  # cherry
print(type(this_list))
print(len(this_list))


# tuple คือข้อมูลที่เก็บได้หลายอย่างแต่แก้ไขไม่ได้
tuple = ("apple", "banana", "cherry")
print(tuple)
print(tuple[0])  # apple
print(tuple[1])  # banana
print(tuple[2])  # cherry
print(type(tuple))
print(len(tuple))

# set คือข้อมูลที่เก็บได้หลายอย่างแต่แก้ไขไม่ได้และไม่ซ้ำกัน
set = {"apple", "banana", "cherry"}
print(set)
print(type(set))
print(len(set))

# dictionary คือข้อมูลที่เก็บได้หลายอย่างแต่แก้ไขไม่ได้และไม่ซ้ำกันและมี key
dictionary = {"brand": "ford", "model": "mustang", "year": 1964}
print(dictionary)
print(type(dictionary))
print(len(dictionary))
print(dictionary["brand"])  # ford
print(dictionary["model"])  # mustang
print(dictionary["year"])  # 1964
