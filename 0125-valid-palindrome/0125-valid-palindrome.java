class Solution {
    public boolean isPalindrome(String s) {
        s = cleanString(s);
        int L = 0;
        int R = s.length() - 1;
        while (L < s.length() / 2) {
            char cL = Character.toLowerCase(s.charAt(L));
            char cR = Character.toLowerCase(s.charAt(R));
            if (cL != cR) {
                return false;
            }
            L++;
            R--;
        }
        return true;
    }

    public static String cleanString(String input) {
        StringBuilder result = new StringBuilder();

        for (char c : input.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                result.append(Character.toLowerCase(c));
            }
        }

        return result.toString();
    }
}