in the patch1.assembly, there is a jump instructions. this takes us to the big dead zone, right before the program in going to the printing erae. 
additionaly,in q2.py there is a jumping instrucion from the start of the dead zone to the end of the deat zone. this way we can patch pur code in the dead zone, but it won't change the start of the program itself. 
lastly, in patch1.assemby there is a code that checks if the line is starting with #!. this happening by reading the first word to EAX, and then check in al=# and if ah=!. 
if not, we are going to jump back right before the print function, and print the line. this is handdled by the "back" section. 
if yes, we are going excecute the line. the adress of the first byte of the line in stored in EAX. we are adding 2 to eax (in order to ingnore the #!), and the pushing this adress and calling system to excute the line. after that, we are going to go back to the regulaer program, right after the printing (becuase we dont want to print the line). 
in q2.py the patch_program_data function will patch the program using the assembly program we write in patch1.asm and patch2.asm and the pathch_data_in_loc function.
we are getting the bytes of the instruction we want to patch using the assemble.assmble_file and assemble.assemble_data, and we are calling to the pathch_data_in_loc with those bytes and the right places of the file. 
