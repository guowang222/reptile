def test_node1():
    import os
    a = 1
    b = 2
    cmd_line = f'node ./62_js.js {a} {b}'
    with os.popen(cmd_line) as nodejs:
        rs = nodejs.read().replace('\n','')
        print(rs)

def test_node2():
    import subprocess
    a = 1
    b = 2
    cmd_line =f'node ./62_js.js {a} {b}'
    p = subprocess.Popen(cmd_line.split(),stdout = subprocess.PIPE)
    rs = p.stdout.read().decode().replace('\n','')
    print(rs)
if __name__ =='__main__':
    # test_node1()
    test_node2()