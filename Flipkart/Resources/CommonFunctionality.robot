*** Settings ***
Library     SeleniumLibrary
Library     Collections
Library     OperatingSystem
Library     Screenshot



*** Variables ***
${env}      Prod
&{url}      prod=https://www.flipkart.com   FN1=
@{browser}      gc  ff  headlesschrome

*** Test Cases ***
Flipkart product search
    start test case
    Finish Test Case

*** Keywords ***
Start Test Case
    Open Browser    ${url.${env}}   ${browser}[0]
    Maximize Browser Window
Finish Test Case
    Close Browser
