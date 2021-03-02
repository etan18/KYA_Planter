# KYA_Planter

Application written by Erin Tan and Meha Patel of the Middlesex County Academy for Science, Mathematics, and Engineering Technologies as part of the Capstone Project

## Make Applications Executable
For GUI Programs, convert .py file to .exe file by running the following command in Command Prompt/Terminal:
```
pyinstaller --onefile <file_name>.py
```

## Raspberry Pi Headless Setup
Find local Raspberry Pi using the following command in Command Prompt/Terminal:
```
ping raspberrypi.local
```
Establish Secure Shell (SSH) network
```
ssh -v pi@[IP Adress]
```
Default Raspberry Pi Password is "raspberry"

## Raspberry Pi Pins

1.
2. 5V to breadboard
3.
4. 5V to breadboard
5.
6. Ground to breadboard
7.
8.
9.
10.
11.
12.
13.
14.
15.
16.
17.
18.
19. GPIO10(MOSI) -> MCP3008 Pin 11(DIN)
20.
21. GPIO9(MISO) -> MCP3008 Pin 12(DOUT)
22.
23. GPIO11(SCLK) -> MCP3008 Pin 13(CLK)
24. GPIO8(CEO) -> MCP3008 Pin 10(CS/SHDN)
25.
26.
27.
28.
29.
30.
31.
