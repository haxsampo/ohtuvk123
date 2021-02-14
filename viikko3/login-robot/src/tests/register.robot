*** Settings ***
Resource  resource.robot
Test Setup  Input Login Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  asiodjhoua  8dua98hd987ad
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  8dua98hd987ad
    Input  new
    Input Credentials  kalle  839j40984j834
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  8dua98hd987ad
    Output Should Contain  Username too short.

Register With Valid Username And Too Short Password
    Input Credentials  kalle  1a
    Output Should Contain  Password too short.

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kalle  oaosiudiasasdij
    Output Should Contain  Password only contains letters.

*** Keywords ***
Input Login Command
    Input  new