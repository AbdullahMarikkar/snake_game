from turtle import  Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()
    
    
screen.listen()
screen.onkey(snake.up,"Up")    
screen.onkey(snake.down,"Down")    
screen.onkey(snake.right,"Right")    
screen.onkey(snake.left,"Left")    

    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    #Detect Collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()



screen.exitonclick()