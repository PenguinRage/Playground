package simulation;

/**
 * 
 * Grid class
 *
 * Container class to hold the grid information.
 * This class should be a wrapper over the two dimensional array of the board.
 * 
 * @author Ian Cleasby
 *
 */

public class Grid {

	boolean[][] grid;
	int height;
	int width;
	
	
	public Grid(int height, int width) {
		this.height= height;
		this.width= width;
		grid = new boolean[height][width];
		for (int y=0; y<height;y++){
			for (int x=0;x<height;x++){
				grid[y][x] = true;
		}
		}
	}
    
	public int getHeight() {
		return height;
	}

	public int getWidth() {
		return height;
	}

	public boolean isWhite(int i, int j) {
		return grid[i][j];
	}
// if within grid set to white
	protected void setWhite(int i, int j) {
		if (i < height && j < width){
			grid[i][j]=true;
		}
	}
// if within grid set to black
	protected void setBlack(int i, int j) {
		if (i < height && j < width) {
			grid[i][j]=false;
		}
	}
}
