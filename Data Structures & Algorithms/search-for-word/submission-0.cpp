class Solution {
public:
    bool backtrack(vector<vector<char>>& board, int i, int j, int stringindex, string word){

        if (i < 0 || i >= board.size() || j < 0 || j >= board[0].size() || board[i][j] != word[stringindex]){
            return false;
        }
        if(stringindex== word.length()-1) return true;

        char temp = board[i][j];
        board[i][j] = '#';


        bool found = 
         backtrack(board, i+1, j, stringindex+1, word) ||
         backtrack(board, i-1, j, stringindex+1, word)||
         backtrack(board, i, j+1, stringindex+1, word)||
         backtrack(board, i, j-1, stringindex+1, word);

         board[i][j] = temp;

         return found;
    }
    bool exist(vector<vector<char>>& board, string word) {
        for(int i =0; i<board.size(); i++){
            for(int j = 0; j<board[0].size(); j++){
                if(backtrack(board,i,j,0,word)){
                    return true;
                }
            }
        }
        return false;
    }

};