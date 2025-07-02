class Solution {
    public int subarraySum(int[] nums, int k) {
        int n = nums.length;
        Map<Integer, Integer> sums = new HashMap<>(); // count of each sum
        int res = 0;
        int currentSum = 0;
        sums.put(0, 1);
        for (int i = 0; i < nums.length; i++) {
            currentSum += nums[i];
            res += sums.getOrDefault(currentSum - k, 0);
            sums.merge(currentSum, 1, Integer::sum);
        }
        return res;
    }
}