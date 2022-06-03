def optimal_change(item_cost, amount_paid):

    # Takes in account people paying exact, or not enough
    if round(amount_paid, 2) - round(item_cost, 2) == 0:
        return "You are all set!"
    elif round(item_cost, 2) > round(amount_paid, 2):
        return "You do not have enough money!"

    # Formats the item cost properly for the final string output
    string_item_cost = str(item_cost)
    item_cost_list = string_item_cost.split(".")
    if len(item_cost_list) == 1:
        pass
    elif len(item_cost_list[1]) == 1:
        item_cost_list.append(f".{item_cost_list[1]}0")
        item_cost_list.pop(1)    
    else:
        item_cost_list.append(f".{item_cost_list[1]}")
        item_cost_list.pop(1)
    adjusted_item_cost = "".join(item_cost_list)
    
    # Seperate area to declare variables needed for calculations (Note 1: Probably should have made seperate functions)
    cashback_needed = []
    coins_needed = []
    total_change_needed = round(amount_paid - item_cost, 2)
    paper_money_dictionary = {

        "$100":100,
        "$50":50,
        "$20":20,
        "$10":10,
        "$5":5,
        "$1":1
    }

    coin_number_dictionary = {

        "25c": .25,
        "10c": .10,
        "5c": .05,
        "1c": .01
    }
        
    # Calculations begin 
    
    while total_change_needed >= 1:
        for monetary_value in paper_money_dictionary:
            if paper_money_dictionary[monetary_value] > total_change_needed:
                continue # Skips over when you would recieve to much paper money
            cashback_needed.append(monetary_value)
            total_change_needed -= paper_money_dictionary[monetary_value]
            total_change_needed = round(total_change_needed, 2)
            break # Resets for loop to check each bill again
    while total_change_needed < 1 and total_change_needed > 0:
        for monetary_value in coin_number_dictionary:
            if coin_number_dictionary[monetary_value] > total_change_needed:
                continue # Same concept as the former loop
            coins_needed.append(monetary_value)
            total_change_needed -= coin_number_dictionary[monetary_value]
            total_change_needed = round(total_change_needed, 2)
            break # Same concept as the former loop

    # Begins final formating of string output

    all_money_needed = cashback_needed + coins_needed

    final_output = f"The optimal change for an item that costs ${adjusted_item_cost} with an amount paid of ${str(amount_paid)} is "
    track_occurences = {
        "$100":0,
        "$50":0,
        "$20":0,
        "$10":0,
        "$5":0,
        "$1":0,
        "25c": 0,
        "10c": 0,
        "5c": 0,
        "1c": 0
    }
    
    for prop in track_occurences:
        for i in range(0, len(all_money_needed)):
            if all_money_needed[i] == prop:
                track_occurences[prop] += 1
    
    # Creates a final dictionary to filter out the zero's
    adjusted_track_occurences = {}

    for adjusted_prop in track_occurences:
        if track_occurences[adjusted_prop] > 0:
            adjusted_track_occurences[adjusted_prop] = track_occurences[adjusted_prop]
    
    # Loops through and creates new strings as needed
    correct_adj = ""
    for values in adjusted_track_occurences:
        if "$" in values and adjusted_track_occurences[values] > 1:
            correct_adj = "bills"
            final_output += f"{adjusted_track_occurences[values]} {values} {correct_adj},"
        elif "$" in values and adjusted_track_occurences[values] < 2:
            correct_adj = "bill"
            final_output += f"{adjusted_track_occurences[values]} {values} {correct_adj}," 
        elif values == "25c" and adjusted_track_occurences[values] > 1:
            correct_adj = "quarters"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "25c" and adjusted_track_occurences[values] < 2:
            correct_adj == "quarter"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "10c" and adjusted_track_occurences[values] > 1:
            correct_adj = "dimes"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "10c" and adjusted_track_occurences[values] < 2:
            correct_adj = "dime"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "5c" and adjusted_track_occurences[values] > 1:
            correct_adj = "nickels"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "5c" and adjusted_track_occurences[values] < 2:
            correct_adj = "nickel"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        elif values == "1c" and adjusted_track_occurences[values] > 1:
            correct_adj = "pennies"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        else:
            correct_adj = "penny"
            final_output += f"{adjusted_track_occurences[values]} {correct_adj},"
        final_output += " "
        
    # Allows me to adjust the final portion of the string
    final_output = ".".join(final_output.rsplit(", ", 1))
    final_output = ", and ".join(final_output.rsplit(", ", 1))\

    return final_output