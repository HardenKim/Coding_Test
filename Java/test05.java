class Solution {
    int convert(String time) {
        String[] nums = time.split(":");
        return Integer.parseInt(nums[0]) * 60 * 60 +
            Integer.parseInt(nums[1]) * 60 +
            Integer.parseInt(nums[2]);
    }
    
    public String solution(String play_time, String adv_time, String[] logs) {
        int playSec = convert(play_time);
        int advSec = convert(adv_time);
        // 초당 시청 인원
        int[] totalSec = new int[100*3600];
        for (String log : logs) {
            int start = convert(log.substring(0,8));
            int end = convert(log.substring(9));
            
            for (int i=start; i<end; i++) {
                totalSec[i]++;
            }
        }
        
        // play_time, adv_time 최대 100시간 = 100*60*60
        // logs (시청자) 최대 300,000
        // adv_time 구간 동안 최대 누적 시청자 = 100*60*60 * 300000
        // int 범위 벗어나므로 long 사용
        long currSum = 0;
        // 0초부터 광고 시간까지의 누적 시청 인원
        for (int i=0; i<advSec; i++) {
            currSum += totalSec[i];
        }
        
        long maxSum = currSum;
        int maxIdx = 0;
        // 1초씩 오른쪽으로 이동하면서 누적 시청 인원 기록
        for (int i=advSec; i<playSec; i++) {
            currSum = currSum + totalSec[i] - totalSec[i-advSec];
            if (currSum > maxSum) {
                maxSum = currSum;
                maxIdx = i - advSec + 1;
            }
        }
        
        return String.format("%02d:%02d:%02d", 
                             maxIdx/3600, (maxIdx/60)%60, maxIdx%60);
    }
}