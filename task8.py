#! /usr/bin/python3

print("content-type: text/html")
print()


print('''<style>
pre{
color: black;
font-weight: bold;
font-size: 20px;
}
</style>''')


import cgi
import subprocess as sb

fs = cgi.FieldStorage()

plate_no = fs.getvalue("x")


if plate_no == "KA 05 NB 1786"
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : JAYESH SHAH
    License No : 12432347910
    Make / Model : Kia / Seltos
    Registration Date : 3/1/2017
    Registering Authority : JAYANAGAR , BENGALURU 
    Vehicle Class : MCWG
    Fuel Type : DIESEL
    Engine No : IVK3FRE4538
    Chassis No : HMSURVWVQVJDIF
    Insurance Upto : 5/15/2022
    Fitness Upto : 4/8/2028
    </pre>''')
    print("</body>")

elif plate_no == "MH 04 BP 7108":
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print('''<pre>
    Registration Name : AMAN JAIN
    License No : 10942424321
    Make / Model : HONDA / SHINE
    Registration Date : 1/1/2019
    Registering Authority : THANE WEST , THANE
    Vehicle Class : MCWG
    Fuel Type : PETROL
    Engine No : IVK3N17344738
    Chassis No : HMSFHDSWVQSVWE
    Insurance Upto : 5/13/2024
    Fitness Upto : 5/8/2029
    </pre>''')
    print("</body>")


else:
    print("<body style='padding: 40px;'>")
    print('<h1 style="color:#df405a;" >Output</h1>')
    print("No data available for this number...")
    print("</body>")
