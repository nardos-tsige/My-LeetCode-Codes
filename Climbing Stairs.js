/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    if (n == 1){
        return 1;
    }
    if (n == 2){
        return 2;
    }
    let p1 = 2
    let p2 = 1
    let current = 0

    for (let i = 3; i <= n; i++){
        current = p1 + p2
        p2 = p1
        p1 = current
    }
    return p1;
};
