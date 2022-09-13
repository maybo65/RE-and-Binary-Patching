def check_message(path: str) -> bool:
    """
    Return True if `msgcheck` would return 0 for the file at the specified path,
    return False otherwise.
    :param path: The file path.
    :return: True or False.
    """
    with open(path, 'rb') as reader:
        bytes = list(reader.read())
        #if the len of the message is one, then its for sure not valid. 
        if len(bytes)<=1:
            return False
        # if the len is two, the message is valid iff the second byte is 0x8c (because we actully xoring 0x8c with nothing)
        if len(bytes)==2:
            if(bytes[1]==0x8c):
                return True
            return False
        
        # the first bytes is indcating the number of bytes were gonna check (excluding the first two bytes), but this cannot exceed the len of the message itself. 
        length = min(len(bytes),bytes[0]+2)
        ##if the size indicator is greater then 127, then we are also going to zero iteration, because there is underflow (the original program uses singed char to hold this size).
        if (len(bytes)>127):
            length=0
        expected_xor = bytes[1]
        res = 0x8c
        #here were xoring each byte in the message (in the given length above), and xoring this whith 0x8c 
        for i in range(2, length):
            res = res ^ bytes[i]
        #checking if the result we got is equal to the second byte in the message, as expected. the message is valid iff it is the case. 
        if(res== expected_xor):
            return True
        return False


def main(argv):
    if len(argv) != 2:
        print('USAGE: python {} <msg-file>'.format(argv[0]))
        return -1
    path = argv[1]
    if check_message(path):
        print('valid message')
        return 0
    else:
        print('invalid message')
        return 1


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))

