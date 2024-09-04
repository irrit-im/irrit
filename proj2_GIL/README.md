## Description
This project contains two programs:

1. `no_impact` is a single-threaded program, and therefore is not affected by the GIL.

3. `bad_impact` is a multi-threaded, CPU-bound program, and therefore is affected by the GIL. This can be proved by comparing its run time to that of a single (identical) thread: the results show that two identical CPU-bound threads take about double the time to run (meaning the GIL does not allow them to run simultaneosly).
