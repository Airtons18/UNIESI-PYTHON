function vez() {
    var vezde = document.getElementById('xy')
    if (vezde == 'x') {
        var vez = pos
        pos = 'o'
    } else {
        vez = pos
        pos = 'x'
    }
    return (pos); 
}

function pos() {
    var resultado = vez()
    var posi = document.getElementById('po');
    if (posi == '11') {
        var b11 = document.getElementById('11').value == resultado;
    }
    if (posi == '12') {
        var b12 = document.getElementById('12').value == resultado;
    }
}

console.log(posi);