# Create the Screen(Step--1)

#from turtle import Turtle, Screen

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")



#screen.exitonclick()

# Create and move a Paddle(Step--2)

#from turtle import Turtle, Screen

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#paddle = Turtle()
#paddle.shape("square")
#paddle.color("white")
#paddle.shapesize(stretch_len=1, stretch_wid=5)
#paddle.penup()
#paddle.goto(350, 0)


#def go_up():
#    new_y = paddle.ycor() + 20
 #   paddle.goto(paddle.xcor(), new_y)

#def go_down():
#    new_y = paddle.ycor() - 20
#    paddle.goto(paddle.xcor(), new_y)


#screen.listen()

#screen.onkey(go_up, "Up")

#screen.onkey(go_down, "Down")

#is_game_on = True

#while is_game_on:
#    screen.update()




#screen.exitonclick()

# Write the Paddle Class and create the Second Paddle(Step--3)


#from turtle import Turtle, Screen

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#class Paddle(Turtle):
    
 #   def __init__(self, position):
 #       super().__init__()
 #       self.shape("square")
 #       self.color("white")
 ##       self.penup()
 #       self.goto(position)

 #   def go_up(self):
 #     new_y = self.ycor() + 20
  #    self.goto(self.xcor(), new_y)

 #   def go_down(self):
 #     new_y = self.ycor() - 20
  #    self.goto(self.xcor(), new_y)


#r_paddle = Paddle((350, 0))

#l_paddle = Paddle((-350, 0))




#screen.listen()

#screen.onkey(r_paddle.go_up, "Up")

#screen.onkey(r_paddle.go_down, "Down")

#screen.onkey(l_paddle.go_up, "w")

#screen.onkey(l_paddle.go_down, "s")

#is_game_on = True

#while is_game_on:
#    screen.update()




#screen.exitonclick()

# Write the Ball Class and Make the Ball Move(Step--4)

#from turtle import Turtle, Screen

#import time

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#class Paddle(Turtle):
    
 #   def __init__(self, position):
 #       super().__init__()
  #      self.shape("square")
 #       self.color("white")
 #      self.shapesize(stretch_len=1, stretch_wid=5)
 #      self.penup()
 #      self.goto(position)

 #   def go_up(self):
 #     new_y = self.ycor() + 20
  #    self.goto(self.xcor(), new_y)

 #   def go_down(self):
 #     new_y = self.ycor() - 20
 #     self.goto(self.xcor(), new_y)


#class Ball(Turtle):
   
 #  def __init__(self):
 #     super().__init__()
 #     self.shape("circle")
 #     self.color("blue")
  #    self.penup()
    
  # def move(self):
  #    new_x = self.xcor() + 10
  #    new_y = self.ycor() + 10
   #   self.goto(new_x, new_y)


#r_paddle = Paddle((350, 0))

#l_paddle = Paddle((-350, 0))

#ball = Ball()




#screen.listen()

#screen.onkey(r_paddle.go_up, "Up")

#screen.onkey(r_paddle.go_down, "Down")

#screen.onkey(l_paddle.go_up, "w")

#screen.onkey(l_paddle.go_down, "s")

#is_game_on = True

#while is_game_on:
 #   time.sleep(0.1)
 #   screen.update()
 #   ball.move()




#screen.exitonclick()

# Detect the collision with wall and bounce(Step--5)

#from turtle import Turtle, Screen

#import time

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#class Paddle(Turtle):
    
 #   def __init__(self, position):
 #       super().__init__()
 #       self.shape("square")
 #       self.color("white")
 #       self.shapesize(stretch_len=1, stretch_wid=5)
 #       self.penup()
 #       self.goto(position)

 #   def go_up(self):
 #     new_y = self.ycor() + 20
 #     self.goto(self.xcor(), new_y)

  #  def go_down(self):
  #    new_y = self.ycor() - 20
  #    self.goto(self.xcor(), new_y)


#class Ball(Turtle):
   
 #  def __init__(self):
 #     super().__init__()
 #     self.shape("circle")
 #     self.color("blue")
 #     self.penup()
 #     self.x_move = 10
 #     self.y_move = 10
    
 #  def move(self):
 #     new_x = self.xcor() + self.x_move
 #     new_y = self.ycor() + self.y_move
 #     self.goto(new_x, new_y)


 #  def bounce(self):
 #     self.y_move *= -1
      



#r_paddle = Paddle((350, 0))

#l_paddle = Paddle((-350, 0))

#ball = Ball()




#screen.listen()

#screen.onkey(r_paddle.go_up, "Up")

#screen.onkey(r_paddle.go_down, "Down")

#screen.onkey(l_paddle.go_up, "w")

#screen.onkey(l_paddle.go_down, "s")

#is_game_on = True

#while is_game_on:
 #   time.sleep(0.1)
 #   screen.update()
 #   ball.move()


 #   if ball.ycor() > 280 or ball.ycor() < -280:
 #      ball.bounce()




#screen.exitonclick()

# Detect Collision with paddle(Step--6)

#from turtle import Turtle, Screen

#import time

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#class Paddle(Turtle):
    
 #   def __init__(self, position):
 #       super().__init__()
  #      self.shape("square")
  #      self.color("white")
 #       self.shapesize(stretch_len=1, stretch_wid=5)
 #       self.penup()
 #       self.goto(position)

 #   def go_up(self):
  #    new_y = self.ycor() + 20
  #    self.goto(self.xcor(), new_y)

 #   def go_down(self):
 #     new_y = self.ycor() - 20
  #    self.goto(self.xcor(), new_y)


#class Ball(Turtle):
   
 # def __init__(self):
  #    super().__init__()
  #    self.shape("circle")
  #   self.color("blue")
   #   self.penup()
   #   self.x_move = 10
   #   self.y_move = 10
    
 #  def move(self):
 #     new_x = self.xcor() + self.x_move
  #    new_y = self.ycor() + self.y_move
  #    self.goto(new_x, new_y)


 #  def bounce_y(self):
 #     self.y_move *= -1


  # def bounce_x(self):
   #    self.x_move *= -1      



#r_paddle = Paddle((350, 0))

#l_paddle = Paddle((-350, 0))

#ball = Ball()




#screen.listen()

#screen.onkey(r_paddle.go_up, "Up")

#screen.onkey(r_paddle.go_down, "Down")

#screen.onkey(l_paddle.go_up, "w")

#screen.onkey(l_paddle.go_down, "s")

#is_game_on = True

#while is_game_on:
#    time.sleep(0.1)
 #   screen.update()
 #   ball.move()


 #   if ball.ycor() > 280 or ball.ycor() < -280:
 #       ball.bounce_y()

 #  if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 or ball.ycor() < -340:
 #       ball.bounce_x()




#screen.exitonclick()

# How to Detect when the ball goes Out of the bounds/ Detect when the paddle misses(Step--8)

#from turtle import Turtle, Screen

#import time

#screen = Screen()
#screen.bgcolor("black")
#screen.setup(width=800, height=600)
#screen.title("Pong")
#screen.tracer(0)

#class Paddle(Turtle):
    
 #   def __init__(self, position):
#       super().__init__()
 #       self.shape("square")
 #       self.color("white")
 #       self.shapesize(stretch_len=1, stretch_wid=5)
 #       self.penup()
 #       self.goto(position)

 #   def go_up(self):
 #     new_y = self.ycor() + 20
 #     self.goto(self.xcor(), new_y)

 #   def go_down(self):
 #     new_y = self.ycor() - 20
 #     self.goto(self.xcor(), new_y)


#class Ball(Turtle):
   
 #  def __init__(self):
 #     super().__init__()
 #     self.shape("circle")
  #    self.color("blue")
 #     self.penup()
 #     self.x_move = 10
 #     self.y_move = 10
    
 #  def move(self):
 #     new_x = self.xcor() + self.x_move
 #     new_y = self.ycor() + self.y_move
 #     self.goto(new_x, new_y)


 #  def bounce_y(self):
#       self.y_move *= -1


 #  def bounce_x(self):
  #     self.x_move *= -1   


 #  def reset_position(self):
 #     self.goto(0, 0)
 #     self.bounce_x()
         



#r_paddle = Paddle((350, 0))

#l_paddle = Paddle((-350, 0))

#ball = Ball()




#screen.listen()

#screen.onkey(r_paddle.go_up, "Up")

#screen.onkey(r_paddle.go_down, "Down")

#screen.onkey(l_paddle.go_up, "w")

#screen.onkey(l_paddle.go_down, "s")

#is_game_on = True

#while is_game_on:
#    time.sleep(0.1)
#    screen.update()
 #   ball.move()


 #   if ball.ycor() > 280 or ball.ycor() < -280:
 #       ball.bounce_y()

 #   if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 or ball.ycor() < -340:
 #       ball.bounce_x()


  #  if ball.xcor() > 380:
 #      ball.reset_position()

 #   if ball.xcor() < -380:
 #      ball.reset_position()




#screen.exitonclick()

# Score Keeping and Changing the Ball Speed(Step--8)

from turtle import Turtle, Screen

import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(position)

    def go_up(self):
      new_y = self.ycor() + 20
      self.goto(self.xcor(), new_y)

    def go_down(self):
      new_y = self.ycor() - 20
      self.goto(self.xcor(), new_y)


class Ball(Turtle):
   
   def __init__(self):
      super().__init__()
      self.shape("circle")
      self.color("blue")
      self.penup()
      self.x_move = 10
      self.y_move = 10
      self.move_speed = 0.1
    
   def move(self):
      new_x = self.xcor() + self.x_move
      new_y = self.ycor() + self.y_move
      self.goto(new_x, new_y)


   def bounce_y(self):
       self.y_move *= -1


   def bounce_x(self):
       self.x_move *= -1  
       self.move_speed *= 0.9 


   def reset_position(self):
      self.goto(0, 0)
      self.move_speed = 0.1
      self.bounce_x()


class Scoreboard(Turtle):
   
   def __init__(self):
      super().__init__()
      self.color("white")
      self.penup()
      self.hideturtle()
      self.l_score = 0
      self.r_score = 0
      self.update_scoreboard()

   def update_scoreboard(self):
       self.clear()
       self.goto(-100, 200)
       self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
       self.goto(100, 200)
       self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

   def l_point(self):
       self.l_score += 1
       self.update_scoreboard()

   def r_point(self):
       self.r_score += 1
       self.update_scoreboard()
      
   
         



r_paddle = Paddle((350, 0))

l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()




screen.listen()

screen.onkey(r_paddle.go_up, "Up")

screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")

screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 or ball.ycor() < -340:
        ball.bounce_x()


    if ball.xcor() > 380:
       ball.reset_position()
       scoreboard.l_point()


    if ball.xcor() < -380:
       ball.reset_position()
       scoreboard.r_point()




screen.exitonclick()














    














    
        






























    
        
















    
        



















    
        
















    
        














    
        