# boxGame
輸入一個n代表字串長度以及m代表字串數量  
並且輸入m個長度為n的隨機數字字串  
ex：3 3  
1 2 3  
2 3 1  
3 2 1  
輸入完後code會去看字串中數字上下左右是否有相鄰的會將其消除變為0  
ex：  
1 2 3  
2 3 0  
3 2 0  
之後遇到0在數值的下層，code會再將數字墜落  
ex：  
1 2 0  
2 3 0  
3 2 3  
即為答案。  
