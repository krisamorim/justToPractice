//função para receber hora e minuto
function angulo(hr, mnt){
    if(hr == 12){
        hr = 0
    }

    let anguloDahr = hr * 30 + (mnt/60)*30
    let anguloDomnt = mnt * 6

    let angulo
    if(anguloDahr > anguloDomnt){
        angulo = anguloDahr - anguloDomnt
    }else{
        angulo = anguloDomnt - anguloDahr
    }

    return angulo
}

console.log(angulo(3,30))
