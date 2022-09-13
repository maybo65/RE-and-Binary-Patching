
# Extra Docomntaion here...

# q1.a 

first, we are checking if the message is from length of 1. if it is one, then its for sure not valid. we are also checking for two. if the len is two, the message is valid if and only if the second byte is 0x8c (because we actully xoring 0x8c with nothing).
then, we are calculating the number of bytes we are going to check. the first bytes is indcating this number (excluding the first two bytes of the massage), but this cannot exceed the len of the message itself, so this going to be the length (the minimum between the two).
then, we are going to xor each byte of the message (without exceeding the length we just calculated), and this we are going to xor to 0x86.
if the xor result we got is equal to the second byte of the message, the the message is valid. 

# q1.b
if the length of the message is less or equal to two, this is a special edge case. to order to fix this, we are going just to makesure the length of the message is two, and the second byte is equal to 0x8c.
assuming this is not the case, we are going to calclate the excpected xor result of the message (just like the message check does). if the second byte of the message is not equal to the expected xor result we just calculated, we'll just gonna change this byte. this way the message is going to be valid forsure.  


 # q1.c 
 if the length of the message isequal to one, this is a special edge case. to order to fix this, we are going just to makesure the length of the message is two, and the second byte is equal to 0x8c (any message of size one is invalid, so this is fix we have to do).
assuming this is not the case, we are going to put zero in the first byte of the message, and 0x8c in the second byte. 
if the first byte is zero- the program will xor nothing to 0x8c, and the will make sure this "xor result" is equal to the second byte, and will return 1 iff this is the case. so, our program is making sure this is the case, by putting 0x8c in the second byte and zero in the first byte.

# q1.d
in order to making sure the patched program will always return 1, we are simply going to replace the "movzx eax, al" instruction in 0x59a address with movxz eax, 1 instrtuction, and a nop (the nop is only there becuse we replace a 3 bytes instrction with a 2 bytes instruction).
the idea behind this is that the movzx eax, al instruction sets al to be 1 iff the message i valid (because of the cmp and setx instructions before). so, by changing this instruction to the new one, we are making sure the message is alwayes valid, no matter what is the cmp result.

# q1.e
here, we are simply changing the mov eax, 1 in 0x6DD. this instrunction sets the retrun value of the main function to 1 in the invalid branch. we are changing the immediate from 1 to 0. this case even if the message is invalid, the return value the main function is still going to be 0 (like it was valid). 
