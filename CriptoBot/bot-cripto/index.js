//Par de moedo BTCBUSD
//buscando padrões nos valores mais altos: no intervalo de 3 hs o bitcoin bateu 4 vezes no valor de 36291
//buscando padrões nos valores mais baixos: no intervalo de 3 hs o bitcoin bateu 5 vezes no valor de 35764

//criando uma função chamada process para colocar tudo dentro dela e ficar mais organizado, por ter uma chamada assincrona (utilizando await) dentro da função, foi add a palavra async antes da declaração da função
async function process(){
    //carregando o axios (utilizado para carregar dados de APIs) em uma variável p/ pode fazer as chamada para a API da BINANCE
    const axios = require("axios");

    //criando uma variavel para utilizar o get do axios para solicitar dados p/ a API e armazenar o resultado
    //como é uma chamada que pode demorar ela é assincrona e por isso deve ter o await p/ que a execução só continue após receber os dados, ou seja, o sistema fica esperando. TB DEVE SER ADD async na frente para declaração da função
    const response = await axios.get("https://api.binance.com/api/v3/klines?symbol=BTCBUSD&interval=1m");//o get é p/ pegar dados dos ultimso 500 candles (mini, max, time) no BTCBUSD no intervalo de 1m

    // após testar e receber as ultimas 500 posições, agora irei criar uma variavel para pegar somente a posição 499 que é esatamente a ultima posição, para simular uma captura em tempo real da ultima posição
    const candle = response.data[499];
    
    //console.log(response.data);
    console.log(candle);
}

process();