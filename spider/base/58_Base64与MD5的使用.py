def test_base64():
    import base64
    msg = 'sxt'
    rs = base64.b32encode(msg.encode())
    print(rs)
    rs2 =  base64.b32decode(rs)
    print(rs2)


def test_md51():
    import hashlib
    m = hashlib.md5()
    m.update('sxt'.encode())
    pwd = m.hexdigest()
    print(pwd)

def test_md52():
    import hashlib
    pwd = hashlib.new('md5',b'sxt').hexdigest()
    print(pwd)
    
if __name__ == "__main__":
    # test_base64()
    test_md51()
    test_md52()