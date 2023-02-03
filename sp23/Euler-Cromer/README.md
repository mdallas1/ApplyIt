# ApplyIt Feb 9, 2023: The Euler-Cromer Method

## Introduction
 The motion of a particle of mass $m$ experiencing an external force may be analyzed using Newton's second law: $F=ma$. If $x(t)$ is the particle's position at time $t$, then $a=\ddot{x}$. Here we've used the dot notation for the deriative with respect to time. We can write Newton's second law as a system of first order order odes.
 
 $$\begin{equation} \begin{split}\dot{v}&=F, v(0)=v_0 
 
 \\ \dot{x}&=v, x(0)=x_0. \end{split}\end{equation}$$

Note that $v$ and $x$ may be vectors. In which case (1) is a system of $2N$ odes, where $N$ is the spatial dimension of the problem at hand. Given an initial position and velocity, one may attempt to solve this system by discretizing in time, $t_n = t_0+n\Delta t$, and applying the standard forward-Euler method, yielding the iterative process
$$\begin{equation}\begin{split} v_{n+1}&=v_n+F_n\Delta t\\ 
x_{n+1}&=x_n+v_n\Delta t, \end{split}\end{equation}$$
where the subscript denotes evaluation at $t_n$.
However, this approach can lead to unstable and non-physical solutions, as we'll soon see. An alternative approach is to apply a the semi-implicit method known as the *Euler-Cromer method* which takes the form
$$\begin{equation}\begin{split}  v_{n+1}&=v_n+F_n\Delta t\\ 
x_{n+1}&=x_n+v_{n+1}\Delta t. \end{split}\end{equation}$$
The term *semi-implicit* here refers to the fact that only one of the equations above, namely, the equation for $x_{n+1}$, has $t_{n+1}$ on both sides of the equation. The right-hand side of the equation for $v_{n+1}$ only depends on $t_n$.
The Euler-Cromer method is particularly effective in the context of oscillatory problems. In this case, one can show that the Euler-Cromer method produces highly stable solutions, and that on average it conserves the energy of the system in question. For proof of these claims, see [Stable solutions using the Euler approximation](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/cromer81.pdf). 

## Goal
In this meeting, we'll first implement the Euler-Cromer method, compare it's performance to that of the standard Euler method on a simple 1D problem. We'll then solve a 2D problem where a mass $m$ is orbiting two other masses $M_1$ and $M_2$ in space. In the last part of the session, we'll write a solver that takes in the parameters of the problem, and solves the Newton system (1) defined by those parameters in 2D (or 3D) using a method of the user's choice.  

Numerical results for the problems discussed above (for various initial conditions) may be found in [Stable solutions using the Euler approximation](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/cromer81.pdf). The form of Newton's equations for the three-body problem can be found in [Euler's three-body problem](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/wild79.pdf).

## Symplectic Integrators
The Euler-Cromer method, also known as the semi-implicit Euler method, is an example of a [*symplectic integrator*](https://en.wikipedia.org/wiki/Symplectic_integrator), which itself is an example of a [*geometric integrator*](https://en.wikipedia.org/wiki/Geometric_integrator). Symplectic integrators are, evidently, often used to solve Hamiltonian systems. That is, systems governed by [Hamilton's equations](https://en.wikipedia.org/wiki/Hamiltonian_mechanics). For an introduction to symplectic integrators, see 
[Symplectic integrators: an introduction](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/DoRo05.pdf).

## Literature
1. [Euler's three-body problem](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/wild79.pdf)
2. [Stable solutions using the Euler approximation](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/cromer81.pdf) 
3. [Symplectic integrators: an introduction](https://github.com/mdallas1/ApplyIt/tree/main/sp23/Euler-Cromer/papers/DoRo05.pdf) 
