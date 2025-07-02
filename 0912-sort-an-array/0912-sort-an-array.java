class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length - 1);
        return nums;
    }

    // sorts elements between index l and r
    private void mergeSort(int[] nums, int l, int r) {
        if (l >= r) { // since we are sorting between l and r, this means we only need to sort one
            return;   // element. But one element by itself is always sorted, thus we return.
        }
        int m = (l + r) / 2;
        mergeSort(nums, l, m);
        mergeSort(nums, m + 1, r);
        merge(nums, l, m, r);
    }

    private void merge(int[] nums, int l, int m, int r) {
        List<Integer> merged = new ArrayList<>();

        int i = l;
        int j = m + 1;
        while (i <= m && j <= r) {
            if (nums[i] <= nums[j]) {
                merged.add(nums[i]);
                i++;
            } else {
                merged.add(nums[j]);
                j++;
            }
        }

        while (i <= m) {
            merged.add(nums[i]);
            i++;
        }
        
        while (j <= r) {
            merged.add(nums[j]);
            j++;
        }

        for (i = 0; i < merged.size(); i++) {
            nums[l + i] = merged.get(i);
        }
    }
}