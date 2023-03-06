# CMPS 2200 Assignment 2

**Name:** Griffin Olimpio

In this assignment we'll work on applying the methods we've learned to analyze recurrences, and also see their behavior
in practice. As with previous
assignments, some of of your answers will go in `main.py`.. You
should feel free to edit this file with your answers; for handwritten
work please scan your work and submit a PDF titled `assignment-02.pdf`
and push to your github repository.


1. Derive asymptotic upper bounds of work for each recurrence below.
  * $W(n)=2W(n/3)+1$
.  
.  a = 2, b = 3, f(n) = 1, and log_b(a) = log_3(2) ≈ 0.631

Since f(n) = Θ(1) and log_b(a) < 1, the recurrence is case 1 of the master theorem.

Therefore, W(n) = Θ(n^(log_b(a))) = Θ(n^log_3(2)).

Hence, the asymptotic upper bound of work for W(n) is Θ(n^log_3(2)).
.  
.  
.  
  * $W(n)=5W(n/4)+n$
.  
.  a = 5, b = 4, f(n) = n, and log_b(a) = log_4(5) ≈ 1.16

Since f(n) = Θ(n) and log_b(a) > 1, the recurrence is case 3 of the master theorem.

Therefore, W(n) = Θ(n^(log_b(a))) = Θ(n^log_4(5)).

Hence, the asymptotic upper bound of work for W(n) is Θ(n^log_4(5)).
.  
.  
.  
  * $W(n)=7W(n/7)+n$
.  
.  a = 7, b = 7, f(n) = n, and log_b(a) = log_7(7) = 1

Since f(n) = Θ(n) and log_b(a) = 1, the recurrence is case 2 of the master theorem.

Therefore, W(n) = Θ(nlog_b(a)) = Θ(n).

Hence, the asymptotic upper bound of work for W(n) is Θ(n).
.  
.  
.  
  * $W(n)=9W(n/3)+n^2$
.  
.  a = 9, b = 3, f(n) = n^2, and log_b(a) = log_3(9) = 2

Since f(n) = Θ(n^2) and log_b(a) > 1, the recurrence is case 3 of the master theorem.

Therefore, W(n) = Θ(n^(log_b(a))) = Θ(n^2).

Hence, the asymptotic upper bound of work for W(n) is Θ(n^2).
.  
.  
.  
  * $W(n)=8W(n/2)+n^3$
.  
.  a = 8, b = 2, f(n) = n^3, and log_b(a) = log_2(8) = 3

Since f(n) = Θ(n^3) and log_b(a) > 2, the recurrence is case 3 of the master theorem.

Therefore, W(n) = Θ(n^(log_b(a))) = Θ(n^3).

Hence, the asymptotic upper bound of work for W(n) is Θ(n^3).
.  
.  
.  
  * $W(n)=49W(n/25)+n^{3/2}\log n$
.  
.  a = 49, b = 25, and d = 3/2. Log base b of a is 2. Therefore, the solution is W(n) = Θ(n^(3/2)log^2 n).


.  
.  
.  
  * $W(n)=W(n-1)+2$
.  
.  W(n) = 2n + W(0). Therefore, the solution is W(n) = Θ(n).
.  
.  
.  
  * $W(n)= W(n-1)+n^c$, with $c\geq 1$
.  
.   W(n) = (n^c + c(n-1)) / c!. Therefore, the solution is W(n) = Θ(n^c / c!).
.  
.  
.  
  * $W(n)=W(\sqrt{n})+1$

Let k = log base 2 of n. Then, we have W(2^k) = W(2^(k/2)) + 1. Repeating this substitution, we have W(2^k) = W(2^(k/2^i)) + i for i = 0, 1, ..., k. Substituting back, we have W(n) = W(2^(log base 2 of n)) + log base 2 of log base 2 of n. Therefore, the solution is W(n) = Θ(log log n).


2. Suppose that for a given task you are choosing between the following three algorithms:

  * Algorithm $\mathcal{A}$ solves problems by dividing them into
      five subproblems of half the size, recursively solving each
      subproblem, and then combining the solutions in linear time.
    
  * Algorithm $\mathcal{B}$ solves problems of size $n$ by
      recursively solving two subproblems of size $n-1$ and then
      combining the solutions in constant time.
    
  * Algorithm $\mathcal{C}$ solves problems of size $n$ by dividing
      them into nine subproblems of size $n/3$, recursively solving
      each subproblem, and then combining the solutions in $O(n^2)$
      time.

    What are the asymptotic running times of each of these algorithms?
    Which algorithm would you choose?

• Algorithm A: T(n) = 5T(n/2) + O(n)
= O(n^(log_2 5))

• Algorithm B: T(n) = 2T(n-1) + O(1)
= O(2^n)

• Algorithm C: T(n) = 9T(n/3) + O(n^2)
= O(n^2(log_3 9))

Of the three algorithms, Algorithm A has the best asymptotic runtime, and would likely be the best choice for large problem sizes.


3. Now that you have some practice solving recurrences, let's work on
  implementing some algorithms. In lecture we discussed a divide and
  conquer algorithm for integer multiplication. This algorithm takes
  as input two $n$-bit strings $x = \langle x_L, x_R\rangle$ and
  $y=\langle y_L, y_R\rangle$ and computes the product $xy$ by using
  the fact that $xy = 2^{n/2}x_Ly_L + 2^{n/2}(x_Ly_R+x_Ry_L) +
  x_Ry_R.$ Use the
  stub functions in `main.py` to implement Karatsaba-Ofman algorithm algorithm for integer
  multiplication: a divide and conquer algorithm that runs in
  subquadratic time. Then test the empirical running times across a
  variety of inputs to test whether your code scales in the manner
  described by the asymptotic runtime. Please refer to Recitation 3 for some basic implementations, and Eqs (7) and (8) in the slides https://github.com/allan-tulane/cmps2200-slides/blob/main/module-02-recurrences/recurrences-integer-multiplication.ipynb
 
 


