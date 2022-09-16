days_list = ["monday", "Tuesday", 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
temp_list = [12, 14, 15, 14, 21, 22, 24]


def check_values(weather_f_dict):
    check_list = [53.6, 57.2, 59.0, 57.2, 69.8, 71.6, 75.2]
    for i in range(len(check_list)):
        dict_val = list(weather_f.values())[i]
        list_val = check_list[i]
        if dict_val == list_val:
            print(f"Your value at index {i} is correct. {dict_val}")
        else:
            print(f"Your value at index {i} is incorrect. {dict_val} should be ")


weather_c = {days_list[i].title(): temp_list[i] for i in range(len(days_list))}

# WRITE YOUR CODE BELOW. The function above will do the checking.
#######################################

weather_f = { day:(temp*9/5) + 32 for(day, temp) in weather_c.items()}

#######################################
# Don't change the function call below.
check_values(weather_f)