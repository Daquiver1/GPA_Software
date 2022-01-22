def calc_gpa_needed(old_gpa, new_gpa, old_chours, new_chours):
	total_chours = old_chours + new_chours
	new_points = total_chours * new_gpa
	old_points = old_chours * old_gpa
	diff_points = new_points - old_points
	min_gpa = diff_points / new_chours

	return min_gpa

old = float(input("Please enter your current gpa: "))
new = float(input("Please enter your desired gpa: "))
c_old = float(input("Please enter your old credit hours: "))
c_new = float(input("Please enter your new credit hours: "))

print(calc_gpa_needed(old, new, c_old, c_new))