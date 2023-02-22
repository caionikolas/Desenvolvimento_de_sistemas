var capitalizeTitle = function(title) {
    let words = title.split(' ')
    for(let i = 0; i < words.length; i++){
        if (words[i].length < 3){
            words[i] = words[i].toLowerCase()
        } else{
            words[i] = words[i].toLowerCase()
            let word = words[i]
            word = word.split('')
            word[0] = word[0].toUpperCase()
            word = word.join('')
            words[i] = word
        }
    }
    words = words.join(' ')
    return words
};

console.log(capitalizeTitle("First leTTeR of EACH Word"))