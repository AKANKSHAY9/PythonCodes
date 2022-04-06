#include<iostream>
using namespace std;
int main(){
    int a;
    cin>>a;
    int b;
    cin>>b;
    int c;
    cin>>c;
    if(c>b){
        if(b>a){
            cout<<"c is largest number\n";
        }
    } else if(b>c){
        if(c>a){
            cout<<"b is the largest number\n";
        } 
        } else{
            cout<<" a is the largest number\n";
        }
}