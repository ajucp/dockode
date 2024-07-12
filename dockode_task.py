def print_hexagon_pattern(rows, cols):
    display_rows = rows
    display_cols = min(cols, rows)  # Determine the number of columns to display based on the smaller dimension

    top = "  ___   " * display_cols
    mid1 = " /   \\___" * (display_cols - 1) + " /   \\"
    mid2 = " \\___/   " * (display_cols - 1) + " \\___/"

    for r in range(display_rows):
        print(top)
        for _ in range(2):
            print(mid1)
            print(mid2)

# Example usage
print("Pattern for 4 rows and 7 columns:")
print_hexagon_pattern(4, 7)

print("\nPattern for 3 rows and 5 columns:")
print_hexagon_pattern(3, 5)
