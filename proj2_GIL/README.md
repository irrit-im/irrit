## Description
This project contains one axample of a programe that is not affected by Python's GIL, and another of a programe that is badly affected by it:

1. <no_impact> is a single-threaded programe, and therefore is not affected by the GIL.

2. <bad_impact> is a multi-threaded, CPU bound programe, and therefore is affected by the GIL. This can be proved by comparing the run time of a single thread: the results show that two identical CPU-bound threads take about double the time to run (meaning the GIL does not allow them to run simultaneosly).