from infosec.core import assemble

def pathch_data_in_loc(program: list, loc: int, patch: bytes):
    """given a program as bytelist, patching the program with a patch in the given loc"""
    # offset from the starting of the program to patch the jump up to the big dead zone. 
    i= loc 
    # patching the program byte by byte
    for b in patch:
        program[i]=b
        i+=1 
        
def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    execute lines starting with #!, and print all other lines as-is.

    Use the `assemble` module to translate assembly to bytes. For help, in the
    command line run:

        ipython3 -c 'from infosec.core import assemble; help(assemble)'

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    #converting the program to a list so we can change the content 
    program2=list(program)
    #assemble bytes program from the assembly code
    patch1 = assemble.assemble_file("./patch1.asm")
    patch2 = assemble.assemble_file("./patch2.asm")
    # patch the jump up to the big dead zone. 
    pathch_data_in_loc(program2, 0x0634, patch1)
    #patch the jump down to skip the change we gonne make in the big dead zone, so the program will start as usual 
    jump_inst=assemble.assemble_data("jmp 0x63")
    pathch_data_in_loc(program2, 0x05CD, jump_inst)
    # here were gonna patch our code, which we wrote in patch2.asm. this is the code that goes in the bid dead zone
    pathch_data_in_loc(program2, 0x5D5, patch2)
    #converting the patched program back to bytes
    return bytes(program2)
    
def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)
    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)

def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <readfile-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
