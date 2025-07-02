class Solution {
    public int characterReplacement(String s, int k) {
        int[] count = new int[26];
        int L = 0;
        int res = 0;
        for (int R = 0; R < s.length(); R++) {
            count[toInt(s.charAt(R))]++;
            while (getMaxValue(count) + k <= R - L) {
                int charAsInt = toInt(s.charAt(L)); 
                count[charAsInt] = Math.max(0, count[charAsInt] - 1);
                L++;
            }
            res = Math.max(res, R - L + 1);
        }
        return res;
    }

    private int getMaxValue(int[] count) {
        int max = 0;
        for (int i = 0; i < count.length; i++) {
            max = Math.max(max, count[i]);
        }
        return max;
    }

    int toInt(char c) {
        return c - 'A';
    }
}