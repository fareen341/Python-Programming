<h1>If else checking condition short way</h1>
<pre>
If the given condn is marks should be less than or equal to 350 and greater than or equal to 450
then:
print(350<=marks<=450)

instead of writing:
marks <=350 and marks >=450
</pre>

<h1>Random Module</h1>
<pre>
import random

#random() : to get randome values between 0 and 1.
x=random.random()

#randint() : to get random intigers(eg to get random number in dice)
x=random.randint(1,6)   #return random intiger value, including 1 and 6
print(x)

#randrange() : returns a number between 3 (included) and 9 (not included), 9-1=8, so 3 to 8
print(random.randrange(3, 9))

#unique() to get the random floating point value between 1 and 10 use uniform
x=random.uniform(1,10)   #random floating values between 1 and 10
x=random.uniform(0,1)   #random floating value between 0 and 1, it can be like 0.603094.. etc

#choice() : picks random values from a list of value
vehicle=['car','bike','bus']
print(random.choice(vehicle))

#choices() : here it will pick choices in the given list based on the k value provided
vehicle=['car','bike','bus']
print(random.choices(vehicle, k=10))

#adding weight in choices
vehicle=['red','blue','green']
print(random.choices(vehicle, weights=[18,18,2], k=10))  #red and blue has 18 chance to be randomly selected, but green has only 2 chance to get randomly secelted.

#shuffle()
deck = list(range(1, 53))
random.shuffle(deck)    #this will randomly shuffle the elements
print(deck)

#sample() : gives the unique values no number will repeat
hand = random.sample(deck, k=5)         #get the 5 unique values
print(hand)
</pre>


<h1>Exception</h1>

![exception](https://user-images.githubusercontent.com/59610617/146680494-251995ff-b7cc-4e07-a2da-c456c9622378.png)

<h1>UPLOADING CSV DATA TO MYSQL DATABASE</h1>
<pre>
1)Create database.
2)Use database;
3)Write code in proper format
def csv_sql(request):
    df = pd.read_csv('D:/userdata.csv')
    x=df.head()
    print(type(x))
    print(x)
    # format: mysql://user:password@host/db
    engine = create_engine('mysql://root:@localhost/csvdb')
    x.to_sql('userdatatable', con=engine)
    return HttpResponse("done")
   
Output: userdatatable is a table name, we dont need to create table just create database and use it, then whatever name we provide in the to_sql parameter that name will be the name of the table.
Note: if the file is xlsx then change pd.read_xlxs
link followed: https://syntaxbytetutorials.com/sql-import-excel-file-to-table-with-python-pandas/
</pre>
