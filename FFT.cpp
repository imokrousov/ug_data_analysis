#include <iostream>
#include <cmath>
#include <vector>
#include <ctime>
#include <queue>
#include <algorithm>
#include <complex>

using namespace std;
const double PI = 3.14159265359;

vector<complex<double> > FFT (vector<complex<double>> a)
{
	int n = a.size();
	vector<complex<double>> y (n); 
	if (n == 1) return a;
	complex<double> wn = {cos(2*PI/n), sin(2*PI/n)};
	complex<double> w = {1,0};
	vector<complex<double>> a0;
	vector<complex<double>> a1;
	for (int i =0 ; i < n/2; i++) 
	{
		a0.push_back(a[2*i]);
		a1.push_back(a[2*i+1]);
	}
	vector<complex<double>> y0 = FFT(a0);
	vector<complex<double>> y1 = FFT(a1);
	for (int k = 0; k < n/2; k++)
	{
		y[k]= y0[k]+w*y1[k];
		y[k+n/2] = y0[k] - w*y1[k];
		w*= wn;
	}
	return y;
}

vector<complex<double> > reverseFFT (vector<complex<double>> a)
{
	int n = a.size();
	vector<complex<double>> y (n); 
	if (n == 1) return a;
	complex<double> wn = {cos(2*PI/n), sin(2*PI/n)}; wn = complex<double>(1,0)/wn;
	complex<double> w = {1,0};
	vector<complex<double>> a0;
	vector<complex<double>> a1;
	for (int i =0 ; i < n/2; i++) 
	{
		a0.push_back(a[2*i]);
		a1.push_back(a[2*i+1]);
	}
	vector<complex<double>> y0 = FFT(a0);
	vector<complex<double>> y1 = FFT(a1);
	for (int k = 0; k < n/2; k++)
	{
		y[k]= (y0[k]+w*y1[k])/complex<double>(n,0);
		y[k+n/2] = (y0[k] - w*y1[k])/complex<double>(n,0);
		w*= wn;
	}
	return y;
}


int main()
{
	vector<complex<double> > Pol=  {{1,0},{3,0},{1,0},{1,0}};
	vector<complex<double> > Fur=  FFT(Pol);
	vector<complex<double> > Ans=  reverseFFT(Fur);
	for (auto x : Ans)
	{
		cout<< x<<endl;
	}
}






