#include <iostream>
#include <list>

#ifndef  COLA_H
#define COLA_H

typedef int Elemento;
using namespace std;

class Big_Integer{
	private:
		list<Elemento> Valor;
		
	public:
		Big_integer();
		Big_Integer(list<Elemento>);
		void add();
		void product();
		void substract();
		void quotiend();
		void remainder();
		void pow();
		list<Elemento> toString();
		void sumarListaValores();
		void multiplicarListaValores();
};

#endif