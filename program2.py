def decode_message( s: str, p: str) -> bool:

        s_index = 0 
        p_index = 0  

        while s_index < len(s) and p_index < len(p):
                if p[p_index] == '*':
                 p_index += 1
                
                if p_index == len(p):
                        return True
                
                # Iterate through the secret message until finding the next character that matches the one after '*' in the decoder key
                while s_index < len(s) and s[s_index] != p[p_index]:
                        s_index += 1
                        elif p[p_index] == '?':
                        s_index += 1
                        p_index += 1
                        elif s[s_index] == p[p_index]:
                        s_index += 1
                        p_index += 1
                        else:
                return False
    
        return s_index == len(s) and p_index == len(p)

  
        return False