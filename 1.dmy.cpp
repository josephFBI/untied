// Codigo en c++ de year-month-day (optimizado)
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>      // Para stringstream
#include <iomanip>      // Para setw, setfill
#include <chrono>       // Para medición de tiempo
using namespace std;

bool es_bisiesto(int anio) {
    return (anio % 400 == 0) || (anio % 4 == 0 && anio % 100 != 0);
}

int dias_del_mes(int mes, int anio) {
    int dias[] = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    if (mes == 2 && es_bisiesto(anio)) return 29;
    return dias[mes - 1];
}

string formatear_fecha(int dia, int mes, int anio) {
    stringstream ss;
    ss << setw(2) << setfill('0') << dia
       << setw(2) << setfill('0') << mes
       << setw(4) << setfill('0') << anio;
    return ss.str();
}

//------------------------------------------------------------------

int main() {
    auto inicio = chrono::high_resolution_clock::now();

    string fecha_lim = "10062010";
    int anio_inicio = 2000;

    // Extraer fecha límite
    int dia_lim = stoi(fecha_lim.substr(0, 2));
    int mes_lim = stoi(fecha_lim.substr(2, 2));
    int anio_lim = stoi(fecha_lim.substr(4, 4));

    // Almacenamiento
    vector<string> fechas;
    fechas.reserve(5000);

    // Generar fechas
    for (int anio = anio_inicio; anio <= anio_lim; anio++) {
        int mes_fin = (anio == anio_lim) ? mes_lim : 12;

        for (int mes = 1; mes <= mes_fin; mes++) {
            int dias_mes = dias_del_mes(mes, anio);
            int dia_fin = (anio == anio_lim && mes == mes_lim) ? dia_lim : dias_mes;

            for (int dia = 1; dia <= dia_fin; dia++) {
                fechas.push_back(formatear_fecha(dia, mes, anio));
            }
        }
    }

    // Imprime los resultados
    cout << "Total de fechas generadas: " << fechas.size() << endl;
    cout << "Primera fecha: " << fechas[0] << endl;
    cout << "Última fecha: " << fechas.back() << endl;

    // Uso de ofstream para guardar el archivo
    ofstream archivo("f_C.txt");
    if (archivo.is_open()) {
        for (const string& f : fechas) {
            archivo << f << endl;
        }
        archivo.close();
        cout << "Archivo 'f_C.txt' guardado UwU." << endl;
    } else {
        cerr << "Error: No se pudo crear el archivo." << endl;
    }

    // Calculo del tiempo
    auto fin = chrono::high_resolution_clock::now();
    chrono::duration<double> duracion = fin - inicio;

    cout << "\n==============================" << endl;
    cout << "Tiempo de ejecución: " << fixed << duracion.count() << " segundos" << endl;
    cout << "Tiempo de ejecución: " << duracion.count() * 1000 << " milisegundos" << endl;
    cout << "==============================" << endl;

    return 0;
}