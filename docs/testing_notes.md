# Testing Notes

## Test Case 1: Upload valid CSV
Expected: Application loads the dataset and displays KPI metrics.

## Test Case 2: SLA breach detection
Expected: Rows with `sla_status = BREACHED` appear in the risk section.

## Test Case 3: Department summary
Expected: Application groups requests by department and calculates total requests, average cycle time, and estimated savings.

## Test Case 4: Executive summary generation
Expected: Application creates a readable summary using calculated KPI values.

## Test Case 5: Recommendation logic
Expected: Application recommends action when SLA breaches or high cycle times exist.
