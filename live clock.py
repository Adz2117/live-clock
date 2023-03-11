#we want to make a live clock with datetime
while True:
#importing datetime library
    from datetime import datetime
    import time
#we areceive now date and time and define that for system
    y=datetime.today().year
    mm=datetime.today().month
    d=datetime.today().day
    h=datetime.today().hour
    m=datetime.today().minute
    s=datetime.today().second
#for beauty our code we use 0 before x<10 
#we print date and time we 1 second slepping
#because we use while true we have live clock now
    if mm <10:
        print("date:",y,': ','0',mm,':',d,"time:" ,h,':',m,':',s)
        time.sleep(1)
    else:
        print("date:",y,': ',mm,':',d,"time:" ,h,':',m,':',s)
        time.sleep(1)

