Commit 1:

Optimize ScheduleOptimizer class

- Replaced copy() method with slice notation for creating a copy of the tasks list
- Replaced list comprehension with filter() function and lambda function for filtering available tasks
- Sorted available tasks based on priority score

Commit 2:

Optimize TimeTracker class

- Used dictionary comprehension to generate the time report instead of appending strings in a loop

Commit 3:

Optimize DataAnalyzer class

- Added default argument for the data parameter in the analyze_data() method
