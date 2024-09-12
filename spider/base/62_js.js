function add(a,b){
    return a+b
}

tmp_a = parseInt(process.argv[2])
tmp_b = parseInt(process.argv[3])
console.log(add(tmp_a,tmp_b))