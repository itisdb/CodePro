class Solution {
    public boolean canFormArray(int[] arr, int[][] pieces) {
        Map<Integer, int[]> map = new HashMap<>();
        for (int[] piece : pieces) {
            map.put(piece[0], piece);
        }
        
        //iterate all the elements in arr
        for (int i = 0; i < arr.length; ) {
            int curVal = arr[i];
            if (map.containsKey(curVal)) {
                int[] piece = map.get(curVal);
                for (int value : piece) {
                    if (arr[i] == value) {
                        i++;
                    } else {
                        return false;
                    }
                }
            } else {
                return false;
            }
        }
        return true;
    }
}
