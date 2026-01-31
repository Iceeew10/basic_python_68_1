# loop
# while loop
# for loop
# break
# continue
# pass
# nested loop


# while loop
i = 1
while i < 10:  # while loop คือการวนลูปไปเรื่อยๆจนกว่าจะครบเงื่อนไข
    print(i)
    if i == 7:  # if คือการตรวจสอบเงื่อนไข
        break  # break คือการหยุดการทำงาน
    i += 1  # i+=1 คือการบวก i เพิ่ม 1


# for loop
for i in range(10):  # for loop คือการวนลูปไปเรื่อยๆจนกว่าจะครบเงื่อนไข
    print(i)

for i in range(10):
    if i == 5:  # if คือการตรวจสอบเงื่อนไข
        break  # break คือการหยุดการทำงาน
    print(i)

    for i in range(10):
        if i == 5:  # if คือการตรวจสอบเงื่อนไข
            continue  # continue คือการข้ามการทำงาน
        print(i)

for i in range(10):  # for loop คือการวนลูปไปเรื่อยๆจนกว่าจะครบเงื่อนไข
    if i == 5:  # if คือการตรวจสอบเงื่อนไข
        pass  # pass คือการข้ามการทำงาน
    print(i)

for i in range(10):  # for loop คือการวนลูปไปเรื่อยๆจนกว่าจะครบเงื่อนไข
    for j in range(10):  # for loop คือการวนลูปไปเรื่อยๆจนกว่าจะครบเงื่อนไข
        print(i, j)  # print คือการแสดงผล
