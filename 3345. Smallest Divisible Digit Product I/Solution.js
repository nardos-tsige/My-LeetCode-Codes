/**
 * @param {number} n
 * @param {number} t
 * @return {number}
 */
var smallestNumber = function(n, t) {
    function digitProduct(num) {
        let product = 1;
        const str = String(num);
        for (let i = 0; i < str.length; i++) {
            product *= parseInt(str[i]);
        }
        return product;
    }
    
    let current = n;
    while (true) {
        if (digitProduct(current) % t === 0) {
            return current;
        }
        current++;
    }
};
