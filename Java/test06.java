import java.util.*;

class Solution {
    class Point {
        int row, col, cnt;
        Point(int r, int c, int t) {
            row = r;
            col = c;
            cnt = t;
        }        
    }
    static final int INF = 987654321;
    static final int[][] D = { {-1,0}, {1,0}, {0,-1}, {0,1} };
    int[][] Board;
    
    int bfs(Point src, Point dist) {
        boolean[][] visited = new boolean[4][4];
        Queue<Point> q = new LinkedList<>();
        q.add(src);
        while (!q.isEmpty()) {
            Point curr = q.poll();
            if (curr.row == dist.row && curr.col == dist.col)
                return curr.cnt;
            
            for (int i=0; i<4; i++) {
                // 한칸 이동
                int nr = curr.row + D[i][0];
                int nc = curr.col + D[i][1];
                if (nr < 0 || nr > 3 || nc < 0 || nc > 3) continue;
                
                if (!visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // cnt + 1 => 방향키 이동은 키 조작 1회
                    q.add(new Point(nr, nc, curr.cnt + 1));
                }
                
                // Ctrl을 통해 끝까지 이동할 경우
                // 4칸이니까 2칸 더 가본다
                for (int j=0; j<2; j++) {
                    // 해당 칸이 카드이면 스탑
                    if (Board[nr][nc] != 0) break;
                    if (nr + D[i][0] < 0 || nr + D[i][0] > 3 || nc + D[i][1] < 0 || nc + D[i][1] > 3)
                        break;
                    nr += D[i][0];
                    nc += D[i][1];
                }
                
                if (!visited[nr][nc]) {
                    visited[nr][nc] = true;
                    // cnt + 1 => 방향키 이동은 키 조작 1회
                    q.add(new Point(nr, nc, curr.cnt + 1));
                }
            }
            
        }
        
        return INF;
    }
    
    int permutate(Point src) {
        int ret = INF;
        // 원하는 카드가 있다면 list에 추가
        for (int num = 1; num <= 6; num++) {
            List<Point> card = new ArrayList<>();
            for (int i=0; i<4; i++) {
                for (int j=0; j<4; j++) {
                    if (Board[i][j] == num) {
                        card.add(new Point(i,j,0));
                    }
                }
            }
            // 원하는 카드가 없을 경우
            if (card.isEmpty()) continue;
            
            // 키 조작 횟수 구하기
            int one = bfs(src, card.get(0)) 
                + bfs(card.get(0) , card.get(1)) + 2;
            int two = bfs(src, card.get(1)) 
                + bfs(card.get(1) , card.get(0)) + 2;
            
            // 카드 지우기
            for (int i=0; i<2; i++) {
                Board[card.get(i).row][card.get(i).col] = 0;
            }
            
            // 카드의 경로를 첫번째 -> 두번째 or 두번째 -> 첫번째
            // 경우의 수 2가지로 나누어 재귀로 최소값을 찾는다.
            ret = Math.min(ret, one + permutate(card.get(1)));
            ret = Math.min(ret, two + permutate(card.get(0)));
            
            // 카드 다시 넣기 (다른 카드부터 시작할 경우를 구하기 위해)
            for (int i=0; i<2; i++) {
                Board[card.get(i).row][card.get(i).col] = num;
            }
        }
        
        // 지울 카드가 하나도 없을 때
        if (ret == INF) return 0;
        
        return ret;
    }
    
    
    public int solution(int[][] board, int r, int c) {
        Board = board;
        return permutate(new Point(r,c,0));
    }
}