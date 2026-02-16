from give_bmi import give_bmi, apply_limit

# Test case 1: Normal case
height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

# Test case 2: Single value
print("\n--- Test case 2: Single value ---")
height2 = [1.80]
weight2 = [75]
bmi2 = give_bmi(height2, weight2)
print(f"BMI: {bmi2}")
print(f"Over limit 25: {apply_limit(bmi2, 25)}")

# Test case 3: All below limit
print("\n--- Test case 3: All below limit ---")
height3 = [1.80, 1.75]
weight3 = [70, 65]
bmi3 = give_bmi(height3, weight3)
print(f"BMI: {bmi3}")
print(f"Over limit 30: {apply_limit(bmi3, 30)}")

# Test case 4: All above limit
print("\n--- Test case 4: All above limit ---")
height4 = [1.60, 1.70]
weight4 = [100, 120]
bmi4 = give_bmi(height4, weight4)
print(f"BMI: {bmi4}")
print(f"Over limit 20: {apply_limit(bmi4, 20)}")

# Test case 5: Error - mismatched lengths
print("\n--- Test case 5: Mismatched lengths ---")
try:
	give_bmi([1.80, 1.75], [70])
except ValueError as e:
	print(f"Error caught: {e}")

# Test case 6: Error - invalid type
print("\n--- Test case 6: Invalid type (string) ---")
try:
	give_bmi(["1.80"], [70])
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 7: Error - negative value
print("\n--- Test case 7: Negative height ---")
try:
	give_bmi([-1.80], [70])
except ValueError as e:
	print(f"Error caught: {e}")

# Test case 8: Error - zero value
print("\n--- Test case 8: Zero weight ---")
try:
	give_bmi([1.80], [0])
except ValueError as e:
	print(f"Error caught: {e}")

# Test case 9: Error - boolean (edge case)
print("\n--- Test case 9: Boolean value ---")
try:
	give_bmi([True], [70])
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 10: apply_limit with valid int limit
print("\n--- Test case 10: apply_limit valid int ---")
bmi10 = [22.5, 28.0, 19.5]
result10 = apply_limit(bmi10, 25)
print(f"BMI: {bmi10}")
print(f"Over limit 25: {result10}")

# Test case 11: apply_limit with float limit (should fail)
print("\n--- Test case 11: apply_limit with float limit ---")
try:
	apply_limit([22.5, 28.0], 25.5)
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 12: apply_limit with string limit (should fail)
print("\n--- Test case 12: apply_limit with string limit ---")
try:
	apply_limit([22.5, 28.0], "25")
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 13: apply_limit with boolean limit (should fail)
print("\n--- Test case 13: apply_limit with boolean limit ---")
try:
	apply_limit([22.5, 28.0], True)
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 14: apply_limit with invalid bmi values
print("\n--- Test case 14: apply_limit with string in bmi list ---")
try:
	apply_limit([22.5, "28.0"], 25)
except TypeError as e:
	print(f"Error caught: {e}")

# Test case 15: apply_limit with all boolean values in bmi
print("\n--- Test case 15: apply_limit with boolean in bmi list ---")
try:
	apply_limit([True, False], 1)
except TypeError as e:
	print(f"Error caught: {e}")