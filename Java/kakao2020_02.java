import java.util.*;
class Solution {
    int pos;
    
    boolean isCorrect(String str) {
        // 옳바른 괄호 문자열인지 확인
        boolean ret = true;
        int left = 0, right = 0;
        Stack<Character> st = new Stack<Character>();
        
        for (int i=0; i<str.length(); i++) {
            if (str.charAt(i) == '(') {
                left++;
                st.push('(');
            } else {
                right++;
                if (st.isEmpty()) 
                    ret = false;
                else
                    st.pop();
            }
            // 최초로 균형잡힌 괄호 문자열이 되는 곳
            if (left == right) {
                pos = i + 1;    // v가 시작되는 idx
                return ret;
            }
        }
        return true;
    }
    
    public String solution(String p) {
        if (p.isEmpty()) return p;
        
        boolean correct = isCorrect(p);
        String u = p.substring(0,pos);
        String v = p.substring(pos, p.length());
        
        if (correct)
            return u + solution(v);
        
        String answer = "(" + solution(v) + ")";
        for (int i=1; i<u.length()-1; i++) {
            if(u.charAt(i) == '(')
                answer += ')';
            else
                answer += '(';
        }
        
        return answer;
    }
}