Feature: Bank Transactions
 
 Scenario: Withdraw money
 Given account balance is 100 dollar
 When withdraw 30 dollar
 Then account balance should be 70 dollar