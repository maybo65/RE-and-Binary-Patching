
#  Reverse Engineering (RE) and Binary Patching

As part of my B.Sc. at Tau (Tel Aviv University) I have chosen to take an intro to cyber and cyber security class.

# My first encounter with RE.

Of course, as part of this class i had to study and under how to RE and manipulate binary files and executables.

My first exercise was a validation program that checks if some message X is valid.

![](https://miro.medium.com/max/1400/1*Y0v3wHvYeT4xVjzJYO3KRw.png)

## Part A.

reverse engineer the msgcheck program to understand which messages it considers valid and which messages it considers invalid.

Using gdb and some time I understood how the msgcheck program validates messages.

![](https://miro.medium.com/max/1012/1*35xQQFnylZwJZnF08To7mA.png)

`Validate function inside msgcheck
`

So, the msgcheck goes and reads the first byte (The first character) of our message and creates a loop that goes of that length. (let's call this our Len var)

It also reads the second byte or our message and puts it aside (let's call this our Validation Var [I’m foreshadowing]).

Inside the loop the validate functions xors each byte (character) of our msg with the first xor key (0x8c) e.g. for the msg Example it will xor 0x8c with ‘E’ then the product of this xor it will xor with ‘x’ and so forth. Eventually it will store the xor product inside al register.

It will compare al with the second bype (Validation Var) if those are the same so our validation function will return that the message is valid.

## Creating the Validate function in python

To check that I understood what going on inside msgcheck i had to create a python strict that does the same validation to our msgcheck.

![](https://miro.medium.com/max/1400/1*WvDAn-X_mlDeCbqIA_XfMg.png)

I will explain one thing before moving on, At line 18 I’m checking if the length is greater than 127. Why that? Well out msgcheck program uses a signed char. meaning it can only have the biggest positive value of 127 (01111111) as the last bit indicates if it's a positive or negative value.

![](https://miro.medium.com/max/1400/0*mVha976Uryq3bGGX.png)

With that I’m all done with Part A.

StackEdit stores your files in your browser, which means all your files are automatically saved locally and are accessible **offline!**

## 
## Part B

Fixing messages that return invalid status.

I chose to change the Validation Var (second character of our message). This went smoothly because I already know what xor product each message return i just need to change the second character to the same value.

![](https://miro.medium.com/max/1400/1*sJKMYHos8qlPOW9fpIAaDA.png)

# Part C

Fixing messages that return invalid status. Yet again.

This time I just changed the first byte (Len var) to 0. that makes the xor product of our message to be exactly what is expected.

## Part D

This time I need to patch the program to validate each msg.

To do that I’m going to change that the validate function return as we saw earlier it compares the exprected xor product with the acctual xor project. and return the value to the main program.

![](https://miro.medium.com/max/830/1*F-1JfjPZEOMjP7_QBqMJsw.png)

Return value to the main program.

I’m going to change this instruction to always return 1.

![](https://miro.medium.com/max/974/1*fB1uwzLfFQq8RCNb3uHIdg.png)

Patched validate.

the mov al,0x1 takes only 2 bytes, so i had to add a nop instruction there to keep everything in its right address

![](https://miro.medium.com/max/1400/1*NSJpjMFGrsU2ltFJWVZNLw.png)

Part E

This time I need to patch the program but this time we patch the return value to return 0 no matter what.

I simply changed mov eax, 1 in 0x6DD.  
This instruction sets the return value of the main function to 1 in the invalid branch.  
I changed the immediate from 1 to 0.  
this case even if the message is invalid,  
the return value the main function is still going to be 0 (like it was valid).

![](https://miro.medium.com/max/710/1*q3dI9mNBrqEOe1UkFXnyyA.png)

Original Main

![](https://miro.medium.com/max/702/1*0gr6LKAmj5wnRAI09WmPJQ.png)

patched Main

# Is there another question?!

Well, there is another question!

This time i got a text file with a few files and a program named readfile

I needed to patch the program that it will execute a line that start with #!

![](https://miro.medium.com/max/1072/1*SMfBcOn6EqUDUOj7_PV2uQ.png)

Not patched

![](https://miro.medium.com/max/1400/1*egwZLMOYDndfHdLKXoPkyg.png)

Patched.

## Reverse engineering the readfile program.

Reverse engineering got me two obvious dead zones in the code (dead zones are places in the code that are not utilized by the code or that are not important.) — I’m going to inject my malicious code inside those dead zones.

I had 1 huge Nop slide in my code and one small. I’m going to use the small one to jump into the big Nop slide that executes my code there.

Let's say that the address of the Big Nop slide was 0x100, and the address of the Small one was 0x400.

![](https://miro.medium.com/max/782/1*L4YMDXZ3dSNRFvl7tk-0mA.png)

Big Nop — nothing will execute after rep (like return)

I have noticed that the code always goes to the small Nop slide so I will use it to jump into the big Nop Slide and do my evil stuff over there.

![](https://miro.medium.com/max/1360/1*9aA6A64g4BVFmTMnwB4vaw.png)

Flow.

> in the small Nop, there is a jump instruction. this takes us to the big Nop,  
> right before the program in going to the printing area.  
> lastly, in Big Nop there is a code that checks if the line is starting with “#!”.  
> this happening by reading the first word to EAX, and then check in al=’#’ and if ah=’!’.  
> If not, we are going to jump back right before the print function, and print the line. this is handled by the “back” section.  
> If yes, we are going to execute the line. the address of the first byte of the line in stored in EAX. we are adding 2 to eax (in order to ignore the #!),  
> and the pushing this address and calling system to execute the line. After that, we are going to go back to the regular program,  
> right after the printing (because we don't want to print the line as instructed).

![](https://miro.medium.com/max/972/1*5xUYxQg9fFkrSSH4pOEHzQ.png)

Explaining AL, AH register compares

And that it!

# A quick disclaimer and a tip

This article is written in a hindsight meaning I have already solved it and i can show the solution. BUT! When I was solving it, it took lots of effort and understanding the code and the meaning behind it.

Nothing is accomplished that easily but it was fun to solve it and get better at the tools and in the assembly language.

## A small tip.

In the second question i had to jump from one piece of code to another but sometimes my code won't jump to the right place. After hours of scratching my head i found a solution! If you try to just +0x100 instruction forward from 0x50 and you land at different address (not 0x150) for example 0x139 add 0x11 to your initial jump i.e. 0x111.
