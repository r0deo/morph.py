# Assignment
# Create the following variables. Use comparison operators to determine their boolean values. The context of the parameter names should tell you how to make these comparisons. Return them in this order:

# is_mustang_edward_same
# is_alphonse_edward_same
# is_winry_alphonse_same


def compare_heights(edward_height, alphonse_height, winry_height, mustang_height):
    # Check if Mustang and Edward have the same height
    is_mustang_edward_same = edward_height == mustang_height
    
    # Check if Alphonse and Edward have the same height
    is_alphonse_edward_same = alphonse_height == edward_height
    
    # Check if Winry and Alphonse have the same height
    is_winry_alphonse_same = winry_height == alphonse_height
    
    return is_mustang_edward_same, is_alphonse_edward_same, is_winry_alphonse_same



        
        


