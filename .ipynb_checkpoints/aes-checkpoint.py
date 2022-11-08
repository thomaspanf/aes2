import os
import binascii
key=binascii.hexlify(os.urandom(16))
print ('The Key You Made Was: ', [x for x in key])
print('The Key You Made Was: ', key)