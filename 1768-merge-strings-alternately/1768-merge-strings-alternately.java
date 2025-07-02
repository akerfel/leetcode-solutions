class Solution {
    public String mergeAlternately(String word1, String word2) {
        int n = word1.length() + word2.length();
        char[] res = new char[n];

        int i = 0;
        int j = 0;
        int k = 0;
        while (i < word1.length() && j < word2.length()) {
            res[k] = word1.charAt(i);
            res[k+1] = word2.charAt(j);
            i++;
            j++;
            k += 2;
        }
        while (i < word1.length()) {
            res[k] = word1.charAt(i);
            i++;
            k++;
        }
        while (j < word2.length()) {
            res[k] = word2.charAt(j);
            j++;
            k++;
        }
        return new String(res);
    }
}