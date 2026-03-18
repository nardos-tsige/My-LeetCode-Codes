class Solution {
    public int addDigits(int num) {
        while (num >= 10){
            int total = 0;
            String numStr = Integer.toString(num);
            for (int i = 0; i < numStr.length(); i++){
                total += numStr.charAt(i) - '0';
            }
            num = total;
        }
        return num;
    }
}
