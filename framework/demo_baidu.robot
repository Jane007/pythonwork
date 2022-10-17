*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Baidu Search Case
    Open Browser        http://www.baidu.com        chrome
    maximize browser window
    Input Text          css:#kw                      奶粉
    Click button        css:#su
    sleep  3
    close browser