""" Simple benchmark function to measure contract's execution time. """
import time
import numpy


# ==================================================
# tester -- benchmarking framework
# ==================================================
def tester(repeat, test_name, test_to_run, *args):
    # repeat the experiemnt 'repeat' times 
    times = []
    for i in range(repeat):
        # take average over 'repeat' execution (timer resolution)
        start_time = time.time()
        for i in range(repeat):
            # DUT
            test_to_run(*args)

        end_time = time.time()
        times.append( (end_time-start_time)/ repeat )

    # compute mean and std
    mean = numpy.mean(times)
    sd = numpy.std(times)

    # print result
    print(test_name + "\t{:.10f}\t\t{:.10f}\t{:.0E}".format(mean*1000, sd*1000, repeat))


# ==================================================