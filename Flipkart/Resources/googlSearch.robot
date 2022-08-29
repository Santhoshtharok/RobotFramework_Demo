*** Settings ***
Library     SeleniumLibrary
Library     OperatingSystem

*** Variables ***
${url}      https://www.google.com
${browser}      gc
${search}       name:q
@{search_values}    robot   1990    CTS

*** Test Cases ***
google_Search
    Open Browser    ${url}      ${browser}
    Maximize Browser window
