/**
 * @param {string} s
 * @return {string}
 */
var reverseWords = function(s) {
    let st = '';
    let sp = s.split(" ");
    for (let i = 0; i < sp.length; i++) {
        sp[i] = sp[i].split('').reverse().join('');
        st += sp[i];
        if (i < sp.length - 1) {
            st += " ";
        }
    }
    return st;
};
