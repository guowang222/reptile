from  Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64

class EncryptData():
    def encrypt(self,data,pb):
        key = RSA.importKey(pb)
        chipher = PKCS1_v1_5.new(key)
        rs = base64.b64encode(chipher.encrypt(data.encode('utf-8')))
        return rs.decode('utf-8')

    def dencrypt(self,data,pv):
        key = RSA.importKey(pv)
        chipher = PKCS1_v1_5.new(key)
        rs = chipher.decrypt(base64.b64decode(data),0)
        return rs.decode('utf-8')
        
if __name__ =='__main__':
    msg = "{'name':'张三','age':18}"
    public_key = '''-----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAuC4V2kRGDsJVI8ZQF06t
    VmGeTR041zZmbni9Hr+p0zgUzwmqP1fei6GoYey1MOqJnzg+ZObA0kC27DwY0XiN
    AE21hb2fcXU54lGaDrbGXCXk+hSj9NqjDitcXyUh84WRkL+eBtP/dcSYd1KSkUlE
    9KyrzPvMZd+EXImMbXx58QZeIDcz4rWHgcTvOihkEI2RjB+PRTz6nGg7hpxt9iUv
    +gKh8Qrrtk6/4h6TjQePZDYouWZXwRWkcgvaA4+JBRDMV+Y7NsR0qLqWl+MUFpn2
    /p4S1QZW1uwU1U5kciJcwekq5de+PRHZJZaa+2NbDtYocTKkiM/1+WySe5lN8HRm
    VwIDAQAB
    -----END PUBLIC KEY-----
    '''
    private_key ='''-----BEGIN PRIVATE KEY-----
    MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC4LhXaREYOwlUj
    xlAXTq1WYZ5NHTjXNmZueL0ev6nTOBTPCao/V96Loahh7LUw6omfOD5k5sDSQLbs
    PBjReI0ATbWFvZ9xdTniUZoOtsZcJeT6FKP02qMOK1xfJSHzhZGQv54G0/91xJh3
    UpKRSUT0rKvM+8xl34RciYxtfHnxBl4gNzPitYeBxO86KGQQjZGMH49FPPqcaDuG
    nG32JS/6AqHxCuu2Tr/iHpONB49kNii5ZlfBFaRyC9oDj4kFEMxX5js2xHSoupaX
    4xQWmfb+nhLVBlbW7BTVTmRyIlzB6Srl1749Edkllpr7Y1sO1ihxMqSIz/X5bJJ7
    mU3wdGZXAgMBAAECggEAf5dlihyMEANuaecjatIVYOclfDSHQQgts9Au69NJOcr7
    F2aRq2obAM5P0O7jouyHxGZ5SvtUjxNH5aXIZ6zEuXYcD3eKslXMcM2pFRJnnkSe
    OOT9pE2mcdV2G2+k8ogQjJ9CQWax7YrxOJBaew2wGHRaXBn/wn8yucyMHPkDnQVn
    nbJgy1g0cIompQ54rZLgcuT+A3h0HgdCZek2hKUEjn+BuSCMlKY5HniqX0cJT66+
    dTZp46A+GXYSaOWxr2p60wP3cmlQHOb8tcWf+VRZq7DmNCO60LqjxEO63woCWR+A
    hqEmc8S27ARPGlSCQwPKJ6zyCQSbqsR1R1HYdEz3UQKBgQDpk5aIBeqxMigqeJK9
    j7I7LxGKwt/zT2WuM8036wRClGvLZBsYLcoq1pIOxKFQHqVshUI3WfiRPZKwP0hH
    Gm3v/bJDqOuP7hPVrblzTXYWtmKlnJhvtK6J8q6+kkX2soaLugro48JW3n9DL2Fn
    8jDBPALCl6DNzAyg7AfN1RMkWQKBgQDJ3IWGLlUutZyxuX+DvDef+Lw1Ap4IegET
    9NUViws5Gp4SO2OlSiZlSCpflFGPsQ9lK+XtF0Z5uQlsQ23cqyCROdafUBaq4Bu6
    uY49Y1JD5OjtonhRVFCKvTsh+3Z3fQeMY1ZCB00dPYm7wVGmBee5UhiF+G6PQsLu
    AQubQwdKLwKBgQDGfuP36H9P4n37ycd6THl8jj1sHLvQu3J/ngoSMSjHo/YPPJ1B
    6Pfbe8lXv4YO3lxaYsyo2U7Brv/Pw5eaxT0ULBaoJQ86m2pDtoTZFcT6/DfM4c0x
    cOy60n/p98h5I7HvYEURMSzgQekIoWU3vrvsGyGFWPIQsg0xXCQtqZvA0QKBgQCR
    znG8DDeHN7NpRF3w38EmEdqQR8Wyxb2FlrFbkEWZB7rp3HALclXtjoTc6RtIuVIv
    d9fqu4cyYQ+HXeU7IXiyrZ5zELxuzNX6uBEgEl/Xnr8I9vQFeut6a1kNIL/fazZK
    l24032U6G7sjHW5Gh7lrSPthuaLSZBy9IZAqo+3eDQKBgF/+fF/ez/VuvLvFICP/
    sCOfa33c/A2fGYuCU6DR0lNFt5eyJPU+FGgV3Mw2JCEUb0mcWYBNY5XGnp9l6Lx7
    Hokwt90GcqXXMUQnYYLJMHbyI1EyoLgb3vRnt16Q/2nw0OTv9f5JgJnufDm3Rc0S
    BI+JN/7tBIt+3uWZt8zzCfR/
    -----END PRIVATE KEY-----
    '''
    enc = EncryptData()
    rs = enc.encrypt(msg,public_key)
    print(f'加密后的数据是:{rs}')
    rs2 = enc.dencrypt(rs,private_key)
    print(f'解密后的数据是:{rs2}')