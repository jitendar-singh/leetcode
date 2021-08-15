import bisect

A = [-14, -10, 2, 108, 108, 108, 243, 285, 285, 285,401]

print(bisect.bisect_left(A,108))
print(bisect.bisect_right(A,-10))

print(bisect.bisect(A,-10))
bisect.insort_left(A,-108)
print(A)
bisect.insort(A,399)
print(A)
