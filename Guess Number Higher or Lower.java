/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution extends GuessGame {
    public int guessNumber(int n) {
        int left = 1;
        int right = n;

        while (left <= right){
            int mid_num = left + (right - left) / 2;// this is to prevent integer overflow
            int result = guess(mid_num);

            if (result == 0){
                return mid_num;
            }
            else if (result == -1){
                right = mid_num - 1;
            }
            else {
                left = mid_num + 1;
            }
        }
        return -1;
    }  
}
