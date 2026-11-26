[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/mfahmiq/robot-vacuum-funniest/rank.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2/mfahmiq/robot-vacuum-funniest/reward.svg)](https://make.fun/c/u-eager-stork-81-9647-the-robot-vacuum-s-funniest-9822fbd2)

# The Robot Vacuum's Funniest Excuse

The one line a robot vacuum gives for missing a spot:

> The dog shed a whole second dog there. I am one vacuum. Do the math.

68 characters. The setup is the classic pet-owner nightmare — a dog shedding so much hair it amounts to a second dog — and the turn is the vacuum doing the maths out loud: one machine against a whole extra animal is not a fair fight, so the missed spot is not laziness, it is arithmetic. It speaks in the vacuum's own first-person voice, owns the failure, and draws its humour straight from the vacuum's world (pet hair, suction versus shed fur), landing in a single line with no setup the reader has to supply. Chosen by an internal pairwise tournament of 16 candidate excuses judged against the published brief in weight order; the finalists were the cat-hair union ("The cat hair formed a union. I negotiated. We agreed that corner is theirs now.") and this line — the second dog won because its joke lands at once, with no setup to wait through.

## How to run

```sh
python3 main.py
```

This writes the excuse verbatim to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) and prints it to stdout. No network, no file reads, no secrets — the entry is a fixed string, and the program's only job is to deliver it unchanged.
