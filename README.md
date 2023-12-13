# DesmosLang
## A Turing-Complete programming language written fully in Desmos
### View the graph here: https://www.desmos.com/calculator/qnbb1stpiz

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
Which we plug into the graph inside the "► Memory" Folder. And run the program

# Instruction Set
```
Any time theres a "&" or a "%" in front of a number,
that is only there to make the code easier to read.

    &#  : value of %#        (not required)
    %#  : address number #   (not required)
    ;   : Just a comment, anything after this character will not be registered

Default Memory Layout:
  %1  : Program Pointer (index of what instruction we need to run)
  %2  : Whether not the program is running.
  %3  : Argument Index (Not Typical) (index of the argument(s) that we need to use)
  %4  : Output (Where most operations store their results)
  %-1 : (The last byte) a redundant byte because desmos is stupid


Instructions:

  Template:
    (Instruction Name) (OPCode, (Number of arguments the instruction requires) ): (The shortened name of the instruction; what you write in "Code.txt")
  
  
  Read (OPCode 1, 1 args(s)): read
      Gets the value from &arg1 and stores it in %4.
  
  Allocate (OPCode 2, 1 arg(s)): allc
      Allocates &arg1 bytes to memory.
  
  Write (OPCode 3, 2 arg(s)): set
      Writes arg2 to %arg1.
  
  Jump (OPCode 4, 1 arg(s)): jmp
      Jumps to &arg1.
  
  Restart (OPCode 5, 0 arg(s)): rst
      Restarts the program from scratch, resetting the memory.
  
  Jneq (OPCode 6, 3 arg(s)): jne
      Jumps to arg3 if &arg1 does not equal &arg2.
  
  Add (OPCode 7, 2 arg(s)): add
      Adds &arg2 to &arg1 and stores the result in %4.
  
  Sub (OPCode 8, 2 arg(s)): sub
      Subtracts &arg2 from &arg1 and stores the result in %4.
  
  Multiply (OPCode 9, 2 arg(s)): mult
      Multiplies &arg1 and &arg and stores the result in %4.
  
  Increment (OPCode 10, 1 arg(s)): inc
      Increments &arg1 by 1 and stores the result in %arg1.
  
  Decrement (OPCode 11, 1 arg(s)): dec
      Decrements &arg1 by 1 and stores the result in %arg1.
  
  Divide (OPCode 12, 2 arg(s)): div
      Divides &arg1 by &arg2 with 8 digits of accuracy and stores the result in %4
  
  Move (OPCode 13, 2 arg(s)): mov
      Writes value of #arg1 to &arg2.
  
  Halt (OPCode 14, 0 arg(s)):
      Completely stops the program and resets the program pointer.

```


