from aes import AES, bytes2matrix
import os

def main():
    iv = os.urandom(16)
    master_key = os.urandom(16)
    aes_tool = AES(master_key)

    # Test encryption / decryption
    cipher_text = aes_tool.encrypt_block(b'aaaaaaaaaaaaaaaa')
    plain_text = aes_tool.decrypt_block(cipher_text)
    assert plain_text == b'aaaaaaaaaaaaaaaa'

    # Expand key
    all_keys = AES._expand_key(aes_tool, master_key)
    print(str(all_keys) + "\n")                     # Affiche toutes les clés
    k10 = all_keys[-1]                              # On récupère la dernière clé (k10)
    print("k10 : " + str(k10))                      # On l'affiche
    print("type k10 : " + str(type(k10)))           # On affiche son type
    print("k10 passe du type 'list of bytes' à 'bytes'")
    k10 = b''.join(k10)                             # On passe k10 en bytes
    print("k10 : " + str(k10))                      # On affiche le nouveau k10
    print("type k10 : " + str(type(k10)) + "\n")    # On affiche son type pour vérifier qu'il est bien passé en bytes

    
    print("Master Key : " + str(master_key))
    print("type master key" + str(type(master_key)) + "\n")

    # Reverse expand key
    i = 10
    for round_key in AES.inverse_expand_key(aes_tool, k10):
        print ("Round " + str(i) + " : " + str(round_key) + "\n")
        i-=1  
    print("First Key : " + str(round_key)) 
    round_key=bytes2matrix(round_key)
    print(round_key)  

    print("Master Key : " + str(master_key))
    master_key=bytes2matrix(master_key)
    print(master_key)



if __name__ == "__main__":
    main()
