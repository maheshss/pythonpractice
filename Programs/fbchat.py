import fbchat
from getpass import getpass
username = str(raw_input("Username:mssaboo "))
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in xrange(no_of_friends):
    name = str(raw_input("Name:Jesal Kotak "))
    friends = client.getUsers(name)  # return a list of names
    friend = friends[0]
    msg = str(raw_input("Message:Hi "))
    sent = client.send(jesaldk, msg)
    if sent:
        print("Message sent successfully!")







