def validate_ruc(ruc):
    """Validates peruvian TIN/RUC.
    
    Args:
        ruc a string containing the RUC
        
    Returns:
        True if RUC is valid, False otherwise
    """
 
    # RUC is 11 chars long   
    if len(ruc) != 11:
        return False
    
    # Multipliers
    m = [ 5, 4, 3, 2, 7, 6, 5, 4, 3, 2]
    
    r  = [0 for i in range(0,11)]
    
    for i in range(0, 10):
        r[i] = int(ruc[i]) * m[i]
        r[10] = r[10] + r[i]
    
    res = r[10] % 11
    last = 11 - res
    
    if last == 11: last = 1
    if last == 10: last = 0
    
    if last == int(ruc[10]):
        return True
    else:
        return False

        
        
        
        
