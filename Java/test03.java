import java.util.*;

class Solution {
    Map<String, Integer> WordMap = new HashMap<>();
    List<List<Integer>> ScoreList = new ArrayList<>();
    
    public int[] solution(String[] info, String[] query) {
        // 언어 4, 직군 3, 경력 3, 푸드 3 = 4*3*3*3 경우의 수
        WordMap.put("-", 0);
        WordMap.put("cpp", 1);
        WordMap.put("java", 2);
        WordMap.put("python", 3);
        WordMap.put("backend", 1);
        WordMap.put("frontend", 2);
        WordMap.put("junior", 1);
        WordMap.put("senior", 2);
        WordMap.put("chicken", 1);
        WordMap.put("pizza", 2);
        
        for (int i=0; i<4*3*3*3; i++)
            ScoreList.add(new ArrayList<>());
        
        // 점수 저장
        for (String str : info) {
            String[] word = str.split(" ");
            int[] arr = {WordMap.get(word[0]) *3*3*3,
                        WordMap.get(word[1]) *3*3,
                        WordMap.get(word[2]) *3,
                        WordMap.get(word[3])};
            int score = Integer.parseInt(word[4]);
            
            for (int i=0; i<(1<<4); i++) {
                int idx = 0;
                for (int j=0; j<4; j++) {
                    // 언어/직군/경력/푸드 가 '-' 인지 아닌지 확인
                    if ((i & (1<<j)) != 0) {
                        idx += arr[j];
                    }
                }
                // - - - - 에도 점수 넣어준다.
                ScoreList.get(idx).add(score);
            }
        }
        
        // 점수 정렬
        for (int i=0; i<4*3*3*3; i++) {
            Collections.sort(ScoreList.get(i));
        }    
        
        int[] answer = new int[query.length];
        for (int i=0; i<query.length; i++) {
            String[] word = query[i].split(" ");
            int idx = WordMap.get(word[0]) *3*3*3 +
                WordMap.get(word[2]) *3*3 +
                WordMap.get(word[4]) *3 +
                WordMap.get(word[6]);
            int score = Integer.parseInt(word[7]);
            int ret = Collections.binarySearch(ScoreList.get(idx), score);
            // 찾는 값이 없을 경우 -1을 하고 음수로 변경해서 return
            if (ret < 0) { 
                ret = -(ret+1); // 150을 찾을 때 100, 200 만 존재하면 ret = 100 인덱스
            } else {    // score 가 있을 때 이전 index 와 같은 score인지 확인
                for (int j=ret-1; j>=0; j--) {
                    if (ScoreList.get(idx).get(j) == score) {
                        ret = j;    
                    } else {
                        break;
                    }
                }
            }
            answer[i] = ScoreList.get(idx).size() - ret;            
        }        
        return answer;
    }
}