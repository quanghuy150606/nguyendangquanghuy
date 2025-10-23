#include<iostream>
#include<stdlib.h>
#include<ctime>
using namespace std;

void sinhmang(int a[], int n)
{
    srand(time(0)); // Sinh các ph?n t? ng?u nhiên m?i l?n ch?y
    for (int i = 0; i < n; i++) {
        cout << "Dang sinh cac phan tu ngau nhien: ";
        a[i] = rand() % 100 + 1; 
        cout << a[i] << endl;
    }
}

void hienthi(int a[], int n)
{
    cout << "In cac phan tu cua mang: " << endl;
    for (int i = 0; i < n; i++)
        cout << a[i] << "\t";
    cout << endl;
}

// S?p x?p theo thu?t toán d?i ch? tr?c ti?p
void sx_doichott(int a[], int n)
{
    int i, j, tg;
    for (i = 0; n - 1; i++) {
        for (j = i + 1; j < n; j++) {
            if (a[j] < a[i]) {
                tg = a[i];
                a[i] = a[j];
                a[j] = tg;
            }
        }
    }
}

void chontt(int a[], int n)
{
    int vtmin, i, j, tg;
    for (i = 0; n - 1; i++) {
        vtmin = i;
        for (j = i + 1; j < n; j++) {
            if (a[j] < a[vtmin]) {
                vtmin = j;
            }
        }
        // Hoán d?i a[i] v?i a[vtmin]
        tg = a[i];
        a[i] = a[vtmin];
        a[vtmin] = tg;
    }
}

// Cài d?t thu?t toán s?p x?p chèn tr?c ti?p
void chentt(int a[], int n)
{
    int i, vtchen;
    int x; // Luu l?i giá tr? c?a a[i], tránh b? ghi dè
    for (i = 1; i < n; i++) {
        x = a[i];
        vtchen = i - 1;
        while ((vtchen >= 0) && (a[vtchen] > x))
        {
            // D?i các ph?n t? sang ph?i
            a[vtchen + 1] = a[vtchen];
            vtchen--;
        }
        a[vtchen + 1] = x; // Chèn a[i] vào dúng v? trí c?a nó
    }
}
void bulbleSort(int a[], int n)
{
    int i, j, tg;
    for (i = 0; i < n - 1; i++)
    
        for (j = n - 1; j > i; j--)
        {
            if (a[j] < a[j - 1])
            {
                tg = a[j];
                a[j] = a[j - 1];
                a[j - 1] = tg;
            }
        }

}

int main()
{
    int n;
    cout << "Nhap vao so n= "; cin >> n;
    int a[100];
    cout << "Sinh mang ngau nhien: " << endl;
    sinhmang(a, n);
    hienthi(a, n);
    cout << "\nMang sau khi sap xep la: " << endl;
    //sx_doichott(a,n);
    //chontt(a,n);
    chentt(a, n);
    hienthi(a, n);
    bulbleSort(a, n);
}
