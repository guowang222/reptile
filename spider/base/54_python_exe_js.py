# pip install PyExecJS


js = '''
function add(num1,num2){
    return num1+num2;
}
function show(){
    return "hello python2js"
}
'''
def func1():
    import execjs
    ctx = execjs.compile(js)
    rs = ctx.call('add',1,2)
    print(rs)

    print(ctx.call('show'))

def func2():
    import js2py
    context = js2py.EvalJs()
    context.execute(js)
    # result = context.add(1, 2)
    result = context.show()
    print(result)


if __name__ == '__main__':
    func1()
    func2()