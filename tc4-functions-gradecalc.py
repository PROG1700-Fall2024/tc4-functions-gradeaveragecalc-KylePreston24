############################################
# Tech Check 4 - Provided Starter File
# Take this provided single-grade entry program and re-work it to use a function, to allow the customized entry of 6 different course grades, and
# to calculate a final grade point average for all six courses.
############################################

# Student Name: Kyle Preston

# main() FUNCTION
numericGrade = 0.0

def openingMessaging():
    print("Grade Point Calculator\n")
    print("Valid letter grades that can be entered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can include a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0.\n")

def userInput(prog):
    letterGrade = input("Please enter a letter grade for PROG1700" + prog + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + prog + " : ")
    return letterGrade, modifier, prog

def userInput(netw):
    letterGrade = input("Please enter a letter grade for NETW1700" + netw + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + netw + " : ")
    return letterGrade, modifier, netw


def userInput(osys):
    letterGrade = input("Please enter a letter grade for OSYS1200" + osys + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + osys + " : ")
    return letterGrade, modifier, osys


def userInput(webd):
    letterGrade = input("Please enter a letter grade for WEBD1000" + webd + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + webd + " : ")
    return letterGrade, modifier, webd


def userInput(comm):
    letterGrade = input("Please enter a letter grade for COMM1700" + comm + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + comm + " : ")
    return letterGrade, modifier, comm


def userInput(dbas):
    letterGrade = input("Please enter a letter grade for DBAS1007" + dbas + " : " ).upper()
    modifier = input("Please enter a modifier (+, - or nothing) " + dbas + " : ")
    return letterGrade, modifier, dbas


def calculateGrade(lettergrade):
    if lettergrade == "A":
        numericGrade = 4.0
    elif lettergrade == "B":
        numericGrade = 3.0
    elif lettergrade == "C":
        numericGrade = 2.0
    elif lettergrade == "D":
        numericGrade = 1.0
    elif lettergrade == "F":
        numericGrade = 0.0
    else:
        print('You entered a invalid grade')
        return lettergrade
    
def calculateModifier(lettergrade, grade_Modifier):
    
    if grade_Modifier == "+":
        if lettergrade != "A" and lettergrade != "F": # Plus is not valid on A or F
            numericGrade += 0.3
    elif grade_Modifier == "-":
        if lettergrade != "F":     # Minus is not valid on F
            numericGrade -= 0.3
    return grade_Modifier, lettergrade
def calculateOverallAvg(averageGrade, prog, netw, osys, webd, comm, dbas):
    averageGrade = int(prog + netw + osys + webd + comm + dbas) / 6
    return averageGrade

#def finalGrade(prog, netw, osys, webd, comm, dbas):
    
    

def finalOutput(prog, netw, osys, webd, comm, dbas, averageGrade):
    print(' The numeric value for PROG1700 is: {0}\n'.format(prog))
    print(' The numeric value for PROG1700 is: {0}\n'.format(netw))
    print(' The numeric value for PROG1700 is: {0}\n'.format(osys))
    print(' The numeric value for PROG1700 is: {0}\n'.format(webd))
    print(' The numeric value for PROG1700 is: {0}\n'.format(comm))
    print(' The numeric value for PROG1700 is: {0}\n'.format(dbas))
    print(' Your average grade is: {0}\n'.format(averageGrade))

def main():
    openingMessaging()

    letterGrade = userInput("")
    modifier = userInput("")
    
 
    #averageGrade = float(prog + netw + osys+ webd+ comm + dbas) / 6
    grade = calculateGrade(prog, netw, osys, webd, comm, dbas)
    grade_Modifier = calculateModifier(prog, netw, osys, webd, comm, dbas, )
    finalOutput(prog, netw, osys, webd, comm, dbas,)
   
#PROGRAM EXECUTION STARTS HERE
main()