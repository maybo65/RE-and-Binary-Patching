def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    return 0 for all input files.

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    #converting the program to a list so we can change the content 
    x=list(program)
    #movzx to al
    x[0x59a]=0xb0
    #immediate is gonna be one. 
    x[0x59b]=0x01
    #adding a nop becuase we only need 3 bytes to the mov, instead of the 3 bytes there were there.
    x[0x59c]=0x90
    # over all we get from the above: movzx al, 1
    #converting the patched program back to bytes
    return bytes(x)
    
    
        


def patch_program(path):
    with open(path, 'rb') as reader:
        data = reader.read()
    patched = patch_program_data(data)
    with open(path + '.patched', 'wb') as writer:
        writer.write(patched)


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msgcheck-program>'.format(argv[0]))
        return -1
    path = argv[1]
    patch_program(path)
    print('done')


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
