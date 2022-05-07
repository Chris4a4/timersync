# PRE-REQUISITES:

LiveSplit Program: <https://livesplit.org/downloads/>
LiveSplit Server Component: <https://github.com/LiveSplit/LiveSplit.Server>
Python: <https://www.python.org/downloads/>
Port-Forwarding set up for the amount of timers to be used (up to 5)

This Python file works in tandem with LiveSplit Server Component to connect two LiveSplit clients together via a
host's public IP address.

Both Clients will need the LiveSplit Server Component installed.

This program can be used to link up to 5 timers together. 


# PORTS:

Ports used by each timer is static and should be as follows:

Timer 1: Port 16834
Timer 2: Port 16835
Timer 3: Port 16836
Timer 4: Port 16837
Timer 5: Port 16838


# PORT-FORWARDING:

Host/Sender must set up Port-Forwarding before used

Port-Forwarding is different per router, research setup specifics for router being used
Make sure to forward each port intended to be used, and that they match the port number in the LiveSplit Timer


# SETUP:

## Host/Sender:

Open LiveSplit > Right Click > Edit Layout > + > Control > LiveSplit Server
Layout Settings > LiveSplit Server (16834) (THIS IS DEFAULT FOR TIMER 1 BUT PORT NUMBER MUST BE CHANGED FOR SUBSEQUENT TIMERS)
Right click timer > Control > Start Server (THIS MUST BE DONE EVERY TIME LIVESPLIT IS OPENED)

## Receiver:

Open LiveSplit > Right Click > Edit Layout > + > Control > LiveSplit Server
Layout Settings > LiveSplit Server (16834) (THIS IS DEFAULT FOR TIMER 1 BUT MUST BE CHANGED FOR SUBSEQUENT TIMERS) 
Right click timer > Control > Start Server (THIS MUST BE DONE EVERY TIME LIVESPLIT IS OPENED)
Open Settings.txt > Enter the host's public IP and the amount of timers to be used > Run Python file

Connection is now established and timers are linked until LiveSplit is closed


# REPEATED USE:

Upon Reopening LiveSplit, connection must be re-established by both Host/Sender and Receiver re-starting LiveSplit Server.
Receiver must also re-start the Python File.
