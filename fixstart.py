def replace_0a_with_0_inplace(filename):
    with open(filename, 'r') as f:
        data = f.read()

    updated_data = data.replace(' 0a ', ' 0 ')

    with open(filename, 'w') as f:
        f.write(updated_data)

# Example usage
replace_0a_with_0_inplace('input.txt')
