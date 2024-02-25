import pandas as pd
import re
# Load the CSV file
df = pd.read_csv('cleaned_data_iteration_v1.csv')

# Function to clean the values in the "Total Amount Received" column
def clean_amount(value):
    if isinstance(value, str):
        # Replace 'NIL' or 'nil' with '00.00'
        if 'NIL' in value.upper():
            return '00.00'
        # Replace ',' with no space
        value = value.replace(',', '')
        # Replace 'lakhs' or 'lakh' with five zeros
        value = re.sub(r'(?i)lakhs?', '00000', value)
        # Remove spaces between numbers
        value = ''.join(value.split())
        # Convert 'numberlakhs' or 'numberlakh' to 'number' + '00000'
        if re.search(r'(?i)\d+lakhs?', value):
            parts = re.split(r'(?i)lakhs?', value)
            if parts[0].isdigit():
                value = parts[0] + '00000'
        # Truncate to 6 digits if length exceeds
        value = value[:6]
        return value
    else:
        return value

# Clean the values in the "Total Amount Received" column
df['Total Amount Received'] = df['Total Amount Received'].apply(clean_amount)

# Save the modified DataFrame back to the CSV file
df.to_csv('test_cleaned5.csv', index=False)

print("Data cleaning completed. Saved as 'test_cleaned.csv'.")
