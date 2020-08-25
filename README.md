# Math Library

this is a math library written in python. You can create a math expression containing numbers, variables and functions. You can also set a value for each variable. You can get the deriative of any expression with this library and finaly you can add your own function to the library from client side without adding code to the library.<br/>

## TODO
1- adding integral ability<br/>
2- adding more predefined functions.<br/>
3- adding a parser so users can use a more math friendly interface.<br/>
<br/>

## Test
for running the testcases you only need to run the following command.<br/>
python3 testcase.py<br/>

there are 9 tests in this file and each test will print one final value.<br/>
test 1: 5*(x^2)+2 , x=2 => result = 22<br/>
test 2: 5*(x^2)+2+y , x=2 , y=3 => result = 25<br/>
test 3: 5*(x^2)+2+y , deriative based on y => result = 1<br/>
test 4: 5*(x^2)+2+y , deriative based on x , x=2 => result = 20<br/>
test 5: 5*(x^2)+2+y , deriative based on x , deriative based on x => result = 10<br/>
test 6: sin(5*(x^2)+2+y) , x=2, y=3 => result = sin(25) = -0.13235175009<br/>
test 7: sin(5*x+2) , deriative based on x , x=2 => result = 5*(cos(12)) = 4.21926979366<br/>
test 8: (func*x)+5 , func=5*(x^2)+2+y , deriative based on x , x=3 , y=10 => result = 5(x^3)+2x+yx+5 = 15(x^2)+2+y = 135+2+10 = 147<br/>
test 9: func(x,y) , func=5*(x^2)+2+y , y=3x , x=3 => result = 5(x^2)+2+3x = 45+2+9 = 56<br/>

