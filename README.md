# TCP_IP_communication_python

Python scripts to communicate with RPI over TCP/IP (LAN).
RPI and PC can be server and client interchangeably.
Client sends the files to the server. 
Multiple files can be sent from current directory of client. 
On the server, similar files with same content will be created in the current directory. 

Client:
CLient sends the data in the following format.
new <filename> <content>\nnew <filename> <content>\n......

Server:
The server reads all the data received into a buffer. 
Parses the data in the buffer. 
Creates similar files and writes the corresponding data into it.

This project is still in the initial stages. 

TODO:
1.  Need to modularize the code.
2.  Need to implement the following subroutines
        parser.
        file creation. 
3.  Need to implement data recepetion, parser and file_creation in threads. 
4.  Need to implement the same in Objective Python.

