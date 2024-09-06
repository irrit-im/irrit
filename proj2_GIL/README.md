## Description
This project contains two programs:

1. `no_impact` is a multi-threaded, I/O bound program, and therefore is only mildly affected by the GIL. This can be demonstrated by comparing its run time to that of a single (identical) thread: the results show that two identical CPU-bound threads take roughly the same time to run, indicating that the GIL is released during the wait periods. However, the multi-threaded version takes slightly longer to run due to the constant aquiry and release of the GIL.

3. `bad_impact` is a multi-threaded, CPU-bound program, and therefore is affected by the GIL. This can be demonstrated by comparing its run time to that of a single threaded version: the results show that two identical CPU-bound threads take about double the time to run, meaning the GIL prevents them from running simultaneosly.
