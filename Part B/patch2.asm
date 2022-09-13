push ebx
mov ebx, [eax]
cmp bl, 0x23
jnz back
cmp bh, 0x21
jnz back
push eax
add eax,2
push eax
call -0x175
pop eax
pop eax
pop ebx 
jmp 0x7c
back:
pop ebx
jmp 0x65
