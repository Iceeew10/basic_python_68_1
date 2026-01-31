# condition

a = 10
b = 20
print(a)
print(b)

if a > b:  # ถ้า a มากกว่า b
    print("a is greater than b , ใช่ a มากกว่า b")  # พิมพ์ a มากกว่า b
elif a == b:  # ไม่เช่นนั้นถ้า a เท่ากับ b
    print("a is equal to b , ใช่ a เท่ากับ b")  # พิมพ์ a เท่ากับ b
else:  # ไม่เช่นนั้น
    print("a is less than b , ใช่ a น้อยกว่า b")  # พิมพ์ a น้อยกว่า b

# loop
for i in range(10):  # วนลูป 10 ครั้ง
    print(i)  # พิมพ์ i

while i < 15:  # วนลูปจนกว่า i จะไม่น้อยกว่า 10
    print(i)  # พิมพ์ i
    i += 1  # บวก i เพิ่ม 1
