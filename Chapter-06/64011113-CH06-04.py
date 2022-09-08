"""
Chapter : 6 - item : 4 - หอคอยแห่งฮานอย
 ส่งมาแล้ว 0 ครั้ง
เขียนโปรแกรมแก้ปัญหา หอคอยแห่งฮานอย โดยเราจะมีแทงไม้อยู่3แท่งคือ A B C และรับ input เป็นจำนวนแผ่นไม้ที่วางซ้อนกันให้แสดงลำดับการย้ายแผ่นไม้ทั้งหมดจากแท่ง A ไปยัง แท่งC โดยแผ่นไม้ที่มีขนาดเล็กกว่าจะอยู่ข้างบนแผ่นไม้ที่มีขนาดใหม่กว่าเสมอ(ห้ามวางแผ่นเล็กกว่าไว้ข้างล่าง)

****ห้ามใช้คำสั่ง for, while, do while*****

หมายเหตุ ทุกฟังก์ชันต้องมี parameter มากที่สุดไม่เกิน 5 ตัว

คำแนะนำ ให้สร้างฟังก์ชันสำหรับแสดงผล แยกต่างหาก และใช้ list ในการเก็บข้อมูลของแท่งไม้แต่ละแท่ง
และให้ระวังเรื่องการสลับ list ให้ดีๆ

หากมีข้อสงสัยเกี่ยวกับ หอคอยแห่งฮานอย สามารถสอบถาม TA เพิ่มเติม หรือ ลองเล่นได้ที่ https://www.mathsisfun.com/games/towerofhanoi.html

def move(n,A,B,C,maxn):
    #code here
n = int(input("Enter Input : "))

Enter Input : 3
|  |  |
1  |  |
2  |  |
3  |  |
move 1 from  A to C
|  |  |
|  |  |
2  |  |
3  |  1
move 2 from  A to B
|  |  |
|  |  |
|  |  |
3  2  1
move 1 from  C to B
|  |  |
|  |  |
|  1  |
3  2  |
move 3 from  A to C
|  |  |
|  |  |
|  1  |
|  2  3
move 1 from  B to A
|  |  |
|  |  |
|  |  |
1  2  3
move 2 from  B to C
|  |  |
|  |  |
|  |  2
1  |  3
move 1 from  A to C
|  |  |
|  |  1
|  |  2
|  |  3




Enter Input : 4
|  |  |
1  |  |
2  |  |
3  |  |
4  |  |
move 1 from  A to B
|  |  |
|  |  |
2  |  |
3  |  |
4  1  |
move 2 from  A to C
|  |  |
|  |  |
|  |  |
3  |  |
4  1  2
move 1 from  B to C
|  |  |
|  |  |
|  |  |
3  |  1
4  |  2
move 3 from  A to B
|  |  |
|  |  |
|  |  |
|  |  1
4  3  2
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
4  3  2
move 2 from  C to B
|  |  |
|  |  |
|  |  |
1  2  |
4  3  |
move 1 from  A to B
|  |  |
|  |  |
|  1  |
|  2  |
4  3  |
move 4 from  A to C
|  |  |
|  |  |
|  1  |
|  2  |
|  3  4
move 1 from  B to C
|  |  |
|  |  |
|  |  |
|  2  1
|  3  4
move 2 from  B to A
|  |  |
|  |  |
|  |  |
|  |  1
2  3  4
move 1 from  C to A
|  |  |
|  |  |
|  |  |
1  |  |
2  3  4
move 3 from  B to C
|  |  |
|  |  |
|  |  |
1  |  3
2  |  4
move 1 from  A to B
|  |  |
|  |  |
|  |  |
|  |  3
2  1  4
move 2 from  A to C
|  |  |
|  |  |
|  |  2
|  |  3
|  1  4
move 1 from  B to C
|  |  |
|  |  1
|  |  2
|  |  3
|  |  4






"""