#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#------------------------------------------------------------------------------
# Author : Enoch Luis S Catuncan
# Date Created : November 5th 2022
#------------------------------------------------------------------------------
import socket
from tkinter import *
from tkinter import messagebox

class Server:
    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(("86.36.42.136", 15112))

    # This function was copied and pasted from HW7
    # This helper function creates the 512 character long block from message
    def createBlock(self, message):
        # Find length of message and ensure it is 3 digits long
        messageLength = str(len(message))
        while len(messageLength) != 3:
            messageLength = "0" + messageLength
        # Create initial block
        block = message + "1" + messageLength

        # Keep adding copies of message to the block 
        # until it is 512 characters long
        while (len(block) < 512):
            # If next copy will make the block go over 512 characters
            if (len(block + message) > 512):
                # Add zeros in between message length and the rest of block
                for i in range(512 - len(block)):
                    block = block[:len(block) - 3] + "0" + \
                    block[len(block) - 3:]
            else:
                # Add copy in between message length and the rest of block
                block = block[:len(block) - 3] + message + \
                block[len(block) - 3:]
        return block

    # This function was copied and pasted from HW7
    def leftRotate(self, x, c):
        return (x << c) & 0xFFFFFFFF | (x >> (32 - c) & 0x7FFFFFFF >> (32 - c))

    # This function was copied and pasted from HW7
    # This helper function creates the message digest
    def createMessageDigest(self, M):
        s = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 5, 
        9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 5, 9, 14, 20, 4, 11, 16, 23, 
        4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 6, 10, 15, 21, 6, 10, 
        15, 21, 6, 10, 15, 21, 6, 10, 15, 21 ]
        K = [0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee, 0xf57c0faf, 
        0x4787c62a, 0xa8304613, 0xfd469501, 0x698098d8, 0x8b44f7af, 
        0xffff5bb1, 0x895cd7be, 0x6b901122, 0xfd987193, 0xa679438e, 
        0x49b40821, 0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa, 
        0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8, 0x21e1cde6, 
        0xc33707d6, 0xf4d50d87, 0x455a14ed, 0xa9e3e905, 0xfcefa3f8, 
        0x676f02d9, 0x8d2a4c8a, 0xfffa3942, 0x8771f681, 0x6d9d6122, 
        0xfde5380c, 0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70, 
        0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05, 0xd9d4d039, 
        0xe6db99e5, 0x1fa27cf8, 0xc4ac5665, 0xf4292244, 0x432aff97, 
        0xab9423a7, 0xfc93a039, 0x655b59c3, 0x8f0ccc92, 0xffeff47d, 
        0x85845dd1, 0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1, 
        0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391]

        a0 = 0x67452301
        b0 = 0xefcdab89
        c0 = 0x98badcfe
        d0 = 0x10325476
        A = a0
        B = b0
        C = c0
        D = d0
        for i in range(64):
            if (i <= 15):
                F = (B & C) | ((~B) & D)
                F = F & 0xFFFFFFFF
                g = i
            elif (i <= 31):
                F = (D & B) | ((~D) & C)
                F = F & 0xFFFFFFFF
                g = ((5 * i) + 1) % 16
            elif (i <= 47):
                F = B ^ C ^ D
                F = F & 0xFFFFFFFF
                g = ((3 * i) + 5) % 16
            elif (i <= 63):
                F = C ^ (B | (~D))
                F = F & 0xFFFFFFFF
                g = (7 * i) % 16
            dTemp = D
            D = C
            C = B
            B = B + self.leftRotate((A + F + K[i] + M[g]), s[i])
            B = B & 0xFFFFFFFF
            A = dTemp
        a0 = (a0 + A) & 0xFFFFFFFF
        b0 = (b0 + B) & 0xFFFFFFFF
        c0 = (c0 + C) & 0xFFFFFFFF
        d0 = (d0 + D) & 0xFFFFFFFF
        return str(a0) + str(b0) + str(c0) + str(d0)

    # This function was copied and pasted from HW7
    # This function carries out CRA to log a user into the server
    def login(self, username, password):
        # Send username to server and receive challenge from server
        self.socket.send(b"LOGIN " + username.encode("utf-8") + b"\n")
        challenge = self.socket.recv(512).decode()
        # Create message string consisting of password and challenge string
        message = password + challenge.split()[2]
        block = self.createBlock(message)

        M = [0 for i in range(16)]
        # Go through each 32-character chunk in the block
        for i in range(16):
            ASCIISum = 0
            # For each 32-character chunk, calcualte the sum of ASCII values
            # of each character in the chunk and store it in M
            for j in range(32):
                ASCIISum += ord(block[(32*i) + j])
            M[i] = ASCIISum

        # Calculate message digest and send it to server
        messageDigest = self.createMessageDigest(M)
        self.socket.send(b"LOGIN " + username.encode("utf-8") + b" " +
        messageDigest.encode("utf-8") + b"\n")
        # Return True if message digest is correct
        if (self.socket.recv(512).decode() == "Login Successful\n"):
            return True
        return False
    
    # This function was copied and pasted from HW7
    # This function returns a list of users for the game (only friends work)
    def getUsers(self):
        self.socket.send(b"@friends")
        # Get the size of the server message
        size = int(self.socket.recv(6).decode()[1:]) - 6
        # Get the rest of the server message
        friends = self.socket.recv(size).decode()
        # Keep receiving until size matches the number of characters received
        while (size != len(friends)):
            friends += self.socket.recv(size).decode()
        return friends.split("@")[3:]

    # This function gets the user's score for a specific level
    def getUserScore(self, username, level):
        toServer = "@getuserscoresrqst@" + username
        size = str(len(toServer) + 6)
        while len(size) != 5:
            size = "0" + size

        self.socket.send(b"@" + size.encode("utf-8") + toServer.encode("utf-8"))
        size = int(self.socket.recv(6).decode()[1:]) - 6
        userScores = self.socket.recv(size).decode()
        while size != len(userScores):
            userScores += self.socket.recv(size).decode()

        if size == 0:
            return size
        else:
            userScores = userScores.split("@")[1:]
            return int(userScores[level + 1])

    # This function updates a user's score for a specific level
    def updateUserScore(self, username, level, score):
        newUserScores = []
        for i in range(5):
            newUserScores += [self.getUserScore(username, i)]
        newUserScores[level] = int(score)
        toServer = "@updateuserscores@" + username + "@" + \
        str(newUserScores[0]) + "@" + str(newUserScores[1]) + "@" + \
        str(newUserScores[2]) + "@" + str(newUserScores[3]) + "@" + \
        str(newUserScores[4]) + "@"

        print(toServer)

        size = str(len(toServer) + 6)
        while len(size) != 5:
            size = "0" + size

        print("SENDING")

        self.socket.send(b"@" + size.encode("utf-8") + toServer.encode("utf-8"))

        print(self.socket.recv(1024).decode()[7:])
        return "scoresupdated" == "scoresupdated" 

# This class was copied and pasted from HW8
class loginWindow:
    def __init__(self, window, server, game):
        # Setup server, window and main frame
        self.server = server
        self.root = window
        self.root.eval("tk::PlaceWindow . center")
        self.root.lift()
        self.root.title("Login Window")
        self.root.geometry("230x130")
        self.mainFrame = Frame(self.root)
        self.mainFrame.pack()
        self.game = game

        # Setup labels and entry boxes
        self.usernameLabel = Label(self.mainFrame, text="Username")
        self.usernameEntry = Entry(self.mainFrame, width=20)
        self.passwordLabel = Label(self.mainFrame, text="Password")
        self.passwordEntry = Entry(self.mainFrame, width=20, show="*")
        self.enterButton = Button(self.mainFrame, text="OK", width=3, 
        height=1, command=self.login)
        self.usernameLabel.pack()
        self.usernameEntry.pack()
        self.passwordLabel.pack()
        self.passwordEntry.pack()
        self.enterButton.pack()
        self.root.mainloop()

    # This function was copied and pasted from HW8
    def login(self):
        # Get entries from entry boxes
        username = self.usernameEntry.get()
        # Use login function from hw 7 to login to server
        # If login successful, open main window
        if self.server.login(username, self.passwordEntry.get()):
            messagebox.showinfo(title="Log in successful", 
            message="Welcome " + username)
            self.game.username = username
            self.game.loggedin = True
            self.root.destroy()
        else:
            messagebox.showerror(title="Unable to login", 
            message="Incorrect username/password")