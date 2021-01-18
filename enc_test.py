from aes import AES
import os

def main():
    iv = os.urandom(16)
    master_key = os.urandom(16)

    aes_tool = AES(master_key)

    cipher_text = aes_tool.encrypt_cbc(b'test', iv)
    plain_text = aes_tool.decrypt_cbc(cipher_text, iv)

    assert plain_text == b'test'

if __name__ == "__main__":
    main()
