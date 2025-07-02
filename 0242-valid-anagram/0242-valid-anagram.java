import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character, Integer> count1 = new HashMap<>();
        for (char c : s.toCharArray()) {
            if (count1.containsKey(c)) {
                count1.merge(c, 1, Integer::sum);
            }
            else {
                count1.put(c, 1);
            }
        }
        Map<Character, Integer> count2 = new HashMap<>();
        for (char c : t.toCharArray()) {
            if (count2.containsKey(c)) {
                count2.merge(c, 1, Integer::sum);
            }
            else {
                count2.put(c, 1);
            }
        }
        return count1.equals(count2);
    }
}