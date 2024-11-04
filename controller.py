import subprocess
import sys

def write(process, str):
    """
    Writes to the process the desired string.
    Handles adding newline at the end of the string and
    flushing the stdout so the string is definitely sent
    """
    process.stdin.write(f'{str}\n')
    process.stdin.flush()

def readline(process):
    """
    Reads a line from stdin from the process
    Removes unnecessary whitespace and the newline character
    """
    return process.stdout.readline().strip()

def average(numList):
    return sum(numList) / len(numList)

def median(sortedNumList):
    """
    Returns the median of the list
    Precondition: the list is already sorted
    """
    medianPosition = (len(sortedNumList) + 1) / 2
    fractionalPart = medianPosition - int(medianPosition)
    medianIndex = int(medianPosition) - 1
    if (fractionalPart == 0):
        return sortedNumList[medianIndex]
    
    return (sortedNumList[medianIndex] + sortedNumList[medianIndex + 1]) / 2

def getRandomList(process):
    """
    Gets a list of 100 random elements from the process
    """
    randNumList = []
    for i in range(100):
        write(process, "GetRandom")
        randNum = readline(process)
        randNumList.append(int(randNum))
    return randNumList

def main():
    # Gets program name from program arguments
    if len(sys.argv) <= 1:
        print("No program passed in as argument")
        return
    
    program = sys.argv[1]

    # creates the subprocess
    randomNumProcess = subprocess.Popen(
        ['python', program],
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )


    # Performs the "Hi function call"
    write(randomNumProcess, "Hi")
    hiResponse = readline(randomNumProcess)
    if hiResponse != "Hi":
        print("Did not return correct \"Hi\" response")

    randNumList = getRandomList(randomNumProcess)
    
    # shutsdown the subprocess
    write(randomNumProcess, "Shutdown")
    returnCode = randomNumProcess.wait()

    randNumList.sort()

    print(randNumList)

    print(f'Average: {average(randNumList)}')
    print(f'Median: {median(randNumList)}')

    

if __name__ == "__main__": 
    main()