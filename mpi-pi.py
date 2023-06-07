import time
from mpmath import mp
from mpi4py import MPI

mp.dps = 102

start_time = time.time()

pi_sum = mp.mpf(0)
n = 10000

comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()

local_sum = mp.mpf(0)
for i in range(rank, n, size):
    st = mp.mpf((4/mp.mpf((8*i)+1)))
    nd = mp.mpf((2/mp.mpf((8*i)+4)))
    rd = mp.mpf((1/mp.mpf((8*i)+5)))
    th = mp.mpf((1/mp.mpf((8*i)+6)))
    multi = (mp.mpf(1)/(16**i))
    local_sum += multi*(st-nd-rd-th)

pi_sum = comm.reduce(local_sum, op=MPI.SUM, root=0)

end_time = time.time()
total_time = end_time - start_time

if rank == 0:
    known_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

    # Set the known value of pi to compare with the calculated value
    known_pi = '3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679'

    # Convert the calculated value of pi to a string with 102 decimal places
    calc_pi = str(pi_sum)[:102]

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
