import java.util.*;
class Solution {
    public int[] solution(int[] answers) {
        int[] answer = new int[3];
        int onesum=0,twosum=0,threesum=0;
        int[] one = {1,2,3,4,5};
        int[] two = {2,1,2,3,2,4,2,5};
        int[] three= {3,3,1,1,2,2,4,4,5,5};
        
        for(int i=0 ;i <answers.length;i++){
            if (one[i%one.length] == answers[i]){
                onesum+=1;
            }
            if (two[i%two.length] == answers[i]){
                twosum+=1;
            }
            if (three[i%three.length] == answers[i]){
                threesum+=1;
            }
        }
        
        int maxx =Math.max(onesum,Math.max(twosum,threesum));
        int cnt=0;
        List ansList = new ArrayList();
        if (onesum==maxx){
            ansList.add(1);
        }
        if (twosum==maxx){
            ansList.add(2);
           
        }
        if (threesum==maxx){
            ansList.add(3);
            
        }
        answer= new int[ansList.size()];
        for ( Object num : ansList){
            answer[cnt]=(int)num;
            cnt+=1;
        }
        return answer;
    }
}