class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> hs;
        for(int num: nums){
            if (hs.count(num)) return true;
            hs.insert(num);
        }
        return false;
    }
};