if('serviceWorker' in navigator){
    window.addEventListener('load', () =>{
    navigator.serviceWorker
        .register('sw.js')
        .then(reg => console.log("GOOD!"))
        .catch(err => console.log(`bad: error: ${err}`))

    })
}