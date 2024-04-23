def composite_trapezoidal(a, b, f, N):
    h = (b - a) / N
    result = 0.5 * (f(a) + f(b))
    for k in range(1, N):
        result += f(a + k * h)
    return result * h

def composite_simpson(a, b, f, N):
    if N % 2 == 1:
        raise ValueError("N must be even for Simpson's rule")
    h = (b - a) / N
    result = f(a) + f(b)
    for k in range(1, N, 2):
        result += 4 * f(a + k * h)
    for k in range(2, N-1, 2):
        result += 2 * f(a + k * h)
    return result * h / 3

# result_trap = composite_trapezoidal(0, 1, lambda x: x**2, 100)
# print(result_trap)
# result_simpson = composite_simpson(0, 1, lambda x: x**2, 100)
# print(result_simpson)
