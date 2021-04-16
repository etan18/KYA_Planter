# KYA_Planter

Application written by Erin Tan of the Middlesex County Academy for Science, Mathematics, and Engineering Technologies as part of the Capstone Project

## setup.py
- Sets all settings and values to default
- Run before testing new environments

## pi.py
- Core program, contains all functions for planter function
- Runs in forever loop

### Make Applications Executable
For GUI Programs, convert .py file to .exe file by running the following command in Command Prompt/Terminal:
```
pyinstaller --onefile <file_name>.py
```

## Hardware
![circuit](/Users/ErinTan/Downloads/IMG_7376.jpg)
### Raspberry Pi Headless Setup
Find local Raspberry Pi using the following command in Command Prompt/Terminal:
```
ping raspberrypi.local
```
Establish Secure Shell (SSH) network
```
ssh -v pi@[IP Adress]
```

### Raspberry Pi Pins

19. GPIO10(MOSI) -> MCP3008 Pin 11(DIN)
21. GPIO9(MISO) -> MCP3008 Pin 12(DOUT)
23. GPIO11(SCLK) -> MCP3008 Pin 13(CLK)
24. GPIO8(CEO) -> MCP3008 Pin 10(CS/SHDN)
