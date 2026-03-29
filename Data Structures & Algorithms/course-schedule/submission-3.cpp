#include<unordered_map>

class Solution {
public:
    bool dfs(int course, unordered_map<int,int>&mark, unordered_map<int,vector<int>>&mylist){
        
        if(mark[course] == 1){
            return false;
        }

        if(mark[course] == 2){
            return true;
        }
        

        mark[course] = 1;
        for(int i = 0; i<mylist[course].size(); i++){
            if(mylist[course][i] == course) return false;
            if(mark[mylist[course][i]] == 1) return false;

        
            if(!dfs(mylist[course][i], mark, mylist)){
                return false;
            };
        }
        mark[course] = 2;
        return true;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int,vector<int>>mylist;
        unordered_map<int,int>mark;

        for(int i =0; i<prerequisites.size(); i++){
            mylist[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        for(int i = 0; i < numCourses; i++){
            if(!dfs(i, mark, mylist)){
                return false;
            }
        }
        
        return true;
    }
};
