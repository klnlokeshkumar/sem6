#include <bits/stdc++.h>
using namespace std;

string ceaserEncryption(string message, int key){
    string cipherText = "";
    for(int ch : message){
        cipherText += (ch - 'a' + key)%26 + 'A';
    }
    return cipherText;
}

string ceaserDecryption(string cipherText, int key){
    string plainText = "";
    for(int ch : cipherText){
        // if the modulo arthimetic gives a negative number we need to add 26 to it.
        int temp = (ch - 'A' - key)%26;
        if(temp < 0) plainText += temp + 26 + 'a';
        else plainText += temp + 'a';
    }
    return plainText;
}

int main(){
    string message;
    int key;
    cout << "Enter the plain test: ";
    cin >> message;
    cout << "Enter the Key(k): ";
    cin >> key;
    string cipherText = ceaserEncryption(message, key);
    cout << "cipher text: " << cipherText << endl;
    string plainText = ceaserDecryption(cipherText, key);
    cout << "Plain text: " << plainText << endl;
    return 0;
}