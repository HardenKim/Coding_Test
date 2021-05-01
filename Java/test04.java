import java.util.*;

class Solution {
    static final int INF = 40000000;
    int[][] Dist = new int[200][200];
    
    void floyd(int n) {
        // 시작->도착 보다 어디를 거쳐서 가는게 더 빠른 최단 경로를 찾는 것
        for (int k=0; k<n; k++) {   // 경유지
            for (int i=0; i<n; i++) {   // 시작점
                for (int j=0; j<n; j++) {   // 도착점
                    Dist[i][j] = Math.min(Dist[i][j], Dist[i][k] + Dist[k][j]);
                }
            }
        }
    }
    
    public int solution(int n, int s, int a, int b, int[][] fares) {
        // 경로 초기화
        for (int i=0; i<n; i++) {
            for (int j=0; j<n; j++) {
                if (i==j) 
                    Dist[i][j] = 0;
                else
                    Dist[i][j] = INF;
            }
        }
        
        // 경로에 주어진 요금 대입
        for (int[] edge : fares) {
            Dist[edge[0]-1][edge[1]-1] = edge[2];
            Dist[edge[1]-1][edge[0]-1] = edge[2];
        }
        
        // 경로에 경유지를 거친 최소 요금 대입
        floyd(n);
        
        // index가 0부터 시작하니 1씩 빼준다.
        s--;
        a--;
        b--;
        
        int answer = INF;
        for (int k=0; k<n; k++) {
            answer = Math.min(answer, Dist[s][k] + Dist[k][a] + Dist[k][b]);
        }
        
        return answer;
    }
}