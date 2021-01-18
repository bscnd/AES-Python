from aes import AES
import os

def main():
    iv = os.urandom(16)
    master_key = os.urandom(16)

    aes_tool = AES(master_key)

    cipher_text = aes_tool.encrypt_block(b'aaaaaaaaaaaaaaaa')
    plain_text = aes_tool.decrypt_block(cipher_text)

    assert plain_text == b'aaaaaaaaaaaaaaaa'

if __name__ == "__main__":
    main()
