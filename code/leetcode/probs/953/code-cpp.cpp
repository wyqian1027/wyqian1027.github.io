vector<int> hashArr(26, 0);

class Solution {
    
private:
    int checkOrder(string a, string b){
        int m = min(a.size(), b.size());
        for (int i = 0; i < m; i++){
            if (a[i] != b[i]) {
                return hashArr[a[i] - 'a'] - hashArr[b[i] - 'a'];
            }
        }
        return a.size() - b.size();
    }

public:
    bool isAlienSorted(vector<string>& words, string order) {
        
        for (int i = 0; i < order.size(); i++){
            hashArr[order[i] - 'a'] = i;
        }
        for (int i = 0; i < words.size() - 1; i++){
            int s = checkOrder(words[i], words[i+1]);
            if (s > 0) {
                return false;
            } else if (s < 0) {
                continue;
            }
        }
        return true;
    }
 
 ;