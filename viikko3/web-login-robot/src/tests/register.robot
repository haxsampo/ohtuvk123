*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Register With Valid Username And Password
    Go To Register Page
    Set Username  asiopdj
    Set Password  as8y98d34
    Confirm Password  as8y98d34
    Click Button  Register
    Welcome Page Should be Open

Register With Already Taken Username And Valid Password
    Go To Register Page
    Set Username  kalle
    Set Password  as8y98d34
    Confirm Password  as8y98d34
    Click Button  Register
    Register Should Fail With Message  User with username kalle already exists

Register With Too Short Username And Valid Password
    Go To Register Page
    Set Username  a
    Set Password  as8y98d34
    Confirm Password  as8y98d34
    Click Button  Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Go To Register Page
    Set Username  asdeghaz1
    Set Password  a1
    Confirm Password  a1
    Click Button  Register
    Register Should Fail With Message  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Go To Register Page
    Set Username  asdeghaz1
    Set Password  osaiudhaosidhjaaa
    Confirm Password  osaiudhaosidhjaaa
    Click Button  Register
    Register Should Fail With Message  Password can't contain only letters

Register With Nonmatching Password And Password Confirmation
    Go To Register Page
    Set Username  asdeghaz1
    Set Password  osaiudha2323jaaa
    Confirm Password  osaiud00099dhja
    Click Button  Register
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Go To Register Page
    Set Username  jaakko
    Set Password  123asd123123
    Confirm Password  123asd123123
    Click Button  Register
    Go To Login Page
    Set Username  jaakko
    Set Password  123asd123123
    Click Button  Login
    Title Should Be  Ohtu Application main page

Login After Failed Registration
    Go To Register Page
    Set Username  jaakko7
    Set Password  1a22222
    Confirm Password  1as2s2s2s2s2s2s2
    Click Button  Register
    Go To Login Page
    Set Username  jaakko
    Set Password  123asd123123
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

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

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}