class Solution {
    public int solution(String s) {
        int answer = s.length();
        
        // 문자열 단위는 (1 ~ length/2)
        for (int i=1; i<=s.length()/2; i++) {
            int pos = 0;
            int len = s.length();
            // 문자열이 반복되는 unit의 길이는 i+1  
            for ( ; pos+i <= s.length() ; ) {
                String unit = s.substring(pos, pos+i);
                pos += i;
                
                int cnt = 0;    // 문자 하나는 표시되어야하므로 중복부터 카운트
                // 문자열이 몇번 반복되는지 카운트
                for ( ; pos+i <= s.length() ; ) {
                    if (unit.equals(s.substring(pos, pos+i))) {
                        cnt++;
                        pos += i;
                    } else {
                        break;
                    }
                }
                // 반복된 횟수를 길이에 반영
                if (cnt > 0) {
                    len -= i * cnt;
                    
                    if (cnt < 9) len += 1;
                    else if (cnt < 99) len += 2;
                    else if (cnt < 999) len += 3;
                    else len += 4;
                }
            }
            answer = Math.min(answer, len);
        }
        
        return answer;
    }
}