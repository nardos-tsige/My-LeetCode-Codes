/**
 * @param {number} x
 * @return {number}
 */
var reverse = function(x) {
    let rem = 0;
    let ana = Math.abs(x);
    
    while (ana > 0) {
        let s = ana % 10;
        rem = (rem * 10) + s;
        ana = Math.floor(ana / 10);
    }
    
    if (rem >= 2147483648) {
        return 0;
    }
    
    if (x < 0) {
        rem *= -1;
    }
    
    return rem;
};
