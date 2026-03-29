#include <unordered_map>
#include <string>

class Solution {
public:
 bool isSame(unordered_map<char,int> &have, unordered_map<char,int> &required){
          for(auto const & [key,val]: required){
            if(have.find(key) == have.end() || have[key] < required[key]){
                return false;
            }
          }
          return true;  
        };
    string minWindow(string s, string t) {
        unordered_map<char,int> have;
        unordered_map<char,int> required;

        for(auto c: t){
            required[c]+=1;
        }

        int start = 0;
        int end = 0;

        int m = 100001;
        int res[2] = {0,0};


        while(end != s.length()){
            char c = s[end];
            have[c]+=1;
            while(isSame(have,required)){
        
                // Store min string first
                if (m > (end-start+1)){
                    m = end-start+1;
                    res[0] = start;
                    res[1] = end-start+1;
                }

                char leftchar = s[start];
                have[leftchar]-=1;
                start++;
            }
            end+=1;

        }
        return s.substr(res[0],res[1]);

    }
};