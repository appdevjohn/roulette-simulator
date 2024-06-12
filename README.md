# Roulette Simulator

Simulates roulette games until the strategy fails. Right now, the strategy being used 
is the Martingale system. The strategy fails when the bet required to make up a loss 
exceeds the balance of the player.

## Running on your machine.

1. Ensure Python is installed on your local machine.
2. Run `python roulette-simulator.py` in the script's directory.

## Sample Output

The sample output reflects a scenario where the min bet is $5, the max bet is $5000, and 
the player starts with $500.
```
Strategy failed at game #47; $265 left; 16 wins and 31 losses; peaked at $580
Strategy failed at game #26; $230 left; 9 wins and 17 losses; peaked at $545
Strategy failed at game #42; $270 left; 17 wins and 25 losses; peaked at $585
Strategy failed at game #44; $270 left; 17 wins and 27 losses; peaked at $585
Strategy failed at game #124; $145 left; 56 wins and 68 losses; peaked at $780
Strategy failed at game #198; $370 left; 101 wins and 97 losses; peaked at $1005
Strategy failed at game #21; $215 left; 6 wins and 15 losses; peaked at $530
Strategy failed at game #111; $110 left; 49 wins and 62 losses; peaked at $745
Strategy failed at game #110; $125 left; 52 wins and 58 losses; peaked at $760
Strategy failed at game #348; $45 left; 164 wins and 184 losses; peaked at $1320
Strategy failed at game #26; $240 left; 11 wins and 15 losses; peaked at $555
Strategy failed at game #97; $115 left; 50 wins and 47 losses; peaked at $750
Strategy failed at game #6; $185 left; 0 wins and 6 losses; peaked at $500
Strategy failed at game #28; $250 left; 13 wins and 15 losses; peaked at $565
Strategy failed at game #103; $105 left; 48 wins and 55 losses; peaked at $740
Strategy failed at game #118; $150 left; 57 wins and 61 losses; peaked at $785
Strategy failed at game #40; $295 left; 22 wins and 18 losses; peaked at $610
Strategy failed at game #57; $285 left; 20 wins and 37 losses; peaked at $600
Strategy failed at game #55; $0 left; 27 wins and 28 losses; peaked at $635
Strategy failed at game #511; $485 left; 252 wins and 259 losses; peaked at $1760
Strategy failed at game #110; $110 left; 49 wins and 61 losses; peaked at $745
Strategy failed at game #170; $265 left; 80 wins and 90 losses; peaked at $900
Strategy failed at game #51; $260 left; 15 wins and 36 losses; peaked at $575
Strategy failed at game #153; $210 left; 69 wins and 84 losses; peaked at $845
Strategy failed at game #543; $485 left; 252 wins and 291 losses; peaked at $1760
Strategy failed at game #218; $410 left; 109 wins and 109 losses; peaked at $1045
Strategy failed at game #484; $385 left; 232 wins and 252 losses; peaked at $1660
Strategy failed at game #103; $145 left; 56 wins and 47 losses; peaked at $780
Strategy failed at game #94; $85 left; 44 wins and 50 losses; peaked at $720
Strategy failed at game #30; $270 left; 17 wins and 13 losses; peaked at $585
Strategy failed at game #289; $565 left; 140 wins and 149 losses; peaked at $1200
Strategy failed at game #186; $305 left; 88 wins and 98 losses; peaked at $940
Strategy failed at game #23; $230 left; 9 wins and 14 losses; peaked at $545
Strategy failed at game #9; $190 left; 1 wins and 8 losses; peaked at $505
Strategy failed at game #111; $125 left; 52 wins and 59 losses; peaked at $760
Strategy failed at game #39; $255 left; 14 wins and 25 losses; peaked at $570
Strategy failed at game #242; $435 left; 114 wins and 128 losses; peaked at $1070
Strategy failed at game #1500; $1555 left; 722 wins and 778 losses; peaked at $4110
Strategy failed at game #18; $225 left; 8 wins and 10 losses; peaked at $540
Strategy failed at game #6; $185 left; 0 wins and 6 losses; peaked at $500
Strategy failed at game #167; $250 left; 77 wins and 90 losses; peaked at $885
Strategy failed at game #41; $280 left; 19 wins and 22 losses; peaked at $595
Strategy failed at game #47; $285 left; 20 wins and 27 losses; peaked at $600
Strategy failed at game #74; $35 left; 34 wins and 40 losses; peaked at $670
Strategy failed at game #194; $315 left; 90 wins and 104 losses; peaked at $950
Strategy failed at game #512; $405 left; 236 wins and 276 losses; peaked at $1680
Strategy failed at game #216; $405 left; 108 wins and 108 losses; peaked at $1040
Strategy failed at game #84; $50 left; 37 wins and 47 losses; peaked at $685
Strategy failed at game #311; $560 left; 139 wins and 172 losses; peaked at $1195
Strategy failed at game #630; $715 left; 298 wins and 332 losses; peaked at $1990
```
