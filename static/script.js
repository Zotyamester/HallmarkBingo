function tick(item) {
    console.log(item.style.backgroundColor);
    if (item.style.backgroundColor == 'rgb(69, 137, 67)' || item.style.backgroundColor == '') {
        console.log('asd');
        item.style.backgroundColor = 'rgb(244, 67, 54)';
    } else {
        console.log('lol');
        item.style.backgroundColor = 'rgb(69, 137, 67)';
    }
}
