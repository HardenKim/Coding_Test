import java.util.*;

class Solution {
    static final int INF = 987654321;
    int[] Sales;
    List<List<Integer>> Team = new ArrayList<>();
    int[][] Cost = new int[300000][2];
    
    void traversal(int node) {
        Cost[node][0] = 0;              // 회의 참석
        Cost[node][1] = Sales[node];    // 회의 미참석
        
        if (Team.get(node).isEmpty()) return;
        
        int extraCost = INF;
        for (int member : Team.get(node)) {
            traversal(member);
            if (Cost[member][0] < Cost[member][1]) {
                Cost[node][0] += Cost[member][0];
                Cost[node][1] += Cost[member][0];
                // 모든 직원이 참석을 안할 수 있으니
                // Cost[member][1]을 더하고 기존에 더한 Cost[member][0]을 뺀다
                extraCost = Math.min(extraCost,
                                     Cost[member][1] - Cost[member][0]);
            } else {
                Cost[node][0] += Cost[member][1];
                Cost[node][1] += Cost[member][1];
                // 참석한 직원이 있으니 extraCost = 0
                extraCost = 0;
            }
        }
        // 모든직원이 참석안했을 경우 extraCost는 0이 아니다
        Cost[node][0] += extraCost;
        
    }
    
    public int solution(int[] sales, int[][] links) {
        Sales = sales;
        // 모든 직원이 팀장이 될 수 있으니 직원 수만큼 리스트 생성
        for (int i=0; i<sales.length; i++) {
            Team.add(new ArrayList<>());
        }
        // 팀장-팀원
        // 직원을 인덱스로 표기하기 쉽게 -1
        for (int[] link : links) {
            Team.get(link[0]-1).add(link[1]-1);
        }
        
        traversal(0);
        return Math.min(Cost[0][0], Cost[0][1]);
    }
}


/*
Map<Integer, List<Integer>
*/