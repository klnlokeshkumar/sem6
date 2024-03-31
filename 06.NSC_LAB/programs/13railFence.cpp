#include <bits/stdc++.h>
using namespace std;

string encryption(string message, int rows) {
    vector<vector<char>> rfArray(rows, vector<char>(message.length(), '-'));
    int i = 0;
    bool down = false;  // Initialize direction to move
    for (int j = 0; j < message.length(); j++) {
        rfArray[i][j] = message[j];
        // Change direction if at the top or bottom rail
        if (i == 0 || i == rows - 1) {
            down = !down;
        }
        // Move to the next row depending on direction
        if (down) {
            i++;
        } else {
            i--;
        }
    }
    // Construct the ciphertext from the rail fence array
    string result = "";
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < message.length(); j++) {
            if (rfArray[i][j] != '-') {
                result += rfArray[i][j];
            }
        }
    }
    return result;
}

string decryption(string cipherText, int rows) {
    vector<vector<char>> rfArray(rows, vector<char>(cipherText.length(), '-'));
    int i = 0;
    bool down = false;  // Initialize direction to move
    for (int j = 0; j < cipherText.length(); j++) {
        rfArray[i][j] = '*';
        // Change direction if at the top or bottom rail
        if (i == 0 || i == rows - 1) {
            down = !down;
        }
        // Move to the next row depending on direction
        if (down) {
            i++;
        } else {
            i--;
        }
    }
    
    // replace stars with cipher characters
    int k = 0;
    for(int i = 0; i < rows; i++){
        for(int j = 0; j < cipherText.length(); j++){
            if(rfArray[i][j] == '*') rfArray[i][j] = cipherText[k++];
        }
    }
    
    // Construct the plain text from the rf array
    string result = "";
    i = 0;
    down = false;  // Initialize direction to move
    for (int j = 0; j < cipherText.length(); j++) {
        result += rfArray[i][j];
        // Change direction if at the top or bottom rail
        if (i == 0 || i == rows - 1) {
            down = !down;
        }
        // Move to the next row depending on direction
        if (down) {
            i++;
        } else {
            i--;
        }
    }
    return result;
}

int main() {
    string message;
    int rows;
    cout << "Enter message: ";
    getline(cin, message);  // Read the whole line including spaces
    cout << "Enter the number of rows: ";
    cin >> rows;
    string cipherText = encryption(message, rows);
    cout << "CipherText: " << cipherText << endl;
    string plainText = decryption(cipherText, rows);
    cout << "Plain text: " << plainText << endl;
    return 0;
}
