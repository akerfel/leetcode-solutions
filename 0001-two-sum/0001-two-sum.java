import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> valueToIndex = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int current = nums[i];
            int needed = target - current;
            if (valueToIndex.containsKey(needed)) {
                return new int[]{i, valueToIndex.get(needed)};
            }
            valueToIndex.put(current, i);
        }
        return new int[]{0, 0};
    }
}