class Solution {
    public String longestCommonPrefix(String[] strs) {
        String prefix = strs[0];
        for (int i = 1; i < strs.length; i++) {
            String s = strs[i];
            if (!s.startsWith(prefix)) {
                int j = 0;
                while (j < prefix.length() && j < s.length() && prefix.charAt(j) == s.charAt(j)) {
                    j++;
                }
                prefix = prefix.substring(0, j);
            }
        }
        return prefix;
    }
}