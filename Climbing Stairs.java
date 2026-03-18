class Solution {
    public int climbStairs(int n) {
       if(n == 1){
        return 1;
       } 
       if (n == 2){
        return 2;
       }
       int p2 = 1;
       int p1 = 2;
       int current = 0;

       for (int i = 3; i <= n; i++){
            current = p2 + p1;
            p2 = p1;
            p1 = current;
       }
       return p1;
    }
}
