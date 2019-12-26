class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        
        m = len(req_skills)
        n = len(people)
        skillBit = {x:i for i, x in enumerate(req_skills)}
        
        dp = {0: []} # skillset -> index of people
        
        for i, p in enumerate(people):
            his = 0
            for x in p:
                his |= 1 << skillBit[x]
            
            res = []
            for skill, team in dp.items():
                res.append([skill, team])
                
            for skill, team in res:
                newSkill = skill | his
                if newSkill == skill: continue
                if newSkill not in dp or len(team) + 1 < len(dp[newSkill]):
                    dp[newSkill] = team + [i]
        
        return dp[(1 << m)-1]