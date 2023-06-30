function solution(new_id) {
    let c1 = new_id.toLowerCase()
    const sp = /[\{\}\[\]\/?,;:|\)*~`!^\+<>@\#$%&\\\=\(\'\"]/gi
    let c2 = c1.replace(sp,'')
    let len = c2.length
    const reg = /./gi
    let c3 = c2.split('')
    
    for ( let i = 0 ; i < len - 1 ; i ++){
        console.log(c3.at(i) + c3.at(i+1))
        if ( c3.at(i) === c3.at(i+1) && c3.at(i) === '.') c3[i] = ''
    
    }
    let reset = c3.join('')
    let c4 = reset.split('')
    
    if ( c4[0] ==='.' ){
        console.log("shifted");
        c4.shift();
    }
    if ( c4.at(-1) === '.') {
        console.log("poped");
        c4.pop();
    }
    
    if (c4.length === 0) {
        c4.push('a');
    }
    console.log(c4)
    let c5 = c4.join('').slice(0,15).split('')
    console.log(c5)
    
    if ( c5[0] ==='.' ){
        console.log("shifted");
        c5.shift();
    }
    if ( c5.at(-1) === '.') {
        console.log("poped");
        c5.pop();
    }
    if (c5.length <= 2) {
        console.log('in')
        let howmany = c5.length
        let won = c5.at(-1)
        for ( let i = howmany; i < 3; i ++){
            c5.push(won);
        }
        console.log(c5)
        
    }
    return c5.join('')
}