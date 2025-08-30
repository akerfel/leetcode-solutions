class Solution {
    public int strStr(String haystack, String needle) {
        char[] hay = haystack.toCharArray();
        char[] need = needle.toCharArray();

        for (int i = 0; i < hay.length; i++) {
            if (hay[i] == need[0]) {
                int potential = i;
                int j = 0;
                while (hay[i] == need[j]) {
                    i++;
                    j++;
                    if (j > need.length - 1) {
                        return potential;
                    }
                    if (i > hay.length - 1) {
                        return -1;
                    }
                }
                i = potential;
            }
        }
        return -1;
    }
}