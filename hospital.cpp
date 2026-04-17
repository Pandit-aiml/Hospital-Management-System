#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

void addPatient(string name, int age, string problem, string weight, string bg, string payment, string doctor) {
    ofstream file("data/patients.txt", ios::app);
    file << name << " " << age << " " << problem << " " << weight << " " << bg << " " << payment << " " << doctor << endl;
    file.close();
}

void viewPatients() {
    ifstream file("data/patients.txt");
    string name, problem, weight, bg, payment, doctor;
    int age;

    while (file >> name >> age >> problem >> weight >> bg >> payment >> doctor) {
        cout << "Name: " << name << " | Age: " << age << " | Problem: " << problem 
             << " | Weight: " << weight << "kg | Blood Group: " << bg 
             << " | Payment: " << payment << " | Doctor: " << doctor << endl;
    }
    file.close();
}

void deletePatient(string targetName) {
    ifstream file("data/patients.txt");
    vector<string> lines;
    string name, problem, weight, bg, payment, doctor;
    int age;

    while (file >> name >> age >> problem >> weight >> bg >> payment >> doctor) {
        if (name != targetName) {
            lines.push_back(name + " " + to_string(age) + " " + problem + " " + weight + " " + bg + " " + payment + " " + doctor);
        }
    }
    file.close();

    ofstream outFile("data/patients.txt", ios::trunc);
    for (const string& line : lines) {
        outFile << line << endl;
    }
    outFile.close();
}

int main(int argc, char* argv[]) {
    if (argc < 2) return 0;

    string command = argv[1];

    if (command == "add" && argc >= 9) {
        addPatient(argv[2], stoi(argv[3]), argv[4], argv[5], argv[6], argv[7], argv[8]);
    }
    else if (command == "view") {
        viewPatients();
    }
    else if (command == "delete" && argc >= 3) {
        deletePatient(argv[2]);
    }

    return 0;
}