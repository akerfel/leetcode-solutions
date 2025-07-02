class Solution {
    public List<Integer> majorityElement(int[] nums) {
        Arrays.sort(nums);
        List<Integer> res = new ArrayList<>();
        int i = 0;
        while (i < nums.length) {
            int count = 1;
            int j = i + 1;
            while (j < nums.length && nums[i] == nums[j]) {
                j++;
                i++;
                count++;
            }
            if (count > nums.length / 3) {
                res.add(nums[i]);
            }
            i++;
        }
        return res;
    }
}