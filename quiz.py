#!/Library/Frameworks/Python.framework/Versions/3.11/bin/pgzrun
from pgzrun import *
from pygame import *
WIDTH = 1280
HEIGHT = 720

main_box = Rect(0, 0, 820, 240)
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40)
timer_box.move_ip(990, 40)
answer_box1.move_ip(50, 358)
answer_box2.move_ip(735, 358)
answer_box3.move_ip(50, 558)
answer_box4.move_ip(735, 558)
answer_boxs = [answer_box1, answer_box2, answer_box3, answer_box4]

score = 0
time_left = 30

q1 = ["The ‘Felifors’ spell turns a cat into a what?", "Hat", "Bat", "Matchbox", "Cauldron", 3]
q2 = ["Who wrote the 7-book series titled ‘The Standard Book of Spells’?", "Kennilworthy Whisp", "Rita Skeeter", "Bathilda Bagshot", "Miranda Goshawk", 4]
q3 = ["Finish the inscription on Dobby’s tombstone: ‘Here lies Dobby…", "‘A true friend’", "‘The best servant’", "‘A free Elf’", "‘Master of socks’", 3]
q4 = ["What are the names of Severus Snape's parents?", "Toby Snape and Elly Priest", "Tobias Snape and Ellen Prince", "Tobias Snape And Eileen Prince", "Tony Snape and Eileen Prince", 3]
q5 = ["What is the name of the Quidditch move where a seeker fake's seeing the snitch and dives to the ground but pulls out of the dive just in time, but the opposing seeker plummets to the ground?", "Wonky Fent", "Wonky Faint", "Wronsky Feint", "Wronsky Faint", 4]
q6 = ["What is Dumbledore's scar above his left knee a perfect map of?", "The London Underground", "The secret passageways of Hogwarts", "The Hogwarts Library", "England", 1]
q7 = ["Why did Cormac McLaggen miss the Quidditch tryouts in the year previous to Harry Potter and the Half-Blood Prince?", "He grew an extra leg due to a dueling accident", "He was in detention for melting his cauldron in potions class", "He broke his knee when he fell through a trick step", "He ate a pound of doxy eggs for a bet", 4]
q8 = ["What is the password to the Prefect's Bathroom on the fifth floor?", "Power", "Pine Fresh", "Oak Leaf", "Toffe", 2]
q9 = ["What was on the calendar Bodric Bode received for Christmas in the fifth book?", "Hippogriffs", "Blast-Ended Skrewts", "Dragons", "Unicorns", 1]
q10 = ["How many staircases are there in Hogwarts?", "364", "994", "142", "993", 3]

questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
question = questions.pop(0)

def draw():
    screen.fill("dim gray")
    screen.draw.filled_rect(main_box, "sky blue")
    screen.draw.filled_rect(timer_box, "sky blue")

    for box in answer_boxs:
        screen.draw.filled_rect(box, "orange")
    
    screen.draw.textbox(str(time_left), timer_box, color =("black"))
    screen.draw.textbox(question[0], main_box, color =("black"))

    index = 1
    for box in answer_boxs:
        screen.draw.textbox(question[index], box, color =("black"))
        index += 1

def game_over():
    global question, time_left
    message = f"Game over. You got {str(score)} questions correct"
    question = [message, "-", "-", "-", "-", 5]
    time_left = 0

def correct_answer():
    global question, score, time_left
    time_left = 30
    score += 1
    if questions:
        question = questions.pop(0)
        time_left += 3
    else:
        print("End of questions")
        game_over()

def incorrect_answer():
    global question, time_left
    
    time_left = 30

    if questions:
        question = questions.pop(0)
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos):
    index = 1
    for box in answer_boxs:
        if box.collidepoint(pos):
            print(f"Clicked on answer {index}")
            if index == question[5]:
                print("You got it correct!")
                correct_answer()
            else:
                print("Incorrect")
                incorrect_answer()
        index += 1

def update_time_left():
    global time_left

    if time_left:
        time_left = time_left -1
    else:
        game_over()

clock.schedule_interval(update_time_left, 1.0)
go()