class Solution {
    public int maxPoints(int[][] points) {
        if (points.length == 1) return 1;
        int ans = 0;
        for (int[] origin : points) {
            Map<Double, Integer> freq = new HashMap<>();
            for (int[] point : points) {
                if (Arrays.equals(origin, point)) continue;
                double angle = Math.atan2(point[1] - origin[1], point[0] - origin[0]);
                freq.merge(angle, 1, Integer::sum);
            }
            ans = Math.max(ans, 1 + Collections.max(freq.values()));
        }
        return ans;
    }
}