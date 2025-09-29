
<h1> Combi </h1>
<h4> Asistente de combinatoria. </h4> 

<h2> VARIACIONES SIN REPETICIÓN </h2>


<p>Determina cuantos grupos de **n** elementos se pueden crear dentro del total de elementos, **m**, sin repetir elementos.</p>

<p>Por ejemplo Los grupos (1,2) y (2,1) contarían como el mismo grupo.</p>

> Formula:
> Vm,n = m * (m-1) * (m-2)... * (m-n+1)
>
> m = Total de elementos
> n = Cantidad de elementos que forman los grupos buscados.


<h3>Ejemplo:</h3>
Variaciones de 2 elementoa dentro de un total de 4 elelementos.
 
Total de elementos: 4
[1] [2] [3] [4]

Tamaño de grupos formados con esos 4 elementos (Sin repeticiones): 12

[1]--[2]   [2]--[1]   [3]--[1]   [4]--[1]               
[1]--[3]   [2]--[3]   [3]--[2]   [4]--[2]  
[1]--[4]   [2]--[4]   [3]--[3]   [4]--[3] 