#Lets create our old nokia phone SNAKE GAME with Sunder's method
"""
OVERVIEW:
->The snake is going to be created by list in 2D matrix connected with each other or we can say that it is continuous.
->we are going to clear the screen for each move to play the game and experience some gaming look.
->Arrows and w,s,a,d are used to change the direction.
->If the snake hits the end of row or column or it touches it's own body, the game will over.
->The food is generated randomly in the matrix except snake body.
->The snake size and speed will increase if it eats the food.


ALGORITHM:

1. IMPORT required libraries or modules:
  1.1 Sunder need keyboard library to read the click in keyboard.
  1.2 Sunder need random to generate food for snake inside matrix.
  1.3 Sunder need os to use terminal commands in program to clear the screen for each move.
     1.3.1 We need to do this because if the screen is not cleared, we may not experience the moving effect of snake.
     1.3.2 Another reason is ,idle does not support much running commands while execution,it supports but,we may not
           expect the efficiency ,speed and screen in it. So we are going to play it in windows or linux terminal.
  1.4 Sunder use time to delay speed of snake's move, so that sunder can experience the movement and can able to
      play. If there is no delay, the change in head or movement will be very fast and we can't able to play.
      
2. Next we are going to intialize the height and width of the board. We can change it according to the view.

3. Now we are going to set directions ,like in which direction what should be done.
  3.1 For up, the row should be decrease and column remain same.
  3.2 For down, the row should increase and again column remains same.
  3.3 For right, column should increase and row remains same.
  3.4 For left, column should decrease and row remains same.
  
4. Next sunder creating a function to clear the terminal screen. I'm using inbuilt function system from os module.
  4.1 For windows ,we use "cls", The os return NewTechnology as the name for windows.
  4.2 For linux ,we use "clear"
  
5. Now let's create a function to print the board where we get the positions of snake body and food as parameter:
  5.1 Before printing the board each time for each moment,we should clear the screen. So sunder calling
      clear_screen() at first in print_board() function.
  5.2 First make it clear sunder..Board height is no.of rows and Board width is no.of columns.
  5.3 I'm going to create 2 nested loop. First is for height or row and second is for width or column of the board.
  5.4 Let sunder make it clear again that we are going to make the game movement only by fast and continous
      printing of board with snake body and food.
  5.5 So whenever we are printing the board, we should remember the points of snake body and food.
     5.5.1 If the points (i,j) of row and col loop lies in snake points list, we should print "O" as it mention
           snake's body.
     5.5.2 Else If the points (i,j) is equal to food list, we should print "X", as it mention the food in the board.
     5.5.3 Else we can print "." to mention the board as it is not the part of snake body or food.
  5.6 Sunder prints empty line after each row gets completed and finally we printing the score according to the
      size of snake's body.
      
6. Next Sunder is moving to the function which moves the snake where i get the points of snake's body and direction
   of the snakeas parameters:
   6.1 Let Sunder break down the steps for how the snake will be moved.
      6.1.1 We are not going to make any animations, we do this by a simple method by making the points in the
            board as the part of snake's body according to the direction where we get it from user.
      6.1.2 The points in board will become the new head of the snake according to the direction. For each movement
            each points in the board will become as new head for the snake moving in the direction.
   6.2 From the points of snake's body, we will get the snake's head position or index, which is always in the
       0th index of the snake's body points.
   6.3 From the head points, we should add the direction points. Let take an example..if the head is in position
       (4,8), if user wants to move the snake to right side ,then we should change the points as..(4,9). Now this
       is the new_head of the snake.
   6.4 Now we should insert the new head in the 0th index of snake body points list and return the new_head.

7. Now let's create function to generate food points in the board, we get snake's body points as parameter.
   7.1 We should generte food where its points or index range from 0 to height-1 and 0 to width-1.
   7.2 We must make sure that the food generated is not in the snake body points.

8. We completed all the sub functions..So sunder is going to jump into the main function where we will use all
   this sub functions whenever it is needed...
   8.1 Firstly intialize the snake points list with a random index for its head to start. Next intialize a variable
       with any direction where the head starts to move in the starting without any user inputs.
   8.2 Then call the food generation function and start it in the food variable and let's set the game_over boolean
       variable as False.
   8.3 Now Sunder moving to the main game loop..while not game_over or until the game_over set to True, this while
       loop will run..
      8.3.1 From the keyboard library i'm using is_pressed() function to get the input key pressed by user.
      8.3.2 If the keyboard.is_pressed("up") condition will be done if the up arrow is pressed. we are also going
            to use "w" to change the direction upwards and we must also make sure that direction is not equal to
            DIRECTION["Down"] because if the snake is moving downwards, it cannot be changed directly upwards.
      8.3.3 Similarly for all other directions, the above step should be done accordingly. We also use "a","s" and "d"
            keys for left, down and right directions. We must also need tocheck whether the direction is opposite to
            the DIRECTION[].
      8.3.4 Now we should send this new direction of snake to the move_snake() function with snake points. This
            function will return the new_head position, so we need to store it in new_head.
      8.3.5 Then we are going to check whether this new head is in the valid position or not: 3 conditions
           8.3.5.1 The snake may hit the end of the board with respect to the board's height, it may hit in top or in
                   bottom. So the row of the new_head, which is new_head[0] should be in the range 0 to BOARD_HEIGHT.
                   if new_head[0] <0 or >=BOARD_HEIGHT ,it means snake hits the board, so we should change the
                   BOOLEAN variable game_over to TRUE and break the loop.
           8.3.5.2 Repeat the above step accordingly, if snake hit the board horizontally with respect to
                   board's width. The 2 changes are, we should check with new_head[1] because the 2nd position
                   represents the column and check with BOARD_WIDTH.
           8.3.5.3 The last condition is to check whether the snake hits on it's own body. It is very simple, if
                   the new_head is in snake list, it means it hits it's own body. YEAH!!! the thinking is right
                   new_head is the current head in snake list,so it is always there, so we should exclude the
                   head position while checking. From 1st index we need to check [1:]
           8.3.5.4 If any of this 3 conditions satisfied, we should change game_over to True and break the while loop.
      8.3.6 If new_head is in valid position, then we need to check whether the head is equal to food.
           8.3.6.1 If it is so, it means the snake has eaten the food, we need to generate new food and store it in
                   food. we should send the snake points list to generate_food() function. Now food has newly
                   generated food index.
           8.3.6.2 Else if the snake has not eaten the food, then we need to remove the last point from the snake list
                   or we can say that we need to pop the snake list to maintain the length of the snake. Because snake
                   head is increasing to next point according to the direction to make the movement, if it has not
                   eaten food it should remain in same size, so we simultaneously popping the last element from snake
                   list. If the snake has eaten the food, we won't pop, so the size of the snake will increase by one
                   by adding new_head.
      8.3.7 Finally Sunder is going to print the board with all updated snake list,head,food and direction. Just we
            need to call the print_board(snake,food) function.
      8.3.8 Let's come to the final set up, Now Sunder is setting a small delay in game, so that game will be in
            playable state. If this delay is not set, it is impossible to play the game due to high speed and screen
            change. We use time.sleep() to make the delay. Delay the time according to length of the snake.
   8.4 Now the while loop completed, let's print the final score of the user, which is len(snake)-2.
9. At last call the main() function.
10. Now our snake_game is ready. Go to terminal and move to the file location and type snake_game_project.py to
    play the game..ENJOY the game!!!
            
                                            THANK YOU!!!                                        by ~ M.Sunderesan
                                                                                                Sathyabama-(2022-2026)            
"""
#Let's begin the coding

#Libraries
import keyboard
import random
import os
import time

#Dimension of the board
BOARD_HEIGHT = 30
BOARD_WIDTH = 60

#Directions
DIRECTION={
    "UP":(-1,0),
    "DOWN":(1,0),
    "RIGHT":(0,1),
    "LEFT":(0,-1)
    }

def clear_screen():
    os.system("cls" if os.name=="nt" else "clear")

def print_board(snake,food):
    clear_screen()
    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if (i,j) in snake:
                print("O", end="")
            elif (i,j) == food:
                print("X", end="")
            else:
                print("." ,end="")
        print()
    print(f"Score: {len(snake) - 1}")

def move_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0] , head[1] + direction[1])
    snake.insert(0, new_head)
    return new_head

def generate_food(snake):
    while True:
        food = (random.randint(1, BOARD_HEIGHT - 2), random.randint(1, BOARD_WIDTH - 2))
        if food not in snake:
            return food

def main():
    snake = [(7,10)]
    direction = DIRECTION["RIGHT"]
    food = generate_food(snake)
    game_over = False

    while not game_over:
        #keyboard press event handling
        if( ( keyboard.is_pressed("up") or keyboard.is_pressed("w") ) and direction != DIRECTION["DOWN"] ):
            direction = DIRECTION["UP"]
        elif( ( keyboard.is_pressed("down") or keyboard.is_pressed("s") ) and direction != DIRECTION["UP"] ):
            direction = DIRECTION["DOWN"]
        elif( ( keyboard.is_pressed("right") or keyboard.is_pressed("d") ) and direction != DIRECTION["LEFT"] ):
            direction = DIRECTION["RIGHT"]
        elif( ( keyboard.is_pressed("left") or keyboard.is_pressed("a") ) and direction != DIRECTION["RIGHT"] ):
            direction = DIRECTION["LEFT"]

        #move the snake
        new_head = move_snake(snake, direction)

        #check new_head with every possibilities
        if (
            new_head[0] < 0 or new_head[0] >= BOARD_HEIGHT or
            new_head[1] < 0 or new_head[1] >= BOARD_WIDTH or
            new_head in snake[1:]
            ):
            game_over = True
            break

        if new_head == food:
            food = generate_food(snake)
        else:
            snake.pop()

        #print the board with updated values
        print_board(snake, food)

        #control game speed
        n=len(snake)
        
        if n<=5:
            x=0.2
        elif n<=10:
            x=0.15
        elif n<=15:
            x=0.1
        elif n<=20:
            x=0.09
        elif n<=25:
            x=0.08
        elif n<=30:
            x=0.07
        elif n<=35:
            x=0.06
        elif n<=40:
            x=0.05
        elif n<=45:
            x=0.04
        elif n<=50:
            x=0.03
        elif n<=70:
            x=0.02
        else:
            x=0.01

        time.sleep(x)

    print("Game over!! Your score is: ", len(snake) - 2)

main()

