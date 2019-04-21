//F0903701 5090379027 ������
//Project 1 Part II
#include<iostream>
#include<time.h>
#include<sstream>
using namespace std;
int size;//�ʺ����
int number;//�Ѿ����õĻʺ�ĸ���
int result;//����
int rx[100],ry[100];//�洢�ʺ������

bool check( int x,int y );

int main( int argc,char* argv[] )
{
	char* pchar = argv[1];
	stringstream ps;
	ps << pchar;
	ps >> size;
	static bool fail = 0;//�����ôη����Ƿ�ɹ�
	number = 0;
	result = 0;
	//��ʼ�����꣬�ÿ�ʼʱû�лʺ����
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
		//��û���ɷţ������
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
			if( ( rx[i] == x ) || ( x - rx[i] == y - ry[i] ) || ( x - rx[i] == ry[i] - y ) )//�ж��Ƿ���ͬһ������
				return 0;
		}
	}
	return 1;
}
