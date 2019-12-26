# 1. DFA
class Solution:
    def isNumber(self, s: str) -> bool:
        
        # using DFA (Deterministic Finite Automaton), like constructing Directed Graph.
        # No need distinguish + and -
        
        state = {
            ""    : {"sign": "-", "num": "1", "dot": "."},
            "."   : {"num": ".1"},
            "1"   : {"num": "1", "dot": ".1", "exp": "1e"},
            ".1"  : {"num": ".1", "exp": "1e"},
            "-"   : {"num": "-1", "dot": "-."},
            "-."  : {"num": "-1"},
            "-1"  : {"num": "-1", "dot": ".1", "exp": "1e"},
            "1e"  : {"num": "1e1", "sign": "1e-"},
            "1e1" : {"num": "1e1"},
            "1e-" : {"num": "1e1"},
        }
        
        s = s.strip()
        cur = ""
        
        for ch in s:
            if ch == ".":
                token = "dot"
            elif ch.isdigit():
                token = "num"
            elif ch == "e":
                token = "exp"
            elif ch in "+-":
                token = "sign"
            else:
                return False
            if token in state[cur]:
                cur = state[cur][token]
            else:
                return False
        
        valids = set(["1", ".1", "-1", "1e1"])
        return cur in valids

# 2. alternatively, not recommended
class Solution:
    def isNumber(self, s: str) -> bool:
        
        s = s.strip()
        dot = 0  # decimal
        digit = 0  # digit
        sign = 0  # sign
        e = 0  # e
                
        for ch in s:
            if ch.isdigit():
                digit += 1
            elif ch in "-+":
                sign += 1
                if sign == 2 or digit > 0 or dot > 0: return False
            elif ch == ".":
                dot += 1
                if e > 0 or dot == 2: return False
            elif ch == "e":
                e += 1
                if e == 2 or digit == 0: return False
                sign = 0
                digit = 0
                dot = 0
            else:
                return False

        return digit > 0
            
                
        