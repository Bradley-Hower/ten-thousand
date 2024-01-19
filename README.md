# LAB - Class 06, 07, 08

Project: Ten Thousand - version 1
Author: Bradley Hower in collaboration with Brendan Huddleston and Errol Vidad

Most output was driven by ChatGPT 4.0. Some poking was needed.

Prompt history: https://chat.openai.com/share/2333d450-080e-4df3-a369-b545a0b53995

See prompts doc for print out.

## How to initialize/run your application (where applicable)

Game logic:

`python3 ten_thousand_pack/game_logic.py`

To play the game:

`python3 -m ten_thousand_pack.game`

## Tests

### How do you run tests?

Run tests via `pytest`. To install, `pip install pytest`.

### Any tests of note?

The test file test_roll_dice includes testing for dice rolls of various numbers and confirmation that all rolls return values between 1 and 6.

The test file test_caculate_score tests for scoring of different variations including:

+ Singles of a number
+ Doubles of a number
+ Two singles of two numbers
+ A single non-scoring roll

---

+ Threes of a number, including of ones
+ Three ones and a single of a number
+ A straight
+ Three of a kind, four of a kind, five of a kind and six of a kind
+ Six ones

---

+ Two pairs
+ Three pairs
+ Two triples

## Version II Test

All tests are gameplay driven. See tests/version_2 for test cases.
