<h1> Combi </h1>
<h4> Asistente de combinatoria. </h4><br> 
<br>
<h2> VARIACIONES SIN REPETICIÓN </h2><br>
<br>
<br>
<p>Determina cuantos grupos de **n** elementos se pueden crear dentro del total de elementos, **m**, sin repetir elementos.</p><br>
<br>
<p>Por ejemplo: Los grupos (1,1) y (2,2) serían grupos formados permitiendo repeticiones.</p><br>
<br>
> Formula:
> Vm,n = m * (m-1) * (m-2)... * (m-n+1)
>
> m = Total de elementos
> n = Cantidad de elementos que forman cada grupo dentro del total.
<br>
<br>
<h3>Ejemplo:</h3><br>
Variaciones de 2 elementoa dentro de un total de 4 elelementos.<br>
<br>  
Total de elementos: 4<br>  
[1] [2] [3] [4]<br>
<br>
Tamaño de grupos formados con esos 4 elementos (Sin repeticiones): 12<br>
<br>
[1]--[2]   [2]--[1]   [3]--[1]   [4]--[1]<br>           
[1]--[3]   [2]--[3]   [3]--[2]   [4]--[2]<br>  
[1]--[4]   [2]--[4]   [3]--[3]   [4]--[3]<br>
<br>
<br>
<h2> VARIACIONES CON REPTICIÓN </h2> 
<br>
<p>Determina cuantos grupos de m elementos se pueden crear tomando "n" elementos del total "m" pudiendo repetir elementos.
<p>Por ejemplo Los grupos (1,2) y (2,1) contarían como grupos diferentes aunque contengan los mismos elementos porque están en diferente orden.
<br>
> Formula:
> VRm,n = m^n
>
> m = Total de elementos
> n = Cantidad de elementos que forman los grupos buscados.