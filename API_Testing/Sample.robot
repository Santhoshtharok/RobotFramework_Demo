*** Settings ***
Library     SeleniumLibrary
Library     RequestsLibrary
Library     JSONLibrary
Library     Collections
Library     Datadriver



*** Test Cases ***
Do a GET request and validate the Response code and Response body
    [documentation]  This test case verifies that the response code of the GET Request should be 200,
    ...  the response body contains the 'title' key with value as 'London',
    ...  and the response body contains the key 'location_type'.
    [tags]  Smoke
    Create Session        MySession   https://www.metaweather.com     Verify= True
    ${respone}=     GET On Session    MySession     /api/location/search/  params=query=london
    Status Should Be    200     ${response}   #Check Status as 200

    #Check id as 101 from Response Body
    ${id}=  Get Value From Json    ${respomse.json()}   id
    ${idFromList}=  Get From List    ${id}  0
    ${idFromListAsString}=  Convert To String    ${idFromList}
    Should Be Equal As Strings    ${idFromListAsString}     101

    #Check the value of the header contenttype
    ${getHeaderValue}=    Get From Dictionary    ${response.headers}   Content-Type
    Should Be Equal    ${getHeaderValue}    application/json; charset=utf-8



