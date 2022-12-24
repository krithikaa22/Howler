print("Hello there, you have a task to do, remember?\nSo, solve this and immediately check your schedule without procrastinating! :)")

"""The main idea is to get an input and generate a certain math problem and then based on the answer,
we'll either ask them to try again or throw them into an infinite loop of annoying reminders.
Depending on the redirectional feasi, we can simply cut the loop randomly, that's not an issue ig."""

inp=int(input("\nEnter a random whole number less than 10:"))

if inp%2==0:
    a=inp/2
    b=(inp/2)+5
    n=a*b
    print("What is",a,"times",b,"=?")
    answer=float(input())
    while(True):
        if answer==n:
            print("Well done!\nNow please don't ignore this notification and proceed to finish off the task you put this reminder for!")
        else:
            print("Oops! Let's try again:")
            answer=float(input())

else:
    a=(inp+1)/2
    b=inp+6
    n=b-a
    print("What is",b,"minus",a,"=?")
    answer=float(input())
    while (True):
        if answer == n:
            print("Well done!\nNow please don't ignore this notification and proceed to finish off the task you put this reminder for!")
        else:
            print("Oops! Let's try again:")
            answer = float(input())
















