# python operators
# arithmetic operators

x = 4+5  # addition #บวก
print(x)

x = 4-5  # subtraction #ลบ
print(x)

x = 4*5  # multiplication #คูณ
print(x)

x = 4/5  # division #หาร
print(x)

x = 4 % 5  # modulo #หารเอาเศษ
print(x)

x = 4**5  # exponentiation #ยกกำลัง
print(x)

x = 4//5  # floor division #หารเอาส่วนเต็ม
print(x)


# assignment operators
x = 5  # กำหนดค่า
print(x)

x += 5  # บวกแล้วกำหนดค่า
print(x)

x -= 5  # ลบแล้วกำหนดค่า
print(x)

x *= 5  # คูณแล้วกำหนดค่า
print(x)

x /= 5  # หารแล้วกำหนดค่า
print(x)

x %= 5  # หารเอาเศษแล้วกำหนดค่า
print(x)

x **= 5  # ยกกำลังแล้วกำหนดค่า
print(x)

x //= 5  # หารเอาส่วนเต็มแล้วกำหนดค่า
print(x)

x = x+1  # บวกแล้วกำหนดค่า
print(x)


# comparison operators
x = 5
y = 10

x == 5  # เท่ากับ
print(x == 5)  # จริง

x != 5  # ไม่เท่ากับ
print(x != 5)  # เท็จ

x > 5  # มากกว่า
print(x > 5)  # เท็จ

x < 5  # น้อยกว่า
print(x < 5)  # จริง

x >= y  # มากกว่าหรือเท่ากับ
print(x >= y)  # เท็จ

x <= y  # น้อยกว่าหรือเท่ากับ
print(x <= y)  # จริง


# logical operators
x = True
y = False

x and y  # และ
print(x and y)  # เท็จ จริงกับจริงเท่านั้น

x or y  # หรือ
print(x or y)  # จริง จริงกับเท็จ

x not y  # ไม่
print(x not y)  # เท็จ จริงกับเท็จ

x ^ y  # xor
print(x ^ y)  # จริง จริงกับเท็จ

x | y  # or
print(x | y)  # จริง จริงกับเท็จ

x ~ y  # not
print(x ~ y)  # เท็จ จริงกับเท็จ

x << y  # left shift
print(x << y)  # เท็จ จริงกับเท็จ

x >> y  # right shift
print(x >> y)  # เท็จ จริงกับเท็จ

&  # and
|  # or
~  # not
^  # xor
<<  # left shift
>>  # right shift
