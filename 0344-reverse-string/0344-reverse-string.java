class Solution {
    public void reverseString(char[] s) {
        int L = 0;
        int R = s.length - 1;

        while (L < s.length / 2) {
            char temp = s[L];
            s[L] = s[R];
            s[R] = temp;
            L++;
            R--;
        }
    }
}