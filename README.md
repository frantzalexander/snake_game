# Snake Game


## Project Overview
This is a game where the Player controls a white snake.

The player gains points by eating the red food within the bounds of the screen.

## Objectives
- Create the screen.
- Create the snake and the ability to move.
- Create the scoreboard.
- Detect collision with food.
- Detect collision with the wall.
- Detect collision with the snake body.

## Results
The snake gains a segment with each food the snake eats. 


The game is over when the snake collides with the wall or with the body.


The high score is saved and updated for future gameplay.

![image](https://github.com/frantzalexander/snake_game/assets/128331579/9161a82c-7931-4dba-b87e-16df73482a1c)



## Process
```mermaid
flowchart TD
start(((START)))
food(Food Module)
snake(Snake Module)
scoreboard(Scoreboard Module)
main(Main Game Module)
refresh_food[Refresh Food]
display[Display Scoreboard]
reset_scoreboard[Reset Scoreboard]
update_scoreboard[Update Scoreboard]
increase_score[Increase Score]
create_snake[Create Snake]
reset_snake[Reset snake]
control[Controls Snake Movement ]
segment[Add Snake Segment]
detect_wall{Detect Collision: Wall}
detect_food{Detect Collision: Food}
detect_tail{Detect Collisoin: Tail}
increase_score2[Increase Score]
add_segment[Add New Segment]
refresh_food2[Place Food In New Location]
reset_snake2[Reset Snake]
reset_scoreboard2[Reset Scoreboard]
finish(((END)))
start --> food
start --> snake
start --> scoreboard
food --> refresh_food
refresh_food --> main
scoreboard --> display
display --> reset_scoreboard
reset_scoreboard --> update_scoreboard
update_scoreboard --> increase_score
increase_score --> main
snake --> create_snake
create_snake --> reset_snake
reset_snake --> control
control --> segment
segment --> main
main --> detect_food
main --> detect_wall
main --> detect_tail
detect_food --> increase_score2
increase_score2 --> add_segment
add_segment --> refresh_food2
refresh_food2 --> finish
detect_wall --> reset_snake2
reset_snake2 --> reset_scoreboard2
detect_tail --> reset_snake2
reset_scoreboard2 --> finish
