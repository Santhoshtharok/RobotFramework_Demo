
*** Settings ***
Library    Collections
#Documentation    Reverse String using RobotFramework

*** Test Cases ***

Reverse String
    ${var}      Set Variable        Robot Framework
    ${set}      Evaluate        $var[::-1]
    Log To Console      \nResult: ${Set}
