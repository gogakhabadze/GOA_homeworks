# Create a list with all learned data types twice
data_types = [
    int, int,
    float, float,
    str, str,
    list, list,
    tuple, tuple,
    dict, dict,
    set, set,
    bool, bool
]

# Extract and print only Boolean values using indexing
boolean_values = [data_types[-2], data_types[-1]]
print(boolean_values)