#include <set>
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        //validate rows
        for (int i=0; i<9; i++){
            set<char> seen;
            for (int j=0; j<9; j++){
                char item = board[i][j];
                if (item != '.'){
                    if (seen.count(item)){
                        return false;
                    }
                    seen.insert(item);
                }
            }
        }
        //validate columns
                for (int i=0; i<9; i++){
            set<char> seen;
            for (int j=0; j<9; j++){
                char item = board[j][i];
                if (item != '.'){
                    if (seen.count(item)){
                        return false;
                    }
                    seen.insert(item);
                }
            }
        }
        //validate boxes
        for (int i=0; i<9; i++){
            set<char> seen;
            for (int j=0; j<9; j++){
                int row = 3 * (i / 3) + j / 3;
                int col = 3 * (i % 3) + j % 3;
                char item = board[row][col];
                if (item !='.'){
                    if (seen.count(item)){
                        return false;
                    }
                    seen.insert(item);
                }
            }
        }
        return true; 
    }
};
