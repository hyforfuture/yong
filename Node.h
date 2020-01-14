//This is a template class to realize Linklist structure.
//Created data: 2020/1/11
//Last modified: 2020/1/14
//Author: ÓÂÐ¡»¢
#pragma once
#ifndef NODE_H
#define NODE_H
#include<iostream>
#include"Link_list.h"
//=========================================================================================
//This is the declaration of "Node".

using std::ends;
using std::ostream;

template<class T>
class Node;

template<class T>
ostream &operator <<(ostream &os, const Node<T> &sample)
{
	os << sample.data;
	return os;
}

template <class T>
class Node
{
	friend class Link_list<T>;
private:
	T data;
	Node<T> *next;
public:
	Node();
	Node(const T &sample);
	Node(Node<T> &sample);
	T getData() { return data; }
	Node<T>* getNext() { return next; }
	Node<T> &operator=(const Node<T> &sample);
	Node<T> operator+(const Node<T> &sample);
	Node<T> operator-();
	Node<T> operator-(const Node<T> &sample);
	Node<T> *operator->();
	friend ostream & operator << <T>(ostream &os, const Node<T> &sample);
};

//================================================================================================
//This is the definition of "Node".

template<class T>
Node<T>::Node()
{
	next = NULL;
}

template<class T>
Node<T>::Node(const T &sample)
{
	data = sample;
	next = NULL;
}

template<class T>
Node<T>::Node(Node<T> &sample)
{
	data = sample.data;
	next = NULL;
}

template<class T>
Node<T> &Node<T>::operator=(const Node &sample)
{
	data = sample.data;
	return *this;
}

template<class T>
Node<T> Node<T>::operator+(const Node &sample)
{
	Node<T> temp(data + sample.data);
	return temp;
}

template<class T>
Node<T> Node<T>::operator-   ()
{
	Node<T> temp(-data);
	return temp;
}

template<class T>
Node<T>* Node<T>::operator->()
{
	return this;
}

template<class T>
Node<T> Node<T>::operator-(const Node<T> &sample)
{
	Node<T> temp(data - sample.data);
	return temp;
}


#endif 
