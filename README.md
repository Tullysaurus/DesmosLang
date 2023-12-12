# DesmosLang
## A Turing-Complete programming language written fully in Desmos
### View the graph here: https://www.desmos.com/calculator/xuxgy2fmnx

You can view the full set of instructions [here](Instruction_Set.txt)

The graph already has a program loaded, which I will explain below.

Here is the assembly code for the pre-loaded program:
```
; This is a simple program to square a number (starting at 2)
; 3 times, so it should return 2^2^2^2 = 65536 in address 16.

set %4 to 12                ; Set the amount of memory we want to allocate
allc %4                     ; Allocate 12 bytes of memory (4 to start + 12 = 16 bytes total)

set %15 to 3                ; How many times to loop
set %16 to 2                ; Initialize %16 to 2

set %4 to 0
jmp to 8 if %15 neq %4      ; Skip the halt instruction if %15 is not equal to 0

hlt                         ; Stop the program if the loop ends

mult %16 and %16            ; Square &16
mov %4 to %16               ; Move the result back into %16

dec %15                     ; Decrement %15

set %4 to 5                 ; Set the target jump address
jmp %4                      ; Jump to the target jump address
```

This gives us the following:
```
Program Memory:  [3, 2, 3, 3, 3, 6, 14, 9, 13, 11, 3, 4]
Program Args:  [4, 12, 0, 4, 0, 0, 15, 3, 0, 16, 2, 0, 4, 0, 0, 15, 4, 8, 1, 0, 0, 16, 16, 0, 16, 4, 0, 15, 0, 0, 4, 5, 0, 4, 0, 0]
```
Which we plug into the graph inside the "► Memory" Folder.
