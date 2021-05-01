class Solution {
    class Trie {
        Trie[] child = new Trie[26];
        int count;
        
        void insert(String str) {
            Trie curr = this;
            for (char ch : str.toCharArray()) {
                curr.count++;
                int idx = ch - 'a';
                if (curr.child[idx] == null) {
                    curr.child[idx] = new Trie();
                }
                curr = curr.child[idx];
            }
            curr.count++;
        }
        
        int search(String str) {
            Trie curr = this;
            for (char ch : str.toCharArray()) {
                if (ch == '?') return curr.count;
                
                curr = curr.child[ch - 'a'];
                if (curr == null)
                    return 0; 
            }
            // 접두사를 reverse 하기 때문에 ? 는 모두 접미사로 마지막에 나오므로
            // 여기까지 올 수 없음 
            return -1;
        }
    }
    
    Trie[] TrieRoot = new Trie[10000];
    Trie[] ReTrieRoot = new Trie[10000];
    
    public int[] solution(String[] words, String[] queries) {        
        int[] answer = new int[queries.length];
        int ansIdx = 0;
        
        // words -> Tire
        for (String str : words) {
            int idx = str.length() - 1;
            if (TrieRoot[idx] == null) {
                TrieRoot[idx] = new Trie();
                ReTrieRoot[idx] = new Trie();
            }
            
            TrieRoot[idx].insert(str);
            str = new StringBuilder(str).reverse().toString();
            ReTrieRoot[idx].insert(str);
        }
        // Search
        for (String str : queries) {
            int idx = str.length() - 1;
            if (TrieRoot[idx] == null) {
                answer[ansIdx++] = 0;
                continue;
            }
            
            if (str.charAt(0) != '?') { // 마지막이 '?' 일때
                answer[ansIdx++] = TrieRoot[idx].search(str);
            } else { // 처음이 '?' 일때
                str = new StringBuilder(str).reverse().toString();
                answer[ansIdx++] = ReTrieRoot[idx].search(str);
            }
            
            
        }
        
        return answer;
    }
}