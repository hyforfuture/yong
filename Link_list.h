//This is a template class to realize Linklist structure.
//Created data: 2020/1/11
//Last modified: 2020/1/14
//Author: ÓÂÐ¡»¢
#pragma once
#ifndef LINK_LIST_H
#define LINK_LIST_H
#include<iostream>
#include"Node.h"
//================================================================================================
//This is the declaration of "Link_list".

using std::ostream;
using std::ends;
using std::cerr;

template<class T>
class Link_list;

template<class T>
class Node;

template<class T>
ostream &operator<<(ostream &os, const Link_list<T> &sample)
{
	Node<T> *p = sample.first;
	for (int i = 0; i < sample.num; ++i)
	{
		os << p->getData() << ends;
		p = p->getNext();
	}
	return os;
}

template<class T>
class Link_list
{
private:
	Node<T>* first;
	int num;
public:
	Link_list();
	~Link_list();
	Node <T>* getFirst();
	int getNum();
	bool isEmpty();
	Node<T> *locate(int index);
	bool append(const T &sample);
	int search(const T &sample, int start = 0);
	bool insert(const T& sample, int index);
	bool erase(int index);
	void makeEmpty();
	friend ostream &operator<< <T>(ostream &os, const Link_list<T> &sample);
};

//================================================================================================
//This is the definition of "Link_list".

template<class T>
Link_list<T>::Link_list()
{
	num = 0;
	first = NULL;
}

template<class T>
Link_list<T>::~Link_list()
{
	if (num == 0)return;
	else
	{
		Node<T> *p = first, *q = p->next;
		for (int i = 0; i < num; ++i)
		{
			delete p;
			p = q;
			if (p->next != NULL)q = p->next;
		}
		num = 0;
	}
}

template<class T>
Node <T>* Link_list<T>::getFirst()
{
	return first;
}

template<class T>
int Link_list<T>::getNum()
{
	return num;
}

template<class T>
bool Link_list<T>::isEmpty()
{
	return (num == 0);
}

template<class T>
Node<T> *Link_list<T>::locate(int index)
{
	Node<T> *p = first;
	if (index >= 0 && index < num)
	{
		for (int i = 0; i < num; ++i)
		{
			p = p->next;
		}
		return p;
	}
	else
		return NULL;
}

template<class T>
bool Link_list<T>::append(const T &sample)
{

	if (num == 0)
	{
		Node<T> *p = new Node<T>(sample);
		if (p == NULL)return false;
		first = p;
	}
	else
	{
		Node<T> *p = first;
		for (int i = 0; i < num - 1; ++i)
		{
			p = p->next;
		}
		p->next = new Node<T>(sample);
		if (p->next == NULL)return false;
	}
	++num;
	return true;
}

template<class T>
int Link_list<T>::search(const T &sample, int start)
{
	Node<T> *p = first;
	for (int i = 0; i < start; ++i)
	{
		p = p->next;
	}
	for (int i = start; i < num; ++i)
	{
		if (p->data == sample)
		{
			return i;
		}
		p = p->next;
	}
	return -1;
}
template<class T>
bool Link_list<T>::insert(const T& sample, int index)
{
	if (index >= 0 && index <= num)
	{
		Node<T> *p, *q;
		p = first;
		if (index == 0)
		{
			q = new Node<T>(sample);
			if (q == NULL)return false;
			q->next = first;
			first = q;
		}
		else if (index > 0 && index <= num)
		{
			for (int i = 1; i < index; ++i)
			{
				p = p->next;
			}
			q = p->next;
			p->next = new Node<T>(sample);
			if (q == NULL)return false;
			p->next->next = q;
		}
		else return false;
		++num;
		return true;
	}
}

template<class T>
bool Link_list<T>::erase(int index)
{
	if (index == 0)
	{
		Node<T> *p = first->next;
		delete first;
		first = p;
	}
	else if (index > 0 && index < num)
	{
		Node<T> *p = first;
		for (int i = 0; i < index - 1; ++index)
		{
			p = p->next;
		}
		Node<T> *q = p->next;
		p->next = q->next;
		delete q;
	}
	else
	{
		cerr << "Wrong parameter!";
		return false;
	}
	--num;
	return true;
}

template<class T>
void Link_list<T>::makeEmpty()
{
	this->~Link_list();
}

#endif
