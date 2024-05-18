var debounce = function(fn, t) {
    let timer;

    return function(...args) {
        clearTimeout(timer)
        timer = setTimeout(() => fn.apply(this, args), t);
    }
};

/*
const log = debounce(console.log, 100);

log('foo 1');
log('foo 2');
log('foo 3');
*/
