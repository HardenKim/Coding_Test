import java.util.*;

class Solution {
    List<Map<String, Integer>> FoodMaps = new ArrayList<>();
    int[] MaxCnt = new int[11]; // 계산하기 편하게 문자길이 length = index
    
    void comb(char[] str, int pos, StringBuilder candi) {
        if (pos >= str.length) {
            int len = candi.length();
            if (len >= 2) {
                int cnt = FoodMaps.get(len).getOrDefault(candi.toString(), 0) + 1;
                FoodMaps.get(len).put(candi.toString(), cnt);
                MaxCnt[len] = Math.max(MaxCnt[len], cnt);
                
            }
            return;
        }
        
        
        comb(str, pos+1, candi.append(str[pos]));   // 현재 문자 선택
        candi.setLength(candi.length()-1);  // 선택한 문자 다시 빼기
        comb(str, pos+1, candi);
    }
    
    public String[] solution(String[] orders, int[] course) {
        // orders 최대 길이 10
        for (int i=0; i<11; i++) 
            FoodMaps.add(new HashMap<String, Integer>());
        
        // 세트 조합 만들기
        for (String str : orders) {
            char[] arr = str.toCharArray();
            // 배열 정렬
            Arrays.sort(arr);
            comb(arr, 0, new StringBuilder());
        }
        
        // 조합에서 course 길이에 해당하는 최대 조합 추출
        List<String> list = new ArrayList<>();
        for (int len : course) {
            for (Map.Entry<String, Integer> entry : FoodMaps.get(len).entrySet()) {
                if (entry.getValue() >= 2 && entry.getValue() == MaxCnt[len]) {
                    list.add(entry.getKey());
                }
            }
        }
        Collections.sort(list);
        
        String[] answer = new String[list.size()];
        for (int i=0; i<list.size(); i++)
            answer[i] = list.get(i);
        
        return answer;
    }
}