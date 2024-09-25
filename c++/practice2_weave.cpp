// Weave a linked list
#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Node {
public:
    int val;
    Node* next; 
    Node(int e): val(e), next(nullptr) {}
    Node(int e, Node* n): val(e), next(n) {}
};

class LinkedList {
public:
    Node* head;
    int size;
    LinkedList(): head(nullptr), size(0) {}
    LinkedList(vector<int>& l) {
        head = new Node(l[0]);
        size = l.size();
        Node* curr = head;
        for (int i = 1; i < size; ++i) {
            curr->next = new Node(l[i]);
            curr = curr->next;
        }
    }

    int is_empty() {
        return (size == 0);
    }

    void append(int d) {
        Node* end = new Node(d);
        if (head == nullptr) {
            head = end;
            return;
        }
        Node* curr = head;
        while (curr->next != nullptr) {
            curr = curr->next;
        }
        curr->next = end;
    }

    void print() {
        Node* curr = head;
        string out = "";
        while (curr != nullptr) {
            out += to_string(curr->val);
            curr = curr->next;
            if (curr != nullptr)
                out += "->";
        }
        cout << out << endl;
    }
};

Node* weave(Node* head) {
    // TODO
    // return the head of the weaved linked list
}

int main(int argc, char* argv[]) {
    if (argc > 1) {
        vector<int> v;
        for (int i = 1; i < argc; ++i) {
            v.push_back(stoi(argv[i]));
        }
        LinkedList l(v);
        weave(l.head);
        l.print();
    }
}
