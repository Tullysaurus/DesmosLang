# DesmosLang
## A Turing-Complete programming language written fully in Desmos
### View the graph here: https://www.desmos.com/calculator/n7ovjgbhod

You can view the full set of instructions [here](Instruction_Set.txt)

The graph already has a program loaded, which I will explain below.

Here is the assembly code for the pre-loaded program:
```
; This is a simple program to square a number (starting at 2)
; 3 times, so it should return 2^2^2^2 = 65536 in address 16.
; Theres a reference sheet for the instructions in the "Encoder.py" file

set %4 to 12
allc %4                     ; Allocate 12 bytes of memory (16 total + 1 extra)

set %15 to 3                ; How many times to loop
set %16 to 2                ; Initialize %16 to 2

set %4 to 0
jmp to 8 if %15 neq %4

hlt                         ; Stop the program if the loop ends

mult %16 and %16            ; Square &16
mov %4 to %16               ; Store &16 ^ 2 in %16

dec %15                     ; Decrement %15

set %4 to 5
jmp %4                      ; Jump to the start of the loop
```
