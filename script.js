return {
    'Price': Array.prototype.slice.call(document.getElementsByClassName('wl9 w7l')).map(x => x.innerText),
    'Name': Array.prototype.slice.call(document.getElementsByClassName('yl tsHeadline550Medium')).map(x => x.innerText),
    'Type': Array.prototype.slice.call(document.getElementsByClassName('kn6')).map(x => x.innerText)
};

