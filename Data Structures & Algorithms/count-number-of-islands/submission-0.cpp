#include <map>
#include<vector>
class Solution {
public:
    void dfs(map<vector<int>,bool> &mark, vector<vector<char>>& grid, int i, int j){
        if (i < 0 || i >= grid.size() || j < 0 || j >= grid[0].size() || grid[i][j] == '0' || mark[{i,j}]){
            return;
        }

        mark[{i,j}] = true;
        dfs(mark, grid, i+1, j);
        dfs(mark, grid, i, j+1);
        dfs(mark, grid, i-1, j);
        dfs(mark, grid, i, j-1);
        return;
    }

    int numIslands(vector<vector<char>>& grid) {
        int count = 0;
        map<vector<int>, bool>mark;
        for(int i =0; i<grid.size(); i++){
            for(int j=0; j<grid[i].size(); j++){
                if(mark[{i,j}]){
                    continue;
                }
                if(grid[i][j] == '1'){
                    dfs(mark, grid, i, j);
                    count += 1;
                }
                
            }
        }
        return count;
        
    }
};
