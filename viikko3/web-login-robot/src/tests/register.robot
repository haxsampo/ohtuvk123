*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  asiopdj
    Set Password  as8y98d
    Confirm Password  as8y98d
    Click Button  Register
    Welcome Page Should be Open

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open