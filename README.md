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

## Process
```mermaid
flowchart TD
start(((START)))
food[Food Module]
snake[Snake Module]
scoreboard[Scoreboard Module]
main[Main Game Module]
refresh_food[Refresh Food]
display[Display Scoreboard]
reset_scoreboard[Reset Scoreboard]
update_scoreboard[Update Scoreboard]
increase_score[Increase Score]
create_snake[Create Snake]
reset_snake[Reset snake]
control[Controls Snake Vovement ]
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

