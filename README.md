# Donut_Renderer: 3D Illusion Interaction

This is a Python program that generates an animated donut using the Pygame library. The donut rotates and creates an illusion of a 3D shape. Each frame of the animation is displayed on the screen using characters and colors.The spinning “donuts” ASCII renderer . The “pixels” are ASCII characters .,-~:;=!*#$@ that accounts for the illumination value of the surface.


<p align="center"> <img src="https://github.com/abelyo252/Donut_Renderer/blob/main/donut-animation.gif"> </p>

    
    
## Installation

To install the most recent version of Clone-Keras, just follow these simple instructions. I use Python 3.11.4 for this project; you can download 3.11.4 from [here](https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe) ,if the two are incompatible, try another version by searching online. If git wasn't installed on your Windows PC, get it from `https://gitforwindows.org/` or install it on linux using `sudo apt-get install git` 

`git clone https://github.com/abelyo252/Donut_Renderer.git`<br>
`cd Donut_Renderer/`<br>
`pip install -r requirements.txt`<br>

---


## Run Code using main.py

`$ python main.py`<br>


---

## The donut | math

A donut or torus can be created by revolving a circle, placed a distance bigger than its radius from an axis, around this axis. Let's call the radius of our circle R₁ and the radius of the torus R₂.


<p align="center"> <img src="https://github.com/abelyo252/Donut_Renderer/blob/main/math/1.png"> </p>


The function formula for a circle with radius r and center M(a, b) is: From this formula, we can derive the parametric equation (which will be easier to work with). To do this we can start with the Pythagorean identity: This equation looks very similar to our previous function formula. Converting the formula of a circle into its parametric equation would look like this:


<p align="center"> <img src="https://github.com/abelyo252/Donut_Renderer/blob/main/math/2.png"> </p>

Well, how to map this 3D object into 2D ie terminal screen?

To map a 3D object onto a 2D terminal screen, you'll need to perform a process called projection. In the provided code, the donut animation is already projected onto a 2D screen using characters. The projection is achieved by representing each point in 3D space as a character on the 2D screen. The x and y coordinates of each point are determined based on its position relative to the screen, and the z-coordinate (depth) is used to determine the color and brightness of the character.
<p align="center"> <img src="https://github.com/abelyo252/Donut_Renderer/blob/main/math/view.png"> </p>

The output of the dot product will be:

Finally you map the result of the dot product to these characters to tweak the lighting. That’s it!


<p align="center"> <img src="https://github.com/abelyo252/Donut_Renderer/blob/main/math/4.png"> </p>


Each character in the code corresponds to a pixel on our terminal. However, how to shade it? For this, we calculate the dot product of the surface normal and the direction of the light. This will say how light and how dark will look on the screen.


---
## Support

You can ask questions and join the development discussion:

- @ Telegram t.me/@benyohanan

---

## Opening an issue

You can also post **bug reports and feature requests** (only)
in [GitHub issues](https://github.com/ab).


---

## Opening a PR

I'm welcome for contributions! Before opening a PR, please read
[contributor guide](https://github.com/blob/master/CONTRIBUTING.md)

