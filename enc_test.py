from aes import AES
import os

def main():
    iv = os.urandom(16)
    master_key = os.urandom(16)
    aes_tool = AES(master_key)

    # Test encryption / decryption
    cipher_text = aes_tool.encrypt_block(b'aaaaaaaaaaaaaaaa')
    plain_text = aes_tool.decrypt_block(cipher_text)
    assert plain_text == b'aaaaaaaaaaaaaaaa'

    # Reverse expand key
    print("Master Key : " + str(master_key) + "\n")

    i = 10
    for round_key in AES.inverse_expand_key(aes_tool, master_key):
        print ("Round " + str(i) + str(round_key) + "\n")
        i-=1    

    # Expand key
    AES._expand_key(aes_tool, master_key)


if __name__ == "__main__":
    main()
