# Cricket Match Simulation

This Python project simulates a thrilling cricket match between two teams. The simulation captures various aspects of the game, including player statistics, team dynamics, ball outcomes, and match results.

## Overview

The simulation consists of several classes representing different elements of the cricket match. These classes work together to create a comprehensive match experience.

### Classes

#### Player

Represents a cricket player with attributes like name, bowling, batting, fielding, running, and experience. Player statistics are stored in a dictionary for easy access.

#### Team

Represents a cricket team, comprising players, a captain, batting order, and bowlers. It offers methods for captain selection, player rotation, and bowler choice.

#### Field

Models the field conditions, considering factors such as size, fan ratio, pitch conditions, and home advantage.

#### Umpire

Acts as the game's umpire, tracking scores, wickets, and overs. It calculates ball outcomes using player and field statistics.

#### Commentator

Creates an engaging match narrative by describing key events, including ball outcomes, game information, match start, end, and final results.

#### Match

Orchestrates the entire match, setting up teams, field, umpire, and commentator. The match progresses in innings, with the first team batting followed by the second team.

## Simulation Algorithm

### Step 1: Player Creation

Generate instances of `Player` for both teams, specifying their skills and attributes.

### Step 2: Team Initialization

Create two teams (`Team`) and assign players to them. Each team selects a captain and establishes batting order and bowlers.

### Step 3: Field Conditions

Define the field conditions, including size, fan ratio, pitch conditions, and home advantage.

### Step 4: Match Setup

Specify the total number of overs for the match.

### Step 5: Match Initialization

Instantiate a `Match` object, providing the teams, field, and total overs.

### Step 6: Start the Match (`start_match()` Method)

1. Team Preparation
   - Choose captains for both teams.
   - Set up initial batting order and bowlers for both teams.

2. Game Information
   - Display essential game details using the `describe_game()` method of the commentator.

3. First Innings
   - Begin the first innings with the batting team.
   - Use the `play_innings()` method to simulate ball-by-ball play.
   - Track runs, wickets, and overs.

4. First Innings Summary
   - Conclude the first innings and record the score.

5. Reset for Second Innings
   - Reset umpire statistics.
   - Initiate the second innings for the opposing team.

6. Second Innings
   - Repeat the innings process for the second team.

7. Match Result
   - Compare the scores of both teams.
   - Announce the winner using the `describe_final_result()` method.

### Ball Play Logic (`play_innings()` Method)

1. Innings Setup
   - Initialize ball count, over count, bowler, and batsman.

2. Innings Loop
   - Loop through overs (up to the total overs).

3. Ball Loop
   - For each over, simulate 6 balls.

4. Ball Outcome Prediction
   - Predict the ball outcome using the umpire's `predict_outcome()` method.

5. Commentary
   - Describe the ball outcome using the commentator's `describe_ball()` method.
   - Update scores or wickets accordingly.

6. Over Completion
   - If 6 balls are bowled, update overs, choose a new bowler, and reset the ball count.

## Conclusion

This README provides a comprehensive guide to the cricket match simulation code, including class functionalities, key methods, and the underlying simulation algorithm. The code is available in the `cricket_match_simulation.py` file.
