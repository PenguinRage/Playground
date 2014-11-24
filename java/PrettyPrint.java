package pretty;

/*
	 ___     ___        ___        ___        ___   __   __
|    \  |    \  \    ___) (__    __) (__    __) (  (  )  ) 
|     ) |     )  |  (__      |  |       |  |     \  \/  /  
|  __/  |    /   |   __)     |  |       |  |      \    /   
| |     | |\ \   |  (___     |  |       |  |       )  /    
| |_____| |_\ \_/       )____|  |_______|  |______/  (_____
     ___     ____      __     ___    __        __
|    \  |    \  (_    _) |    \  |  | (__    __) 
|     ) |     )   |  |   |  |\ \ |  |    |  |    
|  __/  |    /    |  |   |  | \ \|  |    |  |    
| |     | |\ \   _|  |_  |  |  \    |    |  |    
| |_____| |_\ \_(      )_|  |___\   |____|  |____
By Ian Cleasby

REQUIREMENTS:
choose rectangle, triangle, diamond
Rectangle: Parse two integers
Triangle: Parse one integer
Diamond: Parse one integer


*/


public class PrettyPrint {

	// Method for creating spaces.
	public static String createSpaces(int size) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < size; i++) {
			sb.append(" ");
		}
		return sb.toString();
	}

	// Method for making the left and right parts in the rectangle.
	public static String createRectangleLeftAndRight(int width) {
		StringBuilder sb = new StringBuilder();
		sb.append("|");
		sb.append(createSpaces(width));
		sb.append("|\n");

		return sb.toString();
	}

	// Method for making the top and bottom part in the rectangle.
	public static String createRectangleTopAndBottom(int width) {
		StringBuilder sb = new StringBuilder();
		sb.append("+");
		for (int i = 0; i < width; i++) {
			sb.append("-");
		}
		sb.append("+\n");

		return sb.toString();
	}

	// Method for making left and right part of the triangle.
	public static String createTriangleLeftAndRight(int size) {
		StringBuilder sb = new StringBuilder();
		sb.append("|");
		sb.append(createSpaces(size));
		sb.append("\\\n");

		return sb.toString();
	}

	// Method for creating the bottom part of the Triangle.
	public static String createTriangleBottom(int size) {
		StringBuilder sb = new StringBuilder();
		sb.append("+");
		for (int i = 0; i < size; i++) {
			sb.append("-");
		}
		sb.append("+\n");

		return sb.toString();
	}

	// Method for creating the top "+" and bottom "+" in the diamond.
	public static String createDiamondTopAndBottom(int size) {
		StringBuilder sb = new StringBuilder();
		sb.append(createSpaces(size + 1));
		sb.append("+\n");

		return sb.toString();
	}

	// Method for creating the upper body of the diamond.
	public static String createDiamondUpperBody(int size) {
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < size; i++) {
			sb.append(createSpaces(size - i));
			sb.append("/");
			sb.append(createSpaces(i * 2 + 1));
			sb.append("\\\n");

		}
		return sb.toString();
	}

	// Method for creating the middle part of the diamond.
	public static String createDiamondMiddle(int size) {
		StringBuilder sb = new StringBuilder();
		sb.append("+");
		sb.append(createSpaces(size * 2 + 1));
		sb.append("+\n");

		return sb.toString();
	}

	// Method for creating the lower body part of the diamond.
	public static String createDiamondLowerBody(int size) {
		StringBuilder sb = new StringBuilder();
		for (int i = size; i > 0; i--) {
			sb.append(createSpaces(size + 1 - i));
			sb.append("\\");
			sb.append(createSpaces(i * 2 - 1));
			sb.append("/\n");
		}
		return sb.toString();
	}

	// Method for printing out the rectangle shape.
	public static void printRectangle(int height, int width) {
		if (height >= 0 && width >= 0) {
			System.out.print(createRectangleTopAndBottom(width));
			for (int i = 0; i < height; i++) {
				System.out.print(createRectangleLeftAndRight(width));
			}
			System.out.print(createRectangleTopAndBottom(width));
		}
	}

	// Method for printing out the triangle shape.
	public static void printTriangle(int size) {
		if (size >= 0) {
			System.out.println("+");
			for (int i = 0; i < size; i++) {
				System.out.print(createTriangleLeftAndRight(i));
			}
			System.out.print(createTriangleBottom(size));
		}
	}

	public static void printDiamond(int size) {
		if (size >= 0) {
			System.out.print(createDiamondTopAndBottom(size));
			System.out.print(createDiamondUpperBody(size));
			System.out.print(createDiamondMiddle(size));
			System.out.print(createDiamondLowerBody(size));
			System.out.print(createDiamondTopAndBottom(size));
		}
	}

	public static void main(String[] args) {
		// Converting args[0] to lower-case and comparing it to lower case, which makes it case insensitive.
		String shape = args[0].toLowerCase();
		if (shape.equals("rectangle")) {
			// checking if we have enough arguments
			if (args.length >= 3) {
				// Get command line arguments, make them integers, and then call printXXX with the integers.
				printRectangle(Integer.parseInt(args[1]),
						Integer.parseInt(args[2]));
			}

		} else if (shape.equals("triangle")) {
			// checking if we have enough arguments
			if (args.length >= 2) {
				// Get command line arguments, make them integers, and then call printXXX with the integer.
				printTriangle(Integer.parseInt(args[1]));
			}

		} else if (shape.equals("diamond")) {
			// checking if we have enough arguments
			if (args.length >= 2) {
				// Get command line arguments, make them integers, and then call printXXX with the integer.
				printDiamond(Integer.parseInt(args[1]));
			}
		// if none of the conditions above true, print "error" message.
		} else {
			System.out.println("I do not recognise that shape");
		}
	}
}
