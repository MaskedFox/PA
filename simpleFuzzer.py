import socket
import random
import sys
import time
import requests


#DONE: Will first test that everything works as expected, then:
#DONE:: mutate data
#DONE: send mutated data, once without a looop
#DONE: Need to add increment of mutated data
#DONE: add loop if neccesary
#DONE: Send mutated Data w Loop
#DONE: Stop fuzing user-agent and fuzz parameters,for it:
#DONE: Change url, add "/actions"
#DONE: Change GET to POST and add data=payload
#DONE: Add random.seed()
#TODO: Need to add try and exception to catch crashes, encoding issues, other requests possible issues 
#REFERENCE: https://stackoverflow.com/questions/14267452/iterate-over-individual-bytes-in-python-3


class RequestFuzzer:

    def __init__(self):
        # Setting url, Session
        self.url = "http://localhost:5000/actions"
        self.s = requests.Session()

    def add_to_corpus(self):
        # Setting variables to fuzz
        self.fuzz1 = b"OFFICE-THING"
        self.fuzz2 = b"192.168.1.1"
        self.fuzz3 = b"8.8.8.8"
        self.fuzz4 = b"Submit"
        self.fuzz5 = b"Windows"

    def fuzz(self,incrementLength, seedNumber):
        # Incrementing data
        self.fuzz5 = self.fuzz5 * random.randrange(1, 1000)#incrementLength

        #Seed Number
        random.seed(seedNumber)

        # Creating while True loop to create random mutated data
        # and to send the new created data until the Loop its False
        while True:

            # Converting fuzz1 data to bytesarray to later iterate over and change 
            # each character on the bytearray string to a random character. I didnt used bytes because its not mutable
            # Since bytearrays were giving me issues i changed to List
            self.mutatedData = bytearray(self.fuzz5)
            for char in range(len(self.mutatedData)):
                self.mutatedData[char] = int(random.randrange(16, 127))

            # Converting bytearray to bytes
            self.mutatedData = bytes(self.mutatedData)

            # Calling send_fuzzed, to send the data within the loop
            self.send_fuzzed()

            # Printing payload sent and response status
            self.print_payload()

    def send_fuzzed(self):
        # Setting payload to send as POST parameters
        self.payload = {"hostname":self.fuzz1,"hubIp":self.fuzz2,"dnsServer":self.fuzz3, "btnSubmit":self.fuzz4}

        # POST request
        self.req = requests.Request("POST", self.url, data=self.payload)
        self.prepped = self.req.prepare()

        # Fuzzing headers
        self.prepped.headers["user-agent"] = self.mutatedData

         # Send our fuzzed data
        self.response = self.s.send(self.prepped)

        # Waiting 5 secs before sending next packet
        #time.sleep(1)

    def print_payload(self):
        # Printing the payload im sending and the response status code
        print("Payload Sent: {}".format(self.mutatedData))
        #print("Response Status and content: {}".format(self.response.status_code))
        print("")


if __name__ == "__main__":
    rf = RequestFuzzer()
    # Generate request - add to fuzzer
    rf.add_to_corpus()
    # the first argument is the number to increment the data by and the second 
    # arg is the random.seed(#)
    rf.fuzz(100, 1)
    rf.send_fuzzed()
