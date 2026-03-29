class Solution {
public:
    bool dfs(unordered_map<int,int>&marked, unordered_map<int,vector<int>>&mylist, int course, vector<int>&res){
        if(marked[course] == 1){
            return false;
        }

        if(marked[course]==2){
            return true;
        }

        marked[course] = 1;
        for(int i = 0; i<mylist[course].size(); i++){
            if(!dfs(marked, mylist, mylist[course][i], res)){
                return false;
            }
            
        }

        marked[course] = 2;
        res.push_back(course);
        return true;
    }

    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        // build the adjacency list
        unordered_map<int,vector<int>>mylist;

        for(int i = 0; i<prerequisites.size(); i++){
            mylist[prerequisites[i][0]].push_back(prerequisites[i][1]);
        }

        unordered_map<int,int>marked;

        vector<int>res = {};


        for(int i = 0; i<numCourses; i++){
            if(!dfs(marked, mylist, i, res)){
                return {};
            }
        }
        return res;
    }
};
