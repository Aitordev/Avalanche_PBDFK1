# Avalanche_PBDFK1
Avalanche effect analysis on PBKDF1 algorithm

Para realizar estas pruebas he usado una función de derivamiento de
clave conocida como PBKDF1, Los parámetros de la función son una función
hash, un password, un salt, un contador de iteraciones y el tamaño de la
clave ya derivada. Esta función se basa en en calcular el hash del
password concatenado con el salt, y después calcular el hash del hash
que habíamos calculado, tantas veces como estipule el contador de
iteraciones:

*K*[]{#MathJax-Span-26 .anchor}*=H(H(...H(P||S)…*)[]{#MathJax-Span-27
.anchor})

La función hash a utilizar, la cual puede ser una MD2, una MD5 o una
SHA-1, repercutirá en el tamaño de salida del algoritmo siendo de 16
octetos para MD2 y MD5, y de 20 para SHA-1. Las pruebas usaran el hash
SHA-1 ya que la salida es de mayor tamaño y es la opción por defecto del
algoritmo.

El resto de parámetros que se mantendrán en todas las pruebas, sera el
valor del contador de iteraciones a 1000, recomendado así por la
documentación del algoritmo y opción por defecto.

Para realizar este ejercicio el lenguaje de programación elegido a sido
Python y la funcion ha sido obtenida gracias al paquete pyCrypto de
Python, y podemos ver en el archivo 'test\_KDF.py' como soluciona la
función correctamente el vector de prueba, este ejecutable para probar
los vectores pertenece a la API pyCrypto de Python.

Los datos de la primera prueba, ejecutados en el archivo 'PB.py', serán
una password fija y aleatoria de tamaño 4 Bytes y lo que ira variando
sera el salt aleatorio y diferente en cada una de las iteraciones del
bucle de la prueba y de tamaño 8 Bytes, al cual variamos un bit y
calculamos la distancia de Hamming entre las claves derivadas
resultantes y volcamos el resultado en el archivo 'hamming'.

Para la segunda prueba, ejecutada en 'PBv2.py', será una password
aleatoria, la que ira variando y mantendremos el salt fijo y aleatorio
manteniendo los tamaños de la prueba anterior y calculando la distancia
de Hamming volcando el resultado sobre el archivo 'hammingv2'.

En la tercera usamos la misma estructura que en la primera, pero como
password usamos el string 'password' para poder comprobar como repercute
el que el password a cifrar sea aleatorio o no, esta prueba se realiza
con 'PBv3.py' y se vuelcan los datos en 'hammingv3'.

Todas estas pruebas las enfrentaremos al calculo de las distancias de
Hamming de funciones pseudoaleatorias, generado en el archivo 'ran.py' y
volcado en 'ran'.

El tamaño de las muestras serán de 10⁶ para cubrir una pequeña parte de
todas las posibles y tener suficientes datos para que sean de fiar.

Sobre las medidas estadísticas a calcular cabe destacar:

[]{#result_box .anchor}El valor de Skewness que mide la asimetría de la
distribución. El valor de la asimetría puede ser positivo o negativo, o
incluso indefinida. Para un valor cercano a cero es el caso de una
distribución simétrica.

La Kurtosis es un descriptor de la forma de una distribución de
probabilidad, y la Kurtosis de cualquier distribución normal univariante
es 3.

Hay que usar la prueba χ² de Pearson que mide la discrepancia entre una
distribución observada y otra teórica, indicando en qué medida las
diferencias existentes entre ambas, y probar la independencia entre las
dos variables.

![](media/image1.png){width="2.3826388888888888in"
height="0.4486111111111111in"}

Cuanto mayor sea el valor de chi cuadrado, menos verosímil es que la
hipótesis sea correcta.

![](media/image2.jpeg){width="6.6930555555555555in"
height="1.3611111111111112in"}

Adjunto las imágenes con mayor resolución como anexo: 'hist.jpg',
'histv2.jpg' e 'histv3.jpg'

Medidas estadísticas e histogramas obtenidos con Matlab y disponibles en
'crypto.m', 'cryptov2.m', 'cryptov3.m'.

  ------------------------- ----------------- ----------------- ----------------- ------------------
                            **PBDKF1 P. 1**   **PBDKF1 P. 2**   **PBDKF1 P. 3**   **F. Aleatoria**
  **Media**                 80.0080           79.9939           80.0034           80.0002
  **Mediana**               80                80                80                80
  **Moda**                  80                80                80                80
  **Varianza**              40.0587           40.0855           39.9810           40.0535
  **Desviacion Estandar**   6.3292            6.3313            6.3231            6.3288
  **Error Estandar**        0.0063            0.0063            0.0063            0.0063
  **Skewness**              -7.2674e-04       0.0012            -0.0048           0.0030
  **Kurtosis**              2.9872            2.9869            2.9864            2.9896
  **Rango**                 59                58                66                59
  **Maximo**                111               109               114               110
  **Minimo**                52                51                51                51
  **Sum**                   80007962          79993924          80003366          80000159
  **Chi Cuadrado**          0.3334            0.3335            0.3333            
  ------------------------- ----------------- ----------------- ----------------- ------------------

Como podemos ver una vez obtenidos todos los datos tenemos
distribuciones simétricas, normales y univariantes en todos los casos.

En los histogramas la diferencia entre el algoritmo y una función
aleatoria es mínima y con los resultados de chi cuadrado podemos
certificar que las tres pruebas no se diferencian de una distribución
uniforme y aleatoria con un grado de significación del 0,5%.

Referencias

[*https://www.dlitz.net/software/pycrypto/*](https://www.dlitz.net/software/pycrypto/)
- Api criptográfica usada.

[*https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html*](https://www.dlitz.net/software/pycrypto/api/current/Crypto.Protocol.KDF-module.html)
- Documentación del algoritmo y sus parámetros dentro de la Api.

*http://www.di-mgt.com.au/cryptoKDFs.html\#examplespbkdf* - Vectores de
ejemplo

*https://tools.ietf.org/html/rfc2898\#section-5.1* - PBKDF1 en el RFC
2898 (Specification of PKCS \#5 v2.0.)

[*https://en.wikipedia.org/wiki/Skewness*](https://en.wikipedia.org/wiki/Skewness)
- Skewness

[*https://en.wikipedia.org/wiki/Kurtosis*](https://en.wikipedia.org/wiki/Kurtosis)
- Kurtosis

[*https://es.wikipedia.org/wiki/Prueba\_%CF%87%C2%B2\_de\_Pearson*](https://es.wikipedia.org/wiki/Prueba_χ²_de_Pearson)
- Chi cuadrado

[*https://es.wikipedia.org/wiki/Significaci%C3%B3n\_estad%C3%ADstica*](https://es.wikipedia.org/wiki/Significación_estadística)
- Significación estadística para chi Cuadrado

[https://www.tackoverflow.com](https://www.tackoverflow.com/) - Dudas y
errores de programación