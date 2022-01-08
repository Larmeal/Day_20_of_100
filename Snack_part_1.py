from turtle import Turtle, Screen, color
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The snack game")
# ทำให้ภาพดู smooth ขึ้นมาก
screen.tracer(0)

position_snack = [(0, 0), (-20, 0), (-40, 0)]
segment = []

# เป็นการวน loop ใน position_snack เพื่อ genarate งู ในแต่ละตำแหน่งขึ้นมา
for i in position_snack:
    snack = Turtle(shape="square")
    snack.color("White")
    snack.penup()
    # งูตัวแรกถูก genarate ไว้ที่บนิเวณ 0, 0 --> ตัวที่ 2 ที่ -20, 0 --> ตัวที่ 3 ที่ -40, 0
    snack.goto(i)
    # เติม instance ของงูที่ถูก genarate ขึ้นมาทั้ง 3 ตัว 
    segment.append(snack)

again = True
while again:
    # ทำให้หน้าจออัพเดทอยู่ตลอด
    screen.update()
    # ทำให้หน้าจออัพเดทเร็วขึ้น
    time.sleep(0.1)
    # เป็นการสร้าง loop ในการเคลือนที่ของงู โดย concept มันคือการนำงูตัวที่ถูก genarate มาทีละตัวเคลื่อนที่ไปทับตำแหน่งงูที่ถูก genarate มาก่อนหน้า
    # เพื่อแก้ปัญหาให้เวลาที่งูเลี้ยว ซ้าย - ขวา จะได้ไม่มีปัญหาเกิดขึ้น
    # ที่ให้ตำแหน่ง start เป็น len(segment) ก็เพราะว่าในกรณีที่ปริมาณงูเพิ่มขึ้นจะได้ วน loop งูได้ครบทุกตัว
    for n in range(len(segment) - 1, 0, -1):
        # เป็นการกำหนด position ใหม่ให้กับงูตัวแต่ละตัว เข้าไปแทนที่งูที่ตำแหน่งก่อนหน้า โดยที่ n-1 ก็เพราะว่า งูที่ n = 2 จะได้ไปแทนในตำแหน่งของงูที่ n = 1
        # เพราะฉะนั้นแล้วตำแหน่งแรกเริ่มของ position_snack จึงสำคัญมากในกา่รเริ่มสร้างเกมงู 
        position_x = segment[n - 1].xcor()
        position_y = segment[n -1].ycor()
        # ให้งูตำแหน่งที่ n เครื่องที่ไปยัง งูในตำแหน่งก่อนหน้า แปลว่าในขึ้นตอนนี้ งู 2 ตัวจะซ้อนทับกันอยู่ แต่เมื่อวน loop เสร็จ งูทั้งหมดจะเคลื่อนที่ไปยังตำแหน่งที่ใหม่ขึ้น
        segment[n].goto(position_x, position_y)
    segment[0].forward(20)
    segment[0].left(90)

screen.exitonclick()