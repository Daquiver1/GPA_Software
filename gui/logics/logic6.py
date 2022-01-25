def gpa():
	temp = f"""
GPA also known as grade point average is a metric used to measure academic perfomances.
GPA is for a single semester and CGPA is for cumulative semesters.
It ranges from 0.0 to 4.0.
GPA is calculated by adding total credit hours, and total grade point. Then it divides total grade point by total credit hours
Total grade point = (grade point * credit hours) 
The grade points varies for Universities, but for the Univeristy of Ghana
A: 4.0
B+: 3.5
B: 3.0
C+: 2.5
C: 2.0
D+: 1.5
D: 1.0
E and F: 0"""

	return temp

def cgpa():
	temp = f"""
CGPA also known as Cumulative Grade point average is the GPA for the total semesters a student has taken.
CGPA = (Total grade points(4.0, 3.0,2.5, etc) * respective credit hours) / Total number of credits taken """

	return temp

def fgpa():
	temp = f"""
FGPA also known as Final Grade point average is final GPA of the student, with this GPA the weights are added.
Weights varies for Universities, but for the University of Ghana the weights are 1:1:2:2 for each level respectively.
It's calculated by calculating the GPA for each level then multiplying it by it's weighting/total weights.
So level 100 and 200 will be * 1/6, 1/6 and level 300 and 400 will be * 2/6, 2/6. 
It adds everything to get your FGPA. """

	return temp

def credit_hours():
	temp = f"""
Credit hours are a eay of measuring how much credit a student receives for attending a course.
Most credit hours are 3, although you are likely to meet courses lower credit hours. 
Higher credit courses have a higher influence on your GPA than lower credit courses."""

	return temp

def resits():
	temp = f"""
Resists are taken when one fails a course, a failure means getting E or F in a course. 
For University of Ghana, F is a compulsory resit and E is an optional resit. 
Resits are detrimental to your GPA, avoid them as much as you can.
If you fail 2 3-credit courses and pass on third attempt, 9 credit hours and their respective grade points will be added to your transcript.
This isn't good for your GPA. Not at all.
If you've taken a resit and want to calculate your CGPA, GPA or FGPA, add your resists to your total number of credit hours and the grades.
So first sem 5 3-credit courses but I took 2 3-credit resits. That'll be 7 courses with 21 credit hours"""

	return temp

def levels():
	temp = """
The degree classifications(levels) varies for Universites, but for the University of Ghana
First Class: 3.60 - 4.00
Second Class Upper: 3.00 - 3.59
Second Class Lower: 2.00 - 2.99
Third Class: 1.50 - 1.999
Pass: 1.00 - 1.49
Fail(No award): 0.00 - 0.99"""

	return temp

def good_gpa():
	temp = "A good GPA is relative, depends on the individual but a 3.4+ GPA is considered okay."
	return temp

