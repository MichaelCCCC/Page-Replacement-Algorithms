# Python3 implementation of FIFO Page Replacement Algorithm in Operating Systems. 
import pandas as pd
from queue import Queue  

# This is the function used to perform the FIFO Page Replacement Algorithm
def FIFO(pages, n, capacity):
    #To store the current frame
    #"N/A" represent empty frame
    frame = ["N/A"]*capacity 

    #To store the pages in FIFO manner
    indexes = Queue()

    #To store the time
    time = 0

    #To store the output
    output = pd.DataFrame(index=range(0,capacity))

    # Start from initial page  
    page_faults = 0

    for i in range(n):
        # Check if the set can hold more pages  
        if (frame.count("N/A") > 0):
            # Insert it into set if not present  
            # already which represents page fault  
            if (pages[i] not in frame): 
                frame[frame.index("N/A")] = pages[i]

                # increment page fault  
                page_faults += 1

                # Push the current page into 
                # the queue  
                indexes.put(pages[i])

                #Put in the dataframe
                output[time] = frame


        # If the set is full then need to perform FIFO  
        # i.e. remove the first page of the queue from  
        # frame and queue both and insert the current page  
        else: 
              
            # Check if current page is not already present in frames  
            if (pages[i] not in frame): 
                  
                # Pop the first page from the queue  
                val = indexes.queue[0]  
  
                indexes.get()  
  
                # Replace the indexes page
                frame[frame.index(val)] = pages[i]
  
                # push the current page into  
                # the queue  
                indexes.put(pages[i])  
  
                # Increment page faults  
                page_faults += 1

                #Put in the dataframe
                output[time] = frame
            else:
                temp = ["N/A"]*capacity
                temp[frame.index(pages[i])] = "hit"
                output[time] = temp
        time += 1
    print_graph(output, pages,capacity, page_faults)
    
# This is the function used to print out the simulated graph in a nice way
def print_graph(output, pages,capacity, page_faults):
    print("This is the simulated graph using FIFO page replacement algorithm:")
    
    for page in pages:
        print(str(page), end = '\t')
    print('\n')
    for c in range(0,capacity):
        for col in output:
            if(output[col][c] != "N/A"):
                print(output[col][c], end='\t')
            else:
                print(" ", end='\t')
        print('\n')

    print("\nNumber of page fault: " + str(page_faults))
# Driver code  
if __name__ == '__main__':

    print('\n')
    print("Input the reference string reference string.\n")
    print("Please input the reference string separated by comma. (e.g. 7,0,1,2,0,3,0,4,2,3,0,3,0,3,2,1,2,0,1,7,0,1)")

    pages_input = input()
    pages = pages_input.split(',')
    pages = [int(i) for i in pages] 

    capacity = 3
    capacity = int(input("Please input the number of frame:\n"))

    n = len(pages)

    FIFO(pages, n, capacity)
    