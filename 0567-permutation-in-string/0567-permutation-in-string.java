class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        int[] s1count = new int[26];
        int[] s2count = new int[26];
        for(int i = 0 ; i < s1.length() ; i++){
            s1count[s1.charAt(i) - 'a'] += 1;
            s2count[s2.charAt(i) - 'a'] += 1;
        }
        int match = 0;
        for(int i = 0 ; i < 26 ; i++){
            if(s1count[i] == s2count[i]){
                match += 1;
            }
        }
        int l = 0;
        for(int r = s1.length() ; r < s2.length() ; r++){
            if(match == 26){
                return true;
            }

            int index = s2.charAt(r) - 'a';
            s2count[index] += 1;
            if(s2count[index] == s1count[index]){
                match += 1;
            }else if(s2count[index] == s1count[index] + 1){
                match -= 1;
            }

            index = s2.charAt(l) - 'a';
            s2count[index] -= 1;
            if(s2count[index] == s1count[index]){
                match += 1;
            }else if(s2count[index] == s1count[index] - 1){
                match -= 1;
            }

            l += 1;
        }
        return match == 26;
    }
}