from multiprocessing import Pool, cpu_count  # Import the necessary modules
import time
import mpmath as mp

mp.dps = 102  # Set the decimal precision to 100, which will result in pi being calculated to 100 decimal places

start_time = time.time()  # Record the start time for performance analysis

def calculate_sum(start, end):  # Define the function that will be run in parallel
    sign = 1
    local_sum = 0
    for i in range(start, end):  # Loop over the iterations assigned to this process, computing the value of pi for each iteration and adding it to the local sum
        st = mp.mpf(4)/mp.mpf((8*i)+1)
        nd = mp.mpf(2)/mp.mpf((8*i)+4)
        rd = mp.mpf(1)/mp.mpf((8*i)+5)
        th = mp.mpf(1)/mp.mpf((8*i)+6)
        multi = mp.mpf(1)/mp.mpf(16**i)
        local_sum += multi*(st-nd-rd-th)
    return local_sum  # Return the local sum

if __name__ == '__main__':  # Make sure the code is being run from the main module
    n = 10000  # Set the number of iterations to 10000
    num_processes = min(n, cpu_count())  # Determine the number of processes to use based on the number of available CPU cores
    chunk_size = n // num_processes  # Determine the chunk size, or number of iterations assigned to each process
    pool = Pool(processes=num_processes)  # Create a process pool with the specified number of processes
    results = []  # Initialize an empty list to hold the results from each process
    for i in range(num_processes):  # Loop over the number of processes, assigning iterations to each process
        start = i * chunk_size
        end = start + chunk_size if i != num_processes - 1 else n  # If this is the last process, assign it all remaining iterations
        results.append(pool.apply_async(calculate_sum, args=(start, end)))  # Add the result from each process to the results list
    pool.close()  # Close the process pool to prevent any more tasks from being submitted
    pool.join()  # Wait for all processes to complete

    # combine the results from all processes
    final_sum = 0
    for result in results:
        final_sum += result.get()

    end_time = time.time()  # Record the end time for performance analysis
    total_time = end_time - start_time  # Calculate the total time taken for the calculations

    # Set the known value of pi to compare with the calculated value
    known_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

    # Convert the calculated value of pi to a string with 102 decimal places
    calc_pi = str(final_sum)[:102]

    # Determine the number of digits that are different between the known value and the calculated value
    min_len = min(len(known_pi), len(calc_pi))
    num_diff = 0
    for i in range(min_len):
        if known_pi[i] != calc_pi[i]:
            num_diff += 1

    # Print the results
    print('Computed pi value is: \n{}'.format(calc_pi))
    print('Known pi value is: \n{}'.format(known_pi))
    print('The number of different digits is: {}'.format(num_diff))
    print('Total time taken: {:.4f} seconds'.format(total_time))