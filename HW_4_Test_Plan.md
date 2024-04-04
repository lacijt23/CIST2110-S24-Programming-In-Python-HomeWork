# Test Plan for HW4

## 1. 'add' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_add | Addition Test with Positive Numbers | 3, 2) | 5 | 1 | FAIL |Assertion Error. Addition failed, - was used instead of +
002 | test_add | Addition Test with Positive Numbers (001 bugfix) | 3, 2) | 5 | 5 | PASS
003 | test_add | Addition Test with 0 | 0,5 | 5 | 5 | PASS

## 2. 'subtract' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_subtract | Subtraction Test with Positive Numbers | 5, 3 | 2 | 8 | FAIL |Assertion Error. Addition was used in the return rather than subtraction
002 | test_subtract | Subtraction Test with Positive Numbers (001 bugfix) | 5, 3 | 2 | 2 | PASS |
003 | test_subtract | Subtraction Test with Expected Negative Difference | 3, 5 | -2 | -2 | PASS |

## 3. 'divide' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_division | Division Test with Positive Divisible Numbers | 6, 2 | 3 | 12 | FAIL | Assertion Error. The return called for multiplication instead of division.
002 | test_division | Division Test with Positive Divisible Numbers (001 bugfix) | 6, 2 | 3 | 3 | PASS |
003 | test_division | Division Test with Zero | 1, 0 | Zero Division Error | Zero Division Error | Pass

## 4. 'multiply' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_multiply | Multiplication Test with Positive Numbers | 4, 3 | 12 | 1.33333 | FAIL | Assertion Error, Multiplication failed. Return called for division instead of multiplication.
002 | test_multiply | Multiplication Test with Positive Numbers (bugfix 001) | 4, 3 | 12 | 12 | PASS | 
003 | test_multiply | Multiplication Test with Zero | 4, 0 | 0 | 0 | PASS | 

## 5. 'greet' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_greet | Greeting test with different names | John | Hello, John! | Heloo, John! | FAIL | Assertion error, Misspelled "Hello!"
002 | test_greet | Greeting test with different names (001 bugfix) | John | Hello, John! | Hello, John! | PASS |
003 | test_greet | Greeting test with different names | Doe | Hello, Doe! | Hello, Doe! | PASS |

## 6. 'grade_calc' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_grade_calculator | Grade test with different numbers 1-100 | 95 | A | A | PASS |
002 | test_grade_calculator | Grade test with different numbers 1-100 | 85 | B | B | PASS |
003 | test_grade_calculator |Grade test with different numbers 1-100 | 75 | C | C | PASS |
004 | test_grade_calculator | Grade test with different numbers 1-100 | 79 | C | Invalid Score | FAIL | Assertion Error, invalid score
005 | test_grade_calculator  | Grade test with different numbers 1-100 (bugfix 004) | 79 | C | C | Pass |
006 | test_grade_calculator  | Grade test with different numbers 1-100 | 65 | D | D | Pass |
007 | test_grade_calculator  | Grade test with different numbers 1-100 | 50 | F | F | Pass |
008 | test_grade_calculator  | Grade test with different numbers 1-100 | 105 | Invalid Score | Invalid Score | Pass |
009 | test_grade_calculator  | Grade test with different numbers 1-100 | -5 | Invalid Score | Invalid Score | Pass |

## 7. 'speed_check' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_speed_check | Checks if number is within the speed limit | 10 | Too slow | Too slow | Pass |
002 | test_speed_check | Checks if number is within the speed limit | 50 | Within limit | Within limit | Pass |
003 | test_speed_check | Checks if number is within the speed limit of 20 to 60 | 80 | Over speed limit | Over speed limit | Pass |
004 | test_speed_check | Checks if number is within the speed limit | 65 | Within Limit | Unknown | FAIL | Speed check failed for upper end of within limit
005 | test_speed_check | Checks if number is within the speed limit (004 bugfix) | 65 | Within Limit | Within limit | Pass |
## 8. 'is_leap_year' Function

| Test Case ID | Test Case Description | Test Data | Expected Result | Actual Result | Pass/Fail | If Fail, Why? |
|--------------|-----------------------|-----------|-----------------|---------------|-----------|-------------|
001 | test_is_leap_year | Checks if a year is a leap year | 2020 | True | True | Pass |
002 | test_is_leap_year | Checks if a year is a leap year | 2021 | False | False | Pass |
003 | test_is_leap_year | Checks if a year is a leap year | 2000 | True | True | Pass |
004 | test_is_leap_year | Checks if a year is a leap year | 1900 | False | True | FAIL | Assertion error, Leap year check failed for century non-leap year
005 | test_is_leap_year | Checks if a year is a leap year (004 bugfix) | 1900 | False | False | Pass |