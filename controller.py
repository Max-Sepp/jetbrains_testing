import subprocess
import sys

def write(process, str):
    process.stdin.write(f'{str}\n')
    process.stdin.flush()

def readline(process):
    return process.stdout.readline().strip()

def average(numList):
    sum = 0
    for num in numList:
        sum += num
    
    return sum / len(numList)

def median(sortedNumList):
    medianPosition = (len(sortedNumList) + 1) / 2
    fractionalPart = medianPosition - int(medianPosition)
    if (fractionalPart == 0):
        return sortedNumList[medianPosition]
    
    return (sortedNumList[int(medianPosition)] + sortedNumList[int(medianPosition)]) / 2

def main():
    if len(sys.argv) <= 1:
        print("No program passed in as argument")
        return
    
    program = sys.argv[1]

    randomNumProcess = subprocess.Popen(
        ['python', program],
        stdin=subprocess.PIPE, 
        stdout=subprocess.PIPE, 
        stderr=subprocess.PIPE, 
        text=True
    )

    write(randomNumProcess, "Hi")
    hiResponse = readline(randomNumProcess)
    if hiResponse != "Hi":
        print("Did not return correct \"Hi\" response")

    randNumList = []
    for i in range(100):
        write(randomNumProcess, "GetRandom")
        randNum = readline(randomNumProcess)
        randNumList.append(int(randNum))
    
    write(randomNumProcess, "Shutdown")
    returnCode = randomNumProcess.wait()

    randNumList.sort()

    print(randNumList)

    print(f'Average: {average(randNumList)}')
    print(f'Median: {median(randNumList)}')

    

if __name__ == "__main__": 
    main()