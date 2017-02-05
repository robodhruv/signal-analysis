/*
CPU code for 1D convolution.
*/
#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <ctime>
#include <time.h>
using namespace std;

void init_arr(float *arr, int len)
{
	int i = 0;;
	for (i = 0; i < len; i++) {
		arr[i] = 0.0f;
	}
}

void rand_arr(float *arr, int len)
{
	int i = 0;
	for (i = 0; i < len; i++) {
		arr[i] = (rand() % 1000) * 0.01;
	}
}

clock_t convolve(const float *a, const float *b, float *c, int n)
{
	clock_t startCPU, endCPU;
	int i, j;

	startCPU = clock();

	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			c[i + j] += a[i] * b[j];
		}

	endCPU = clock();

	return endCPU - startCPU;
}

int main()
{
	float *a, *b, *c, *d;
	int m, n = 0;

	printf("\nInput length n:");
	scanf("%d", &n);

	m = 2 * n - 1;

	a = (float*)malloc(sizeof(float) * n);
	b = (float*)malloc(sizeof(float) * n);
	c = (float*)malloc(sizeof(float) * m);

	srand((unsigned int)time(NULL) + rand());

	rand_arr(a, n);
	rand_arr(b, n);
	init_arr(c, m);

	clock_t timeCPU = convolve(a, b, c, n);

	double secCPU = (double)timeCPU / CLOCKS_PER_SEC;
	printf("CPU time used: %.2f", secCPU);
	cout<<endl;

	cout << "Press enter to exit. ";
	getchar();

	free(a);
	free(b);
	free(c);

	return 0;
}
