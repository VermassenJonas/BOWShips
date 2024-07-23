

from decimal import Decimal

class Interpolator:
	@staticmethod
	def linear_interpolation( x, *points):
		
		points = sorted(points)               # order points by x, then by y
		(x1, q1), (x2, q2) = points

		if not x1 <= x <= x2:
			raise ValueError('x not within the interval')
		if q1<=0 or q2 <= 0:
			raise ValueError('bad data or invalid combination')
		return (q1 * (x2-x)+ q2 *(x-x1)) / (x2-x1)
	@staticmethod
	def bilinear_interpolation( x, y, *points): # from stackoverflow
		'''Interpolate (x,y) from values associated with four points.

		The four points are a list of four triplets:  (x, y, value).
		The four points can be in any order.  They should form a rectangle.

			>>> bilinear_interpolation(12, 5.5,
			...                        [(10, 4, 100),
			...                         (20, 4, 200),
			...                         (10, 6, 150),
			...                         (20, 6, 300)])
			165.0

		'''
		points = sorted(points)               # order points by x, then by y
		(x1, y1, q11), (_x1, y2, q12), (x2, _y1, q21), (_x2, _y2, q22) = points

		if x1 != _x1 or x2 != _x2 or y1 != _y1 or y2 != _y2:
			raise ValueError('points do not form a rectangle')
		if not x1 <= x <= x2 or not y1 <= y <= y2:
			raise ValueError('(x, y) not within the rectangle')		
		q1 = Interpolator.linear_interpolation(x, (x1, q11), (x2, q21) )
		q2 = Interpolator.linear_interpolation(x, (x1, q12), (x2, q22) )
		return Interpolator.linear_interpolation(y, (y1, q1) , (y2, q2))
	

if __name__ == '__main__':
	ipol = Interpolator
	print(ipol.linear_interpolation(4.5, (4, 10), (10,15)))

	print(ipol.bilinear_interpolation(12, 5.5,
		(10, 4, 100),
		(20, 4, 200),
		(10, 6, 150),
		(20, 6, 300)))