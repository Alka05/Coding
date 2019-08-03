khush@khush:~$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> var12 = "hi"
>>> var13 = float("hi"
... python
  File "<stdin>", line 2
    python
         ^
SyntaxError: invalid syntax
>>> var12 = "hi"
>>> var13 = float("hi")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: hi
>>> var23 = 2.9
>>> var24 = int ( var23)
>>> 
>>> var24=int(2.9)
>>> print var24
2
>>> var34 = 25
>>> var35 = str(25)
>>> print var35
25
>>> print var34
25
>>> var45 = 3.5
>>> var46 = str(var45)
>>> print var46
3.5
>>> var56 = "yoo"
>>> var57 = int(var56)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'yoo'
>>> 
>>> 


khush@khush:~$ pythonn


Command 'pythonn' not found, did you mean:

  command 'python0' from snap python0 (0.9.1)
  command 'python' from deb python3
  command 'python' from deb python
  command 'python' from deb python-minimal
  command 'python2' from deb python-minimal
  command 'python3' from deb python3-minimal

See 'snap info <snapname>' for additional versions.

khush@khush:~$ 
khush@khush:~$ python
Python 2.7.15rc1 (default, Nov 12 2018, 14:31:15) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> raw_input
<built-in function raw_input>
>>> user_input = raw_input("yoooo")
yoooo
>>> user_input = raw_input(25)
25
>>> Example 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Example' is not defined
>>> 
>>> number1 = raw_input("200"
... number1 = raw_input("200")
  File "<stdin>", line 2
    number1 = raw_input("200")
          ^
SyntaxError: invalid syntax
>>> number1 = raw_input("20")
20
>>> number1 = raw_input(20)
20
>>> 
>>> number2 = raw_input("29")
29
>>> 
>>> number3 = int(number2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: ''
>>> number3 = int(29)
>>> print number3
29
>>> 
>>> 
>>> 
>>> number_x = raw_input("28")
28
>>> number_y = raw_input("24")
24

