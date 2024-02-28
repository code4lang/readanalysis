#!/bin/bash

# Specify the path to your CSV file
CSV_FILE="C:\Users\Utilisateur\OneDrive\Escritorio\marinaproject\contacts_google.txt"

# Loop through each row in the CSV file
while IFS= read -r row; do
    # Search for the username using Sherlock
    result=$(sherlock "$row")

    # Print the result
    echo "Username '$row': $result"
done < "$CSV_FILE"
