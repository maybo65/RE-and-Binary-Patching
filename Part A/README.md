# q1.a 

first, we are checking if the message is from length of 1. if it is one, then its for sure not valid. we are also checking for two. if the len is two, the message is valid if and only if the second byte is 0x8c (because we actully xoring 0x8c with nothing).
then, we are calculating the number of bytes we are going to check. the first bytes is indcating this number (excluding the first two bytes of the massage), but this cannot exceed the len of the message itself, so this going to be the length (the minimum between the two).
then, we are going to xor each byte of the message (without exceeding the length we just calculated), and this we are going to xor to 0x86.
if the xor result we got is equal to the second byte of the message, the the message is valid. 
