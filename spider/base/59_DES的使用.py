from Crypto.Cipher import DES
import base64

class EncryptData():
    def __init__(self,key) -> None:
        self.key = key
        self.length = DES.block_size
        self.des = DES.new(key,DES.MODE_ECB)
    
    def add_8(self,info):
        while len(info) % self.length !=0:
            info += b'\x00'
        return info
    def encrypt(self,data):
        data = self.add_8(data)
        rs = self.des.encrypt(data)
        rs = str(base64.b64encode(rs),encoding='utf-8')
        return rs
    def dencrypt(self,data):
        rs = base64.b64decode(data.encode('utf-8'))
        msg = self.des.decrypt(rs)
        return msg
# data
# key
# encrypt
# dencrypt

if __name__ =='__main__':
    key = b'12345678'
    msg = b'sxt'
    enc = EncryptData(key)
    enc_data = enc.encrypt(msg)
    print(f'加密的数据是：{enc_data}')
    print(f'解密的数据是：{enc.dencrypt(enc_data).decode()}')