// Vanilla 
class Solution {
    public int ladderLength(String A, String B, List<String> wordList) {
        
        Deque<String> q = new ArrayDeque<>();
        Set<String> set = new HashSet<>();
        Set<String> visited = new HashSet<>();
        set.addAll(wordList);
        visited.add(A);
        if (!set.contains(B)) return 0;
        int level = 1;
        q.offer(A);
        
        while (!q.isEmpty()){
            int size = q.size();
            
            for (int i = 0; i < size; i++){
                String cur = q.poll();
                if (cur.equals(B)) return level;
                
                char[] arr = cur.toCharArray();
                for (int j = 0; j < arr.length; j++){
                    char old = arr[j];
                    for (char k = 'a'; k <= 'z'; k++){
                        arr[j] = k;
                        String trans = new String(arr);
                        if (set.contains(trans) && !visited.contains(trans)) {
                            q.offer(trans);
                            visited.add(trans);
                        }
                    }
                    arr[j] = old;
                }
            }
            level += 1;
        }
        return 0;
    }
}

// Improved with double BFS
class Solution {

    public int ladderLength(String beginWord, String endWord, List<String> wordList) {  
        Set<String> wordSet = new HashSet<>(wordList);
        if (!wordSet.contains(endWord))
            return 0;
        Set<String> beginSet = new HashSet<>(), endSet = new HashSet<>();

        int len = 1;
        Set<String> visited = new HashSet<>();

        beginSet.add(beginWord);
        endSet.add(endWord);
        while (!beginSet.isEmpty() && !endSet.isEmpty()) {
            if (beginSet.size() > endSet.size()) {
                // Swap two sets
                Set<String> set = beginSet;
                beginSet = endSet;
                endSet = set;
            }

            Set<String> temp = new HashSet<>();
            for (String word : beginSet) {
                char[] chs = word.toCharArray();

                for (int i = 0; i < chs.length; i++) {
                    for (char c = 'a'; c <= 'z'; c++) {
                        char old = chs[i];
                        chs[i] = c;
                        String target = String.valueOf(chs);

                        if (endSet.contains(target)) {
                            return len + 1;
                        }

                        if (!visited.contains(target) && wordSet.contains(target)) {
                            temp.add(target);
                            visited.add(target);
                        }
                        chs[i] = old;
                    }
                }
            }

            beginSet = temp;
            len++;
        }

        return 0;
    }
}