package imagery;

import java.awt.Color;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

/*
 __  _  _   __    ___  ____  ____  __  __    ____  ____ 
(  )( \/ ) /__\  / __)(  __)(_  _)(  )(  )_ (  __)(  _ \
(  )( /\ )/ \/ \| (_ \(  __) (  ) (  )(_/\ )(  __)( |/ /
(__)\_)(_/\_/\_/ \___/(____) (__) (__)\____/(____)(_|\_)
By Ian Cleasby 
PURPOSE: to import an image and create a new image of 4 different colored windows.

REQUIREMENTS:
- image
- location - needs to be given. In this case pasing through args.

OUTPUT: will be saved in same folder
*/

public class ImageTiler {
	

	public static BufferedImage getTileImage(BufferedImage Image) {
		// GRABBING PROPERTIES FROM OUR GLOBAL VARIABLE
		BufferedImage tileimage = new BufferedImage(Image.getWidth(),
				Image.getHeight(), BufferedImage.TYPE_INT_RGB);
 
		// ------------------ GRIDING STARTS HERE -------------------	
		// NESTED FOR LOOP TO MAKE GRID ON IMAGE
		for (int i = 2; i < Image.getWidth(); i = i + 2) {
			for (int j = 2; j < Image.getHeight(); j = j + 2) {
				int red = 0, green = 0, blue = 0;
				// NESTED FOR LOOPS TO CALCULATE NEIGHBOURING AVERAGE PIXELS
				for (int k = 2; k > 0; k--) {
					for (int l = 2; l > 0; l--) {
						int color1 = Image.getRGB(i-k,j-l);
						Color c = new Color(color1);
						blue=blue + c.getBlue();
						green=green +c.getGreen();
						red=red +c.getRed();
					}
				}
				// ------------------ GRIDING ENDS HERE --------------------
				// ---------------COLOR CODING STARTS HERE------------------
				// AVERAGE COLORS FOR TOP LEFT CORNER
				Color tint = new Color(red/4,green/4,blue/4);
				tileimage.setRGB((i/2)-1, (j/2)-1, tint.getRGB());
				
				// AVERAGE OF RED AND BLUE FOR TOP RIGHT CORNER
				Color tintb = new Color(red/4,0,blue/4);
				tileimage.setRGB((i/2)-1+(Image.getWidth()/2), (j/2)-1, tintb.getRGB());
				
				// AVERAGE OF GREEN AND RED FOR BOTTOM LEFT
				Color tintgr = new Color(red/4,green/4,0);
				tileimage.setRGB((i/2)-1, (j/2)-1 +(Image.getHeight()/2), tintgr.getRGB());
				
				// AVERAGE OF GREEN AND BLUE FOR BOTTOM RIGHT
				Color tintgb = new Color(0,green/4,blue/4);
				tileimage.setRGB((i/2)-1 + (Image.getWidth()/2), (j/2)-1 +(Image.getHeight()/2), tintgb.getRGB());
				//----------------COLOR CODING ENDS HERE------------------
			}
		}
		return tileimage;
	}

	// CREATES NEW IMAGE FOR ANY IMAGE CALLED IN CMD
	private static BufferedImage createNewImage(String location) {
		try {
			System.out.println("Looking for image file.");
			BufferedImage image = ImageIO.read(new File(location));

			return image;

		} catch (IOException e) {
			return null;
		}

	}

	// MAIN FUNCTION
	public static void main(String[] args) {
		try {
			// TERMINAL COMMAND
			String location = args[0];
			BufferedImage Image = createNewImage(location);
			BufferedImage coolImage = getTileImage(Image);
			// OUTPUT OF NEW IMAGE
			int length = location.length() - 4;
			File outputfile = new File(location.substring(0, length)
					+ "-tiled.png");
			ImageIO.write(coolImage, "png", outputfile);
			// NO FILE EXISTS
		} catch (IOException e) {
			System.out.println("Sorry, I cannot find that file.");
		}
		// --------------- END OF ROAD ----------------
	}
}
