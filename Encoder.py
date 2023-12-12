import regex, os
os.system("cls")

Instructions = [line.strip() for line in open("Code.txt","r").readlines() if not line.strip() == ""]

def Decode(Code):
    PMem = []
    PArgs = []
    PMap = {"read": 1,"allc": 2,"set": 3,"jmp": 4,"rst": 5,"jne": 6,"add": 7,"sub": 8,"mult": 9,"inc": 10,"dec": 11,"div": 12,"mov": 13,"hlt": 14}

    for line in Code:
        # Get the operation
        OP = line.split(" ")[0].lower()

        if OP == ";" : continue # Error Handling

        if (OP == "jmp" and "neq" in line): OP = "jne"

        # Get the arguments
        Args = [int(i.group()) for i in regex.finditer("(?<!;.*)[0-9]+", line)]

        # Re-arrange the arguments & Edge Cases
        if OP == "jne" or OP == "mov" or OP == "sub": Args.append(Args.pop(0))
        if OP == "hlt" or OP == "rst": Args = [1]

        PMem.append(PMap[OP])

        # append the arguments to the full program arguments
        PArgs.extend(Args + [0] * (3-len(Args)))


    return (PMem, PArgs)

Encoded = Decode(Instructions)
print("\n>> COPY <<")
print("Program Memory: ",Encoded[0])
print("Program Args: ",Encoded[1])
print(">> COPY <<")
