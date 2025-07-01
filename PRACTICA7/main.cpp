// Laboratorio 7: Códigos Huffman
// Lenguaje: C++
// Autor: Aguillon Mora Angel
// Fecha de entrega: 21 de mayo de 2025

#include <iostream>
#include <fstream>
#include <queue>
#include <unordered_map>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cctype>
using namespace std;

// Nodo para el árbol de Huffman
struct HuffmanNode {
    char simbolo;
    int frecuencia;
    HuffmanNode *izquierda, *derecha;

    HuffmanNode(char s, int f) : simbolo(s), frecuencia(f), izquierda(nullptr), derecha(nullptr) {}
};

struct Comparador {
    bool operator()(HuffmanNode* a, HuffmanNode* b) {
        return a->frecuencia > b->frecuencia;
    }
};

// Normaliza el texto: minúsculas y sin acentos/símbolos
string normalizarTexto(const string& texto) {
    string resultado;
    for (char c : texto) {
        if (isalpha(c)) {
            resultado += tolower(c);
        } else if (isspace(c)) {
            resultado += c;
        }
    }
    return resultado;
}

// Funcíon para generar el diccionario de frecuencias
unordered_map<char, int> generarFrecuencias(const string& texto) {
    unordered_map<char, int> frecuencias;
    for (char c : texto) {
        frecuencias[c]++;
    }
    return frecuencias;
}

// Construye el árbol de Huffman
HuffmanNode* construirArbolHuffman(const unordered_map<char, int>& frecuencias) {
    priority_queue<HuffmanNode*, vector<HuffmanNode*>, Comparador> minHeap;

    for (auto par : frecuencias) {
        minHeap.push(new HuffmanNode(par.first, par.second));
    }

    while (minHeap.size() > 1) {
        HuffmanNode* izquierda = minHeap.top(); minHeap.pop();
        HuffmanNode* derecha = minHeap.top(); minHeap.pop();

        HuffmanNode* fusion = new HuffmanNode('\0', izquierda->frecuencia + derecha->frecuencia);
        fusion->izquierda = izquierda;
        fusion->derecha = derecha;
        minHeap.push(fusion);
    }

    return minHeap.top();
}

// Genera los códigos de Huffman
void generarCodigos(HuffmanNode* raiz, const string& codigo, unordered_map<char, string>& codigos) {
    if (!raiz) return;
    if (raiz->simbolo != '\0') {
        codigos[raiz->simbolo] = codigo;
    }
    generarCodigos(raiz->izquierda, codigo + "0", codigos);
    generarCodigos(raiz->derecha, codigo + "1", codigos);
}

// Guarda los códigos Huffman en un archivo
void guardarCodigos(const unordered_map<char, string>& codigos, const string& nombreArchivo) {
    ofstream archivo(nombreArchivo);
    for (const auto& par : codigos) {
        archivo << par.first << ' ' << par.second << '\n';
    }
    archivo.close();
}

// Codifica el texto
string codificarTexto(const string& texto, const unordered_map<char, string>& codigos) {
    string resultado;
    for (char c : texto) {
        resultado += codigos.at(c);
    }
    return resultado;
}

// Calcula la tasa de compresión
void calcularTasaCompresion(const string& original, const string& codificado) {
    int bitsOriginal = original.size() * 8;
    int bitsCodificado = codificado.size();
    cout << "Tamanio original en bits: " << bitsOriginal << endl;
    cout << "Tamanio codificado en bits: " << bitsCodificado << endl;
    cout << "Tasa de compresion: " << (double)bitsCodificado / bitsOriginal << endl;
}

// Decodifica el texto
string decodificarTexto(const string& codificado, HuffmanNode* raiz) {
    string resultado;
    HuffmanNode* actual = raiz;
    for (char bit : codificado) {
        if (bit == '0') actual = actual->izquierda;
        else actual = actual->derecha;

        if (!actual->izquierda && !actual->derecha) {
            resultado += actual->simbolo;
            actual = raiz;
        }
    }
    return resultado;
}

int main() {
    // Paso 1: Cargar archivo y normalizar
    ifstream archivoEntrada("entrada.txt");
    string texto((istreambuf_iterator<char>(archivoEntrada)), istreambuf_iterator<char>());
    archivoEntrada.close();
    texto = normalizarTexto(texto);

    // Paso 2: Generar frecuencias
    auto frecuencias = generarFrecuencias(texto);

    // Paso 3: Construir árbol
    HuffmanNode* arbol = construirArbolHuffman(frecuencias);

    // Paso 4: Generar códigos
    unordered_map<char, string> codigos;
    generarCodigos(arbol, "", codigos);

    // Guardar códigos Huffman
    guardarCodigos(codigos, "codigos.huff");

    // Paso 5: Codificar
    string textoCodificado = codificarTexto(texto, codigos);

    // Paso 6: Calcular tasa de compresión
    calcularTasaCompresion(texto, textoCodificado);

    // Paso 7: Guardar archivo codificado
    ofstream archivoCodificado("codificado.txt");
    archivoCodificado << textoCodificado;
    archivoCodificado.close();

    // Paso 8: Cargar y decodificar archivo
    ifstream archivoLeido("codificado.txt");
    string textoLeido((istreambuf_iterator<char>(archivoLeido)), istreambuf_iterator<char>());
    archivoLeido.close();

    string textoDecodificado = decodificarTexto(textoLeido, arbol);

    // Paso 9: Guardar archivo decodificado
    ofstream archivoDecodificado("decodificado.txt");
    archivoDecodificado << textoDecodificado;
    archivoDecodificado.close();

    cout << "\nTexto decodificado:\n" << textoDecodificado << endl;

    return 0;
}