import java.util.*;

class Solution {
    boolean isValid(char c) {
        if (Character.isLetterOrDigit(c)) return true;
        if (c == '-' || c == '_' || c == '.') return true;
        
        return false;
    }
    
    public String solution(String new_id) {
        StringBuilder answer = new StringBuilder();
        
        boolean lastDot = false;
        for (char c : new_id.toCharArray()) {
            if (!isValid(c)) continue;
            if (c == '.') {
                // 처음 및 연속된 '.' skip
                if (answer.length() == 0 || lastDot) continue;
                lastDot = true;
            } else {
                lastDot = false;
            }
            
            c = Character.toLowerCase(c);
            answer.append(c);
        }
        
        // 16자 이상일 경우 15개로 고정
        if (answer.length() >= 16)
            answer.setLength(15);
        
        // 빈 문자열일 경우 'a' 추가
        if (answer.length() == 0)
            answer.append('a');
        
        // 마지막 '.' 제거
        if (answer.charAt(answer.length() - 1) == '.')
            answer.deleteCharAt(answer.length() - 1);
        
        // 길이가 2 이하라면 길이 3까지 마지막 문자 추가
        if (answer.length() <= 2) {
            char c = answer.charAt(answer.length() - 1);
            while (answer.length() < 3)
                answer.append(c);                
        }
        
        return answer.toString();
    }
}