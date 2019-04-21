//F0903701 5090379027 李自勉
//Project 1 Part II
#include<iostream>
#include<time.h>
#include<sstream>
using namespace std;
int size;//皇后个数
int number;//已经放置的皇后的个数
int result;//解数
int rx[100],ry[100];//存储皇后的坐标

bool check( int x,int y );

int main( int argc,char* argv[] )
{
	char* pchar = argv[1];
	stringstream ps;
	ps << pchar;
	ps >> size;
	static bool fail = 0;//标明该次放置是否成功
	number = 0;
	result = 0;
	//初始化坐标，让开始时没有皇后放置
	for( int i = 0;i < size;i++)
		rx[i] = -1;
	clock_t t1,t2;
	t1 = clock( );
	while( ( number > -1 )&&( number < size ) )
	{
		fail = 1;
		if( rx[number] < size - 1 )
		{
			for( int i = rx[number] + 1;i < size;i++)
			{
				if( check( i,number) )
				{
					rx[number] = i;
					ry[number] = number;
					number ++;
					fail = 0;
					break;
				}
			}
		}
		//若没出可放，则回溯
		if( fail )
		{
			rx[number] = -1;
			number --;
		}
		if( number == size )
		{
			result ++;
			rx[number] = -1;
			number --;
		}
	}
	t2 = clock( );
	cout << "The result is " << result << endl
		 << "Time is " << ( t2 - t1 ) << " ms" << endl;
	return 0;
}

bool check( int x,int y )
{
	if( y != 0)
	{
		for( int i = 0;i < number;i++)
		{
			if( ( rx[i] == x ) || ( x - rx[i] == y - ry[i] ) || ( x - rx[i] == ry[i] - y ) )//判断是否在同一条线上
				return 0;
		}
	}
	return 1;
}
