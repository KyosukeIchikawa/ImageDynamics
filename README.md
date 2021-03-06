# ImageDynamics
I tried to solve the equation of motion considered the image as a two dimensional scalar field.
By this method, I think that the image can be in various forms.

## Case 1: Wave equation
<img src="./img/waveeq1.gif"/>
<img src="./img/waveeq2.gif"/>
Solving the above wave equation, the solution is as follows.
It seems to be vibrating in the earthquake.
<table border="0" cellspacing="0" cellpadding="5" bordercolor="#333333">
<tr>
<td><img src="./img/waveeq_caffe0.png"/>
<td><img src="./img/waveeq_caffe10.png"/>
<td><img src="./img/waveeq_caffe20.png"/>
</tr>
</table>

## Case 2: Diffusion equation
<img src="./img/diffeq1.gif"/>
<img src="./img/diffeq2.gif"/>
Solving the above diffusion equation, the solution is as follows.
It seems that RGB are averaged so that the temperature distribution becomes thermal equilibrium.
<table border="0" cellspacing="0" cellpadding="5" bordercolor="#333333">
<tr>
<td><img src="./img/diffeq_garden0.png"/>
<td><img src="./img/diffeq_garden10.png"/>
<td><img src="./img/diffeq_garden20.png"/>
</tr>
</table>

## Case 3: Diffusion equation (Negative diffusion coefficient)
<img src="./img/diffeq3.gif"/>
<img src="./img/diffeq2.gif"/>
Solving the above diffusion equation (Negative diffusion coefficient), the solution is as follows.
An unnatural expression that heat moves from low temperature to high temperature.
In the image, you can see the effect of emphasizing the boundary.
<table border="0" cellspacing="0" cellpadding="5" bordercolor="#333333">
<tr>
<td><img src="./img/diffeq2_garden0.png"/>
<td><img src="./img/diffeq2_garden20.png"/>
<td><img src="./img/diffeq2_garden40.png"/>
</tr>
</table>

## Case 4: Cahn-Hilliard equation
<img src="./img/cahneq1.gif"/>
Details will be released in the future.<br>
Solving the above Cahn-Hilliard equation, the solution is as follows.
This is an expression that describes a two-phase fluid.
In the image, we believe that it is possible to extract the object so much (while adjusting the coefficient).
<table border="0" cellspacing="0" cellpadding="5" bordercolor="#333333">
<tr>
<td><img src="./img/cahneq1_caffe0pre.png"/>
<td><img src="./img/cahneq1_caffe0.png"/>
<td><img src="./img/cahneq1_caffe1.png"/>
<td><img src="./img/cahneq1_caffe2.png"/>
</tr>
<tr>
<td><img src="./img/cahneq1_caffe3.png"/>
<td><img src="./img/cahneq1_caffe4.png"/>
<td><img src="./img/cahneq1_caffe5.png"/>
<td><img src="./img/cahneq1_caffe20.png"/>
</tr>
</table>
