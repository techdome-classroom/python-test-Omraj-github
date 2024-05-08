def decode_message( s: str, p: str) -> bool:

         s_index = 0  # Index for iterating through the secret message
    p_index = 0  # Index for iterating through the decoder key
    
    while s_index < len(s) and p_index < len(p):
        if p[p_index] == '*':
            # If the current symbol in the decoder key is '*', it matches any sequence of letters
            # Move to the next character in the decoder key
            p_index += 1
            
            # If '*' is the last symbol in the decoder key, it can match the remaining characters in the secret message
            if p_index == len(p):
                return True
            
            # Iterate through the secret message until finding the next character that matches the one after '*' in the decoder key
            while s_index < len(s) and s[s_index] != p[p_index]:
                s_index += 1
        elif p[p_index] == '?':
            # If the current symbol in the decoder key is '?', it can match any single letter
            # Move to the next character in both the secret message and the decoder key
            s_index += 1
            p_index += 1
        elif s[s_index] == p[p_index]:
            # If the characters match, move to the next character in both the secret message and the decoder key
            s_index += 1
            p_index += 1
        else:
            # If none of the above conditions are met, the decoder key doesn't match the message
            return False
    
    # If both indices reached the end of their respective strings, the decoder key matches the message
    return s_index == len(s) and p_index == len(p)

  
        return False