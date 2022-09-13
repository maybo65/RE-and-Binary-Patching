def patch_program_data(program: bytes) -> bytes:
    """
    Implement this function to return the patched program. This program should
    return 0 for all input files.

    The fix in this file should be *different* than the fix in q1d.py.

    :param data: The bytes of the source program.
    :return: The bytes of the patched program.
    """
    #converting the program to a list so we can change the content 
    x=list(program)
    # patcing the progeram in the right place with 0 immediate instead of 1.
    x[0x6de]=0x0
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
