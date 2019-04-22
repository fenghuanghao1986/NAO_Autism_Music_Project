/*
#include <iostream>
using namespace std;

int main()
{
	int numberOfLanguages;
	cout << "How many programming languages have you used:";
	cin >> numberOfLanguages;
	if (numberOfLanguages < 1)
		cout << "you need to work harder to learn more\n"
		<< "and do better next time.\n";
	else
		cout << "You hired!\n";
	return 0;
}

#include <iostream>
using namespace std;
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char a = 'b';
	int c = 10, d = 10u, e = 10ul, f = 032, g = 0xC;
	cout << a << "\n"
		<< c << "\n"
		<< d << "\n"
		<< e << "\n"
		<< f << "\n";
	double h = 3.14, i = 3.14f, j = 3.14L;
	cout << h << "\n"
		<< i << "\n"
		<< j << "\n";
	system("PAUSE");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char a, d, e, g, h, m, o;
	int b, c, x, f, i, j;
	double k, l, n;
	
	cin >> oct >> i
		>> hex >> j
		>> k
		>> l >> m
		>> n >> o;

	cout << i << endl
		<< j << endl
		<< k << endl
		<< l << endl
		<< n << endl;

	system("PAUSE");
	return 0;

}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int year, month, day, hour, minute, second;
	cout << "please tell me the date and time: ";
	cin >> year >> month >> day >> hour >> minute >> second;
	cout << year << ":" << month << ":" << day << ":" << hour
		<< ":" << minute << ":" << second << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	cout << (654 * 987) << "\n"
		<< ((-55) * (-52)) << "\n"
		<< (3 / 0) << "\n"			// error C2124: divide or mod by zero
		<< (65 / 2.0) << "\n"
		<< (1e10 * 1e20) << endl;	
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	double Pi = 3.14159, r, C, S;
	cout << "please provide 'r' value: \n";
	cin >> r;
	C = Pi * (2 * r);
	S = Pi * (r * r);
	cout << "C = " << C << "\n"
		<< "S = " << S << "\n";
	system("pause");

	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double x;
	cout << "input a float number: \n";
	cin >> x;
	cout << sin(x) << "\n"
		<< cos(x) << "\n"
		<< tan(x) << "\n"
		<< abs(x) << "\n"
		<< ceil(x) << "\n"
		<< floor(x) << endl;
	system("pause");

	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double x, y;
	cout << "please input two numbers x and y, then I compute the x to the power of y: \n";
	cin >> x >> y;
	cout << pow(x, y) << "\n";
	system("pause");

	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	double convertor = 35273.92, mass;
	cout << "provice you ounces: \n";
	cin >> mass;
	mass = mass / convertor;
	cout << ceil(1 / mass) << endl;
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{	
	const double convertor = 0.001;
	double dosage, weightOfMouse, weightOfHuman, amountOfSoda;

	cout << "We are going to talk about a interesting topic today: \n"
		<< "How much dosage of artificial sweets will kill a mouse? \n"
		<< "How much soda you can drink based on the killing dosage for mouse?"
		<< endl;
	cout << "Please input the dosage for mouse you think: \n";
	cin >> dosage;
	cout << "Please input the weight of that mouse: \n";
	cin >> weightOfMouse;
	cout << "Please input your weight: \n";
	cin >> weightOfHuman;
	amountOfSoda = (weightOfHuman * dosage / weightOfHuman) / convertor;
	cout << "You can only drink these amount of soda: " 
		<< amountOfSoda << ", if more than that, it may kill you as well."
		<< endl;
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;

int main()
{
	const double rateOfRise = 0.076;
	double currentSalary, increase, newSalary, monthlyPay;
	int year;
	cout << "We are going to estimate your future salary,\n"
		<< "nwo, tell me about your current year end income: ";
	cin >> currentSalary;
	cout << "Now, tell me how long you will stay in this compay: ";
	cin >> year;
	newSalary = currentSalary * (pow((1 + rateOfRise), year));
	increase = newSalary - currentSalary;
	monthlyPay = newSalary / 12;
	cout << "This is your future year income: $" << newSalary
		<< " after " << year << "years" << "\n"
		<< "Total increases is $" << increase << " each year. \n"
		<< "And your monthly income by that time is: $" << monthlyPay
		<< ". Well done! And good luck to your future! Bye! \n";
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	int maxNum = 300, actualNum, diff;
	cout << "How many people attending this meeting: " << endl;
	cin >> actualNum;
	if (actualNum <= maxNum)
	{
		diff = maxNum - actualNum;
		cout << "Number of people not vailate the rule." << endl
			<< "Based on law, you still can have " << diff
			<< " people atttend." << endl;
	}
	else {
		diff = actualNum - maxNum;
		cout << "Based to law, you should reduce " << diff
			<< " amount of people to start the meeting." << endl;
	}
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	char a;
	cin >> a;
	int b;
	b = (int)a;
	cout << b << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;
	char b;
	b = (char)a;
	cout << b << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;

int main() 
{
	cout << "#include<iostream>\n"
		<< "using namespace std;\n"
		<< "int main()\n"
		<< "{\n"
		<< "int a;\n"
		<< "cout<<\"please input an intergal number\"<<endl;\n"
		<< "cin>>a;\n"
		<< "char b;\n"
		<< "b=(char)a;\n"
		<< "cout<<b<<endl;\n"
		<< "}\n";
		system("pause");
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	char cha;
	cin >> cha;
	if ((cha >= '0') && (cha <= '9'))
		cout << "it is a number" << endl;
	else if ((cha >= 'a') && (cha <= 'z'))
		cout << "it is a lowercase letter" << endl;
	else if ((cha >= 'A') && (cha <= 'Z'))
		cout << "it is a capital letter" << endl;
	else
	{
		int b;
		b = (int)cha;
		cout << "it is a special character with ASCII " << b << endl;
	}
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	float a;
	cout << "Please type a number: ";
	cin >> a;
	if (a >= 0)
		cout << "you input is " << a << " which is greater than 0." << endl;
	else
		cout << "you input is " << a
		<< " which is less than 0. And now I am converting it to positive. "
		<< (-a) << " is the final answer now." << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	float temp, result;
	int conv;
	cout << "Please choose your function: \n"
		<< "Type 1 to convert C to F; \n"
		<< "Type 2 to convert F to C. \n"
		<< "Make you selection now: ";
	cin >> conv;
	cout << "Please type current temperture: " << endl;
	cin >> temp;
	switch (conv)
	{
	case 1:
		result = ((9 * temp) / 5) + 32;
		cout << "Temperture is " << result << " F." << endl;
		break;
	case 2:
		result = (5 * (temp - 32)) / 9;
		cout << "Temperture is " << result << " C." << endl;
		break;
	default:
		break;
	}
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	double a, b;
	cout << "This function is to compare two numbers you put in."
		<< "Please input your two numbers: "
		<< endl;
	cin >> a >> b;
	cout << _Max_value(a, b) << ">" << _Min_value(a, b) << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int x, y, * pi_x = &x, * pi_y = &y;
	cout << "Please input two numbers\n";
	cin >> x >> y;
	cout << pi_x << endl	// this is memory address
		<< pi_y << endl		// this is memory address
		<< *pi_x << endl	// this is variable value
		<< *pi_y << endl	// this is variable value
		<< x << endl		// this is always value
		<< y << endl;		// this is always value
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int x, y, * pi_x = &x, * pi_y = &y, a;
	cout << "Please input two numbers: \n";
	cin >> x >> y;
	x += 1;
	y -= 1;
	a = *pi_x;
	*pi_x = *pi_y;
	*pi_y = a;
	cout << pi_x << endl
		<< pi_y << endl
		<< *pi_x << endl
		<< *pi_y << endl
		<< x << endl
		<< y << endl;
	system("pause");
	return 0;

}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int x, y;
	cout << "Please input two numbers: \n";
	cin >> x >> y;
	int &ref_x = x, &ref_y = y;		// this is reference, then what is the difference between pointer and reference?
	cout << _Max_value(ref_x, ref_y) << "> " << _Min_value(ref_x, ref_y) << endl;
	int a;
	a = x;
	x = y;
	y = a;
	cout << ref_x << endl
		<< ref_y << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int x, y;
	cout << "Please input two number: \n";
	cin >> x >> y;
	const int *pi_y = &y;		//constant pointer
	int* const pi_x = &x;		//pinter constat
	
	*pi_x = 10;							//then what is the difference between these two pointer or constant????
	cout << *pi_x << endl
		<< *pi_y << endl
		<< pi_x << endl
		<< pi_y << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int a[5];
	int *p;
	int i = 0, k = 0, j = 0, max;
	cout << "input five intergers: " << endl;
	cin >> a[0] >> a[1] >> a[2] >> a[3] >> a[4];
	p = &a[0];

	while (i < 5)
	{
		a[i] = *p * 2;
		cout << *p << " ";
		p = p + 1;
		i++;
	}
	cout << endl;
	
	p = p - 1;
	for (j = 0; j < 5; j++)
	{
		cout << *p << " ";
		p = p - 1;
	}
	cout << endl;

	max = a[0];
	for (k = 0; k < 5; k++)
	{
		if (a[k] > max)
			max = a[k];
	}
	cout << "max = " << max << endl;
	system("pause");
	return 0;
	
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	cout << "The default output of the true value is "
		<< true << endl;
	cout << "In order to output the true value, we can write the value as "
		<< boolalpha << true << endl;
	int x, y;
	cout << "please input numbers: " << endl;
	cin >> x >> y;
	bool x_greater_y = false, x_less_y = false, x_equal_y = false;
	if (x < y)
		x_less_y = true;
	else if (x > y)
		x_greater_y = true;
	else
		x_equal_y = true;
	cout << "It is " << x_equal_y << " that x is equal to y. \n"
		<< "It is " << x_greater_y << " that x is greater than y. \n"
		<< "It is " << x_less_y << " that x is less than y."
		<< endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	typedef enum states{ greater_than=0, equal_to=1, less_than=2};
	cout << "Please input two integers " << endl;
	int x, y;
	cin >> x >> y;
	if (x > y)
		cout << greater_than << endl;
	else if (x == y)
		cout << equal_to << endl;
	else
		cout << less_than << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <cctype>
using namespace std;
int main()
{
	char s[30] = "Uinversity of Denver";
	int i;
	char* p_c;
	p_c = &s[0];
	for (i = 0; i < 29; i++)
	{
		*p_c = toupper(*p_c);
		cout << *p_c;
		p_c++;
	}
	cout << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int arr[5][5];
	int i, j;
	for (i = 0; i < 5; i++)
	{
		for (j = 0; j < 5; j++)
		{
			arr[i][j] = 1;
		}
	}
	arr[2][3] = 0;
	cout << "Please input two numbers to see the value in array: \n";
	cin >> i >> j;
	if ((i < 5) && (j < 5))
		cout << arr[i][j] << endl;
	else
		cout << "error!" << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int x, y;
	cout << "please input 2 numbers: " << endl;
	cin >> x >> y;
	cout << "x + y = " << x + y << endl
		<< "x - y = " << x - y << endl
		<< "x * y = " << x * y << endl;
	if (y != 0)
		cout << "x / y = " << x / y << endl
		<< "x % y = " << x % y << endl;			// to find a remainder you must use interger to do the math
	else
		cout << "error!" << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <math.h>
using namespace std;
int main()
{
	int year;
	double a, b, c;
	cout << "Please input a year number, I can tell you if it is lead numer: " << endl;
	cin >> year;
	if (year <= 0)
		cout << "error!" << endl;
	else
	{
		a = year % 4;
		b = year % 100;
		c = year % 400;
		if (a != 0)
			cout << "This is not lead year!" << endl;
		else if (b == 0 && c != 0)
			cout << "This is not lead year!" << endl;
		else
			cout << "This is lead year!" << endl;
	}

	system("pause");
	return 0;
}
*/


/*
#include<iostream>
using namespace std;
int main()
{
	int x, i = 0, m = 0, n = 0, z = 0;
	while (cin >> x)
	{
		i++;
		if (x > 0)
			m = m + 1;
		else if (x == 0)
			z = z + 1;
		else
			n = n + 1;
	}
	if (n > 0)
		cout << "negitave number" << n << endl;
	cout << "total number" << i << endl
		<< "positive number" << m << endl
		<< "number of zero" << z << endl;

	return 0;
}
*/


/*
#include <iostream>
using namespace std;
int main()
{
	double T0[30], T1[4][4], T2[4][4], T[4][4];
	double* p_t = &T0[0];
	int i = 0, j = 0;

	cout << "Please keep inputing numbers untill you cannot type more: " << endl;
	// inputting numbers for future useage
	while (i < 30)
	{
		cin >> T0[i];
		i++;
	}
	cout << p_t << endl;
	cout << "Please check below, to make sure these are the numbers you wanted!" << endl;
	// confirming inputted numbers for next steps
	while (i > 0)
	{
		cout << *p_t;
		p_t++;
		i--;
	}
	cout << endl;
	p_t = p_t - 1;
	cout << p_t << endl;
	system("pause");
	// assign second half of inputs from bottom to top into T1
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			T1[i][j] = *p_t;
			p_t--;
		}
	}
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			cout << T1[i][j] << " ";
		}
		cout << endl;

	}
	cout << endl;
	cout << p_t << endl;
	system("pause");
	p_t = &T0[0];
	// assign first half of inputs from top to bottom to T2
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			T2[i][j] = *p_t; 
			p_t++;
		}
	}
	cout << endl;
	cout << p_t << endl;
	
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			cout << T2[i][j] << " ";
		}
		cout << endl;
	}
	system("pause");

	p_t = &T0[0];
	cout << p_t << endl;
	// calculate T = T1 * T2 for each element
	for (i = 0; i < 4; i++)
	{
		for (j = 0; j < 4; j++)
		{
			T[i][j] = T1[i][j] * T2[i][j];
			cout << T[i][j] << " ";
		}
		cout << endl;
	}
	cout << endl;
	cout << p_t << endl;
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
	int num, maxNum, minNum, anotherNum;
	char choice;
	cout << "please input first number: " << endl;
	cin >> num;
	maxNum = num;
	minNum = num;
	cout << "do you want to input something more? Please enter y or n: " << endl;
	cin >> choice;
	while ((choice == 'Y') || (choice == 'y'))
	{
		cout << "now, you may enter another number: " << endl;
		cin >> anotherNum;
		maxNum = max(num, maxNum);
		maxNum = max(maxNum, anotherNum);
		minNum = min(num, minNum);
		minNum = min(minNum, anotherNum);
		cout << "do you want to input another number: " << endl;
		cin >> choice;
	}

	cout << "The max number of all your inputs is :" << maxNum << endl;
	cout << "The min number of all your inputs is : " << minNum << endl;

	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int i, j, k, m, n;
	for (i = 0; i < 8; i++)
	{
		if (i <= 4) {
			for (j = 0; j < 5 - i; j++)
				cout << " ";
			for (k = 0; k < 2 * i - 1; k++)
				cout << "*";
			cout << endl;
		}
		else
		{
			for (m = 0; m < i - 3; m++)
				cout << " ";
			for (n = 0; n < 15 - i * 2; n++)
				cout << "*";
			cout << endl;
		}
	}
	system("pause");
	return 0;
}
*/

/*
#include <iostream>
using namespace std;
int main()
{
	int i;
	int a, b;
	cout << "input a number: " << endl;
	cin >> a;
	b = a;

	cout << "this is new a: " << endl;
	for (i = 0; i < 16; i++)
	{
		a = a << 1;					// shift a for 1 bit left
		cout << a << endl;
	}

	cout << "this is new b: " << endl;
	for (i = 0; i < 16; i++)
	{
		b = b >> 1;					// shift b for 1 bit right
		cout << b << endl;
	}

	system("pause");
	return 0;
}

*/



#include <iostream>
using namespace std;
int main()
{
	char str1[255], str2[3] = "ff", str3[3] = "fl", str4[3] = "fi", * p1, * p2, * p3, * p4, * temp2, * temp3, * temp4;
	int sum2 = 0, sum3 = 0, sum4 = 0;
	cout << "Please input some some f l i letters: " << endl;
	cin >> str1;
	p1 = str1;
	p2 = str2;
	p3 = str3;
	p4 = str4;

}
