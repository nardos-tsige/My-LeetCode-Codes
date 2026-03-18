/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    // Keep looping until we have a single digit
    while (num >= 10) {
        let total = 0;
        let numStr = num.toString();
        for (let i = 0; i < numStr.length; i++) {
            total += parseInt(numStr[i]);
        }
        num = total;
    }
    return num;
};
